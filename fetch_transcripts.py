#!/usr/bin/env python3
"""Fetch YouTube transcripts for SEO experts using the Supadata API."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], check=True)
    import requests

BASE_URL = "https://api.supadata.ai/v1"
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "research" / "youtube-transcripts"
VIDEOS_PER_EXPERT = 5
REQUEST_TIMEOUT = 60

EXPERTS: dict[str, str] = {
    "nathan_gotch": "https://www.youtube.com/@NathanGotch",
    "glen_allsopp": "https://www.youtube.com/@Detailed",
    "koray_tugberk": "https://www.youtube.com/@KorayTugberkGubur",
    "lily_ray": "https://www.youtube.com/@LilyRaySEO",
    "mike_king": "https://www.youtube.com/@iPullRank",
}


def parse_env_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe"):
        text = raw.decode("utf-16")
    elif raw.startswith(b"\xfe\xff"):
        text = raw.decode("utf-16-be")
    elif len(raw) >= 2 and raw[1:2] == b"\x00":
        text = raw.decode("utf-16-le")
    elif raw.startswith(b"\xef\xbb\xbf"):
        text = raw.decode("utf-8-sig")
    else:
        text = raw.decode("utf-8")

    values: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key:
            values[key] = value
    return values


def get_api_key() -> str:
    file_vars = parse_env_file(SCRIPT_DIR / ".env")
    api_key = (
        os.environ.get("SUPADATA_API_KEY")
        or os.environ.get("SUPADATA_KEY")
        or file_vars.get("SUPADATA_API_KEY")
        or file_vars.get("SUPADATA_KEY")
    )
    if not api_key:
        raise SystemExit(
            "Missing Supadata API key. Set SUPADATA_API_KEY in your environment or "
            "in a .env file next to this script (get one at https://dash.supadata.ai)."
        )
    return api_key


def api_get(path: str, params: dict, api_key: str) -> tuple[int, dict | list | str | None]:
    response = requests.get(
        f"{BASE_URL}{path}",
        params=params,
        headers={"x-api-key": api_key},
        timeout=REQUEST_TIMEOUT,
    )
    try:
        payload = response.json()
    except ValueError:
        payload = response.text
    return response.status_code, payload


def get_latest_video_ids(channel_url: str, api_key: str, limit: int = VIDEOS_PER_EXPERT) -> list[str]:
    status, data = api_get(
        "/youtube/channel/videos",
        {"id": channel_url, "limit": limit, "type": "all"},
        api_key,
    )
    if status != 200 or not isinstance(data, dict):
        message = data.get("message", data) if isinstance(data, dict) else data
        print(f"  Could not list channel videos ({status}): {message}")
        return []

    video_ids: list[str] = []
    for key in ("videoIds", "shortIds", "liveIds"):
        for video_id in data.get(key, []):
            if video_id and video_id not in video_ids:
                video_ids.append(video_id)
            if len(video_ids) >= limit:
                return video_ids[:limit]
    return video_ids[:limit]


def get_video_metadata(video_id: str, api_key: str) -> dict | None:
    status, data = api_get("/youtube/video", {"id": video_id}, api_key)
    if status == 200 and isinstance(data, dict):
        return data
    return None


def extract_transcript_text(content: str | list | None) -> str:
    if not content:
        return ""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for chunk in content:
            if isinstance(chunk, dict):
                text = chunk.get("text", "")
                if text:
                    parts.append(text.strip())
            elif isinstance(chunk, str):
                parts.append(chunk.strip())
        return "\n\n".join(part for part in parts if part)
    return str(content).strip()


def fetch_transcript(video_url: str, api_key: str) -> tuple[str | None, str | None]:
    status, data = api_get(
        "/youtube/transcript",
        {"url": video_url, "lang": "en", "text": "true"},
        api_key,
    )

    if status in (206, 404):
        error = data.get("error", "transcript-unavailable") if isinstance(data, dict) else "unknown"
        return None, error

    if status != 200 or not isinstance(data, dict):
        message = data.get("message", data) if isinstance(data, dict) else data
        return None, f"HTTP {status}: {message}"

    transcript = extract_transcript_text(data.get("content"))
    if not transcript:
        return None, "empty-transcript"
    return transcript, None


def slugify(text: str, max_length: int = 80) -> str:
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_-]+", "-", slug).strip("-")
    return slug[:max_length] or "video"


def save_transcript(
    expert_name: str,
    video_id: str,
    title: str,
    video_url: str,
    transcript: str,
) -> Path:
    expert_dir = OUTPUT_DIR / expert_name
    expert_dir.mkdir(parents=True, exist_ok=True)

    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    filename = f"{slugify(title)}-{video_id}.md"
    output_path = expert_dir / filename

    content = (
        f"# {title}\n\n"
        f"**Video URL:** {video_url}\n\n"
        f"**Date fetched:** {fetched_at}\n\n"
        f"## Transcript\n\n"
        f"{transcript}\n"
    )
    output_path.write_text(content, encoding="utf-8")
    return output_path


def process_expert(expert_name: str, channel_url: str, api_key: str) -> tuple[int, int]:
    print(f"\n[{expert_name}] {channel_url}")
    video_ids = get_latest_video_ids(channel_url, api_key)
    if not video_ids:
        print("  No videos found.")
        return 0, 0

    saved = 0
    skipped = 0

    for index, video_id in enumerate(video_ids, start=1):
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"  [{index}/{len(video_ids)}] {video_url}")

        metadata = get_video_metadata(video_id, api_key)
        title = metadata.get("title", f"YouTube Video {video_id}") if metadata else f"YouTube Video {video_id}"

        transcript, error = fetch_transcript(video_url, api_key)
        if error:
            print(f"    Skipped ({error})")
            skipped += 1
            continue

        output_path = save_transcript(expert_name, video_id, title, video_url, transcript)
        print(f"    Saved: {output_path.relative_to(SCRIPT_DIR)}")
        saved += 1

    return saved, skipped


def main() -> None:
    api_key = get_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_saved = 0
    total_skipped = 0

    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Fetching up to {VIDEOS_PER_EXPERT} recent videos per expert...")

    for expert_name, channel_url in EXPERTS.items():
        saved, skipped = process_expert(expert_name, channel_url, api_key)
        total_saved += saved
        total_skipped += skipped

    print(
        f"\nDone. Saved {total_saved} transcript(s), skipped {total_skipped} video(s) "
        f"across {len(EXPERTS)} expert(s)."
    )


if __name__ == "__main__":
    main()
