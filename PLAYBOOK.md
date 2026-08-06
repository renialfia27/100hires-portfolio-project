# AI-Powered SEO Content Production Playbook / SOP

**Author:** Reni Alfia
**Based on:** `/research/sources.md`, `/research/linkedin-posts/`, `/research/youtube-transcripts/`
**Topic:** AI-Powered SEO Content Production (B2B SaaS)

---

## Why This Playbook Is Structured This Way

After reading through all 10 experts' recent material, one pattern stood out: almost nobody disagrees that AI should be used somewhere in the content pipeline. The real disagreement is about *where*. Some experts want AI doing research and structuring while humans write (Mike King, Lily Ray). Others are comfortable with AI drafting entire pages as long as a human edits (Matt Diggity, Nathan Gotch). One expert has publicly tested letting AI write an entire site with no human pass at all (Matt Diggity's "100% AI content" experiment), and another has publicly documented client sites getting hit with manual actions for doing exactly that (Lily Ray).

So this playbook is organized as a **production pipeline with checkpoints**, not a single "prompt and publish" workflow. The sources themselves show that skipping checkpoints is where things go wrong.

Two other patterns shaped how I weighted the material. First, I leaned more heavily on experts whose claims are backed by track record or independent data rather than opinion alone: Kevin Indig's frameworks carry more weight here because they come from someone who actually ran SEO in-house at Shopify, G2, and Atlassian, not just commentary from the sidelines; Glen Allsopp's posts carry more weight because they're backed by studies of thousands of sites, not a single anecdote. Second, a few of the "AI SEO" voices in this set (Will Scott and Koray Tugberk Gubur, specifically) are, underneath the new terminology, really re-asserting classic technical and architectural SEO discipline (crawl access, site structure, semantic hierarchy) under an AI framing. I don't read that as a weakness. If anything, it's a signal that the fundamentals didn't change as much as the AI-search hype suggests, which is part of why Part 1 of this playbook leads with foundations instead of jumping straight to new AI tactics.

---

## Part 1: Foundations (Do This Before Producing Any Content)

**1.1. Verify AI crawlers can actually reach your site before producing anything.**
Will Scott documented a client whose infrastructure returned 429 errors to AI crawler user-agents at the hosting/platform level. That's invisible to standard SEO audits, and invisible to Claude and Meta AI specifically, while Google AI Mode could still see the site. Content quality was never the problem; access was.
*(Source: Will Scott, "AI Crawl Access Trumps Content Quality," LinkedIn, ~Feb 2026: https://www.linkedin.com/posts/williamscott_your-seo-tools-can-say-everything-is-fine-activity-7459614959518380034-S0yU)*

**1.2. Run every piece of planned content through a readiness check before drafting, not after: is it Accessible, Useful, Extractable, Recognizable, Consistent, Corroborated, Credible, Differentiated, Fresh, and Transactable?**
This is Aleyda Solis's 10-characteristic framework for AI search readiness. Her point is that teams jump to writing before confirming the content *type* is even a good candidate for AI visibility.
*(Source: Aleyda Solis, "The New Rules of AI Visibility," LinkedIn/Moz, ~May 2026: https://www.linkedin.com/posts/aleyda_my-moz-guide-based-on-my-recent-webinar-activity-7463253507266052097-FXwm)*

**1.3. Treat AI search as an evaluation layer on existing brand clarity, not a new channel to "do SEO for."**
Will Scott reframes the central question from "can we rank?" to "can an AI system understand what we do, who we help, and why we should be trusted?" That shift moves the fix from "write more content" to "fix entity clarity, service specificity, and proof layers first."
*(Source: Will Scott, "AI Search Is an Evaluation Layer, Not a New Channel," LinkedIn, ~May 2026: https://www.linkedin.com/posts/williamscott_the-most-common-ai-search-mistake-i-see-is-activity-7465847068893544448-yWQs)*

**1.4. Set the quality bar explicitly before scaling: content must contain something AI alone cannot produce (real testing, an opinion, an original data point) or it doesn't get published.**
Lily Ray's argument is specific: Google's Quality Rater Guidelines reward *effort*, and content produced in a short AI session is structurally recognizable as low-effort even if it reads fine. She frames this as the line between content that ranks and content that gets cited.
*(Source: Lily Ray, "Non-Commodity Content vs. AI Automation," LinkedIn, ~May 2026: https://www.linkedin.com/posts/lily-ray-44755615_google-recently-reminded-everyone-that-non-commodity-activity-7455667858283368448-zkBC)*

---

## Part 2: Research & Topic Planning

**2.1. Every content brief must define four layers before drafting starts: Query Definition, Query Aspect, Query Theme, and Query Phrasification, not just a target keyword.**
Koray Tugberk Gubur's framework is the most detailed brief structure in the research set. His point: a keyword tells you what someone typed, not what they mean, what related questions they have, or how they'd phrase follow-ups. AI Overviews are built by hybridizing all of that.
*(Source: Koray Tugberk Gubur, "Query Semantics: How Google Interprets Intent for AI Overviews," LinkedIn, ~May 2025: https://www.linkedin.com/posts/koray-tugberk-gubur_query-semantics-seo-case-study-convince-activity-7325119159787245568-CLiK)*

**2.2. Apply "Query Deserves Page" discipline: not every query gets a dedicated URL. Some deserve a section, some a single sentence.**
This is a guardrail against exactly the kind of AI-content sprawl other experts (Gotch, Diggity) encourage. Koray's own case study only publishes what "the ecosystem genuinely deserves," not a URL for every keyword combination.
*(Source: Koray Tugberk Gubur, "Travel SEO Case Study: Query Deserves Page," LinkedIn, ~Jan 2026: https://www.linkedin.com/posts/koray-tugberk-gubur_1988-click-growth-in-28-days-won-bcau-activity-7417334824945766400-LUI3)*

**2.3. Before writing, map the sub-query cluster an AI system would generate around your target query (query fan-out), and cover the cluster with content, not one page per keyword.**
Mike King's argument, backed by his patent research into AI Mode: a single AI answer is often assembled from multiple synthetic sub-queries, so content that only answers the primary query is competing at a disadvantage against content that answers the fan-out.
*(Source: Mike King, "AI Mode Patents: Why It's Not 'Just SEO,'" LinkedIn, ~June 2025: https://www.linkedin.com/posts/michaelkingphilly_how-ai-mode-and-ai-overviews-work-based-on-activity-7335330568374571008-ik6d)*

**2.4. Build a genuine "topic map" of at least ~100 unique subtopics around one seed topic before producing, pulling from Search Console query data and AI-assisted clustering.**
Nathan Gotch's "topic domination" system starts here. The point isn't the volume itself; it's that most teams stop after 10–15 obvious topics and leave the long tail (and the AI fan-out territory) completely uncovered.
*(Source: Nathan Gotch, "7-Step SEO Campaign Checklist (for 2026)," YouTube, June 11, 2026: https://www.youtube.com/watch?v=H_l6nQjrc0Y)*

---

## Part 3: The Production Workflow

**3.1. Build a structured "knowledge base" of brand facts, FAQs, offers, and voice *before* generating any AI drafts, and require every draft to pull from it.**
Both Nathan Gotch and Mike King converge on this independently. Gotch's version: at least 10 structured artifacts uploaded to a project/Advisor tool so every draft is grounded in real brand facts instead of the model's general knowledge. Mike King's framing is broader: genAI's real value in SEO is analysis and workflow automation, not being used as a replacement copywriter with no grounding.
*(Source: Nathan Gotch, "7-Step SEO Campaign Checklist (for 2026)," YouTube, June 11, 2026: https://www.youtube.com/watch?v=H_l6nQjrc0Y; Mike King, "SEO in 2025: Agents Over AI Content Writing," LinkedIn, ~Jan 2025: https://www.linkedin.com/posts/michaelkingphilly_people-have-asked-me-about-seo-in-2025-activity-7273137999448600576-OEeT)*

**3.2. Find a genuine differentiation angle before drafting ("what makes this page 10% better than the top 5 competitors"), not just better formatting.**
Nathan Gotch calls this the "purple cow" step. Competitor analysis isn't just for keyword gaps; it's to find the specific angle (more original data, better UX, a missing sub-topic) that AI systems and humans both have a reason to prefer.
*(Source: Nathan Gotch, "7-Step SEO Campaign Checklist (for 2026)," YouTube, June 11, 2026: https://www.youtube.com/watch?v=H_l6nQjrc0Y)*

**3.3. Structure every draft against Kevin Indig's 11 AEO levers, grouped in three stages: Retrieved (fast load, clean metadata), Cited (fact density, FAQ coverage, freshness under 3 months, top-10 organic position), Trusted (author credentials, third-party/UGC validation).**
This is the most complete production checklist across all 10 sources. Use it as the actual QA rubric before a piece is marked "done," with a 90-day refresh cycle for anything AI-critical.
*(Source: Kevin Indig, "11 Levers for AEO: Retrieved → Cited → Trusted," LinkedIn, ~Feb–Mar 2026: https://www.linkedin.com/posts/kevinindig_same-tactics-new-game-if-you-think-ai-activity-7414334371656245248-O-sB)*

**3.4. Tag every piece of content with which layer(s) it's optimized for: SEO (ranking), AEO (structured answers/schema), or GEO (citation-readiness for generative engines). Each layer needs different structural elements.**
Matt Diggity's three-layer framework is useful specifically because it forces a decision at brief stage instead of trying to make one article do all three jobs by accident.
*(Source: Matt Diggity, "AI System for Hundreds of SEO Tasks," LinkedIn, ~Nov 2025: https://www.linkedin.com/posts/mattdiggityseo_i-built-an-ai-system-that-churns-out-hundreds-activity-7391675069242015744-8Si_)*

**3.5. Do not rely on "AI humanizer" tools to make AI drafts pass as human-written. Route every AI draft through a skilled human editor instead.**
Nathan Gotch tested multiple humanizer tools and found they add fluff and weaken clarity rather than adding genuine expertise; he calls the humanizer-on-AI-content workflow "AI inception." (See disagreement #2 below: Ruben Hassid takes a more optimistic view of prompting AI to sound natural directly.)
*(Source: Nathan Gotch, "Using AI to Humanize AI Content: It Doesn't Work," LinkedIn, ~March 2025: https://www.linkedin.com/posts/nathangotch_using-ai-to-humanize-ai-content-for-seo-activity-7304865684289699840-q7E2)*

---

## Part 4: Distribution & Off-Site Authority

**4.1. Every "topic," not just the website page, should also get a YouTube asset and a LinkedIn/social asset, because off-site UGC (Reddit, YouTube, social) is heavily cited by LLMs alongside indexed pages.**
Lily Ray's research shows off-site signals get cited by LLMs at least as often as owned, indexed content, meaning a single blog post without any off-site presence is an incomplete production unit, not a finished one.
*(Source: Lily Ray, "How SEO Is Evolving in 2025 (AI, Reddit & Ranking)," LinkedIn, ~July 2025: https://www.linkedin.com/posts/lily-ray-44755615_how-seo-is-evolving-in-2025-lily-ray-talks-activity-7317662260846354432-ZAON)*

**4.2. On YouTube specifically, publish a dedicated "conversion asset" first, then build every other video in the topic cluster to funnel back to it. Don't publish videos in isolation.**
Nathan Gotch's YouTube funnel model treats the channel as a five-stage awareness funnel rather than a library of disconnected how-to videos, which is what most teams default to.
*(Source: Nathan Gotch, "7-Step SEO Campaign Checklist (for 2026)," YouTube, June 11, 2026: https://www.youtube.com/watch?v=H_l6nQjrc0Y)*

**4.3. Actively extract which sources AI platforms already cite for your target queries, and prioritize outreach/mentions on those specific sources over generic backlink building.**
Nathan Gotch's citation-extraction workflow (query the AI platforms, pull the citations, categorize by type, then do outreach on the gaps) is the most concrete version of this across the research set. Matt Diggity's "citations are the new backlinks" framing supports the same shift in priority.
*(Source: Nathan Gotch, "7-Step SEO Campaign Checklist (for 2026)," YouTube, June 11, 2026: https://www.youtube.com/watch?v=H_l6nQjrc0Y; Matt Diggity, "2026 SEO Strategy: Citations Are the New Backlinks," LinkedIn, ~Jan 2026: https://www.linkedin.com/posts/mattdiggityseo_heres-my-2026-seo-strategy-stop-chasing-activity-7404443723511623681--Dk9)*

---

## Part 5: Measurement

**5.1. Track AI referral traffic and citation rate as a *separate* KPI from rankings and clicks. Don't fold it into a general "organic" bucket.**
Aleyda Solis's post on separate metrics is the clearest statement of this: ranking metrics and citation/recommendation metrics measure different things and require different content formats, so mixing them into one dashboard hides what's actually working.
*(Source: Aleyda Solis, "AI Search Demystified," LinkedIn/Microsoft Advertising, ~March 2026: https://www.linkedin.com/posts/aleyda_ai-search-demystified-activity-7430550976257888256-l0VA)*

**5.2. Before treating any AI-visibility "win" as validated, check it against real usage-share data. AI referral traffic is still a small fraction of total organic traffic for most sites.**
Lily Ray cited Similarweb and Glen Gabe's client data showing LLM referral traffic sits around 1–2% of total organic traffic for most sites, even amid heavy AI-search hype. This matters for prioritization: don't deprioritize traditional SEO to chase AI citations that currently drive a small fraction of traffic.
*(Source: Lily Ray, "GEO, AEO, LLMO: Separating Fact from Fiction," MozCon 2025 talk, YouTube: https://www.youtube.com/watch?v=2nJkT8zOzcM)*

**5.3. Track AI visibility tooling changes as part of routine competitive monitoring, the same way you'd track a competitor's new backlinks.**
Glen Allsopp documents Ahrefs shipping 106 product updates in 5 months around AI visibility tracking alone. The tooling category is moving fast enough that a quarterly check-in isn't enough.
*(Source: Glen Allsopp, "Ahrefs AI Visibility Product Updates," LinkedIn, ~Jan 2026: https://www.linkedin.com/posts/glen-allsopp-63084025_ahrefs-ships-december-2025-product-updates-activity-7420103923891511298-Maij)*

---

## Where Experts Disagree

### Disagreement 1: Should AI generate entire pages/sites at scale with minimal human involvement?

- **Matt Diggity recommends:** Yes, if done systematically. He publicly built and ran a website on 100% AI-generated content and reported real traffic and revenue results from a site he personally owns. *(Source: Matt Diggity, "I Built a Website with 100% AI Content. Here's What Happened," LinkedIn, Feb 2023: https://www.linkedin.com/posts/mattdiggityseo_i-built-a-website-with-100-ai-content-activity-7029093777013182464-Ir-G. Note on date: this post is from February 2023, well outside this research's 3–6 month collection window. I'm keeping it in the disagreement because it's still the clearest documented case of this approach in the collected material, but I'm flagging it as dated evidence, not current practice. See Weaknesses.)*
- **Lily Ray recommends:** No. She documents real client cases of Google manual actions triggered by scaled AI content abuse, and argues Google's Quality Rater Guidelines specifically reward the kind of hands-on effort a fully-automated pipeline can't produce.
- **Which side I take:** Lily Ray's, for this playbook's context, and her position is also the more current one of the two. Matt Diggity's experiment is on a site he owns and controls risk tolerance for personally; a B2B SaaS brand with a reputation to protect can't treat organic search as a controlled experiment. I've built the human-editor checkpoint (3.5) and the non-commodity quality bar (1.4) into this playbook as non-negotiable, not optional. Honestly, finding out this specific claim was three years old also made me trust Diggity's other numbers in this research a bit less by association, not because they're necessarily wrong, but because if the most central claim wasn't checked for recency, I can't be fully sure the rest were either.

### Disagreement 2: Can you make AI-written content read as human through better prompting, or is that a dead end?

- **Ruben Hassid recommends:** Yes. He published an 8-step prompt framework (plain language, no clichés, direct tone) specifically designed to make ChatGPT output read naturally. *(Source: Ruben Hassid, "The One Prompt to Make ChatGPT Write Naturally," LinkedIn, ~May 2025: https://www.linkedin.com/posts/ruben-hassid_the-one-prompt-to-make-chatgpt-write-naturally-activity-7339879340999888896-zxiE)*
- **Nathan Gotch recommends:** No. He tested multiple "AI humanizer" approaches and concluded they add fluff and weaken clarity rather than closing the expertise gap, calling it "AI inception." *(Source: Nathan Gotch, "Using AI to Humanize AI Content: It Doesn't Work," LinkedIn, ~March 2025: https://www.linkedin.com/posts/nathangotch_using-ai-to-humanize-ai-content-for-seo-activity-7304865684289699840-q7E2)*
- **Which side I take:** A middle position, closer to Gotch's. Better prompting (Hassid's framework) is a reasonable *first pass* to strip obvious AI clichés, but it doesn't substitute for the human edit pass in 3.5; prompting fixes tone, not the underlying lack of tested, first-hand expertise that Lily Ray's quality bar requires. I also give Gotch's conclusion a bit more weight than a random skeptic's take would get, for a specific reason: he sells an AI SEO tool for a living, so he has every commercial incentive to tell people AI shortcuts work. Publicly saying humanizer tools *don't* work, against his own product's interest, is the kind of admission that's more credible precisely because it costs him something to say it.

### Disagreement 3: Should content production default to building a dedicated page for every distinct keyword/intent gap?

- **Nathan Gotch recommends:** Yes, generally. His "splintering" tactic explicitly builds a new dedicated page whenever an existing page ranks for a keyword beyond position 50 with a poor intent match, aiming for a large topic map (100+ pages) per seed topic. *(Source: Nathan Gotch, "7-Step SEO Campaign Checklist (for 2026)," YouTube, June 11, 2026: https://www.youtube.com/watch?v=H_l6nQjrc0Y)*
- **Koray Tugberk Gubur recommends:** No. His "Query Deserves Page" principle explicitly rejects auto-generating a page for every keyword; some queries deserve a section or a sentence, not a URL. *(Source: Koray Tugberk Gubur, "Travel SEO Case Study: Query Deserves Page," LinkedIn, ~Jan 2026: https://www.linkedin.com/posts/koray-tugberk-gubur_1988-click-growth-in-28-days-won-bcau-activity-7417334824945766400-LUI3)*
- **Which side I take:** Koray's, as the default rule, but with a concrete filter for deciding which of Gotch's splinter-worthy keywords actually get built first, since most teams (especially a one-person content function) can't build all of them anyway. Rank candidates by transactional intent first (how close the keyword is to a buying decision), then by search volume, then by competition difficulty, but calibrate that last filter against the site's own authority rather than treating difficulty as a fixed number: a site with strong existing authority can go after a competitive keyword and still realistically win, but a newer or smaller site should stick to low-to-medium difficulty keywords first and build authority before attempting the harder ones. Only keywords that clear all three filters get a dedicated splintered page; the rest either fold into an existing page's section, per Koray's Query Deserves Page principle, or wait for a later cycle once the site has more authority to spend.

---

## What I Rejected and Why

**1. Ruben Hassid's AI avatar / voice-cloning content scaling model (EasyGen).**
Ruben documented real results: 770K+ LinkedIn followers, 60M+ video views using AI avatars and voice cloning to scale personal-brand content. *(Source: figures from `/research/sources.md`, Expert 6 bio, and `/research/linkedin-posts/ruben-hassid.md`. I could not find a direct, dated link for the specific EasyGen/avatar case study in the collected material, only the aggregate follower/view figures; that gap is itself part of why I'm cautious about this source, see Weaknesses.)* I'm rejecting this as a production method for a B2B SaaS content playbook specifically because it's optimized for personal-brand growth on a single platform (LinkedIn), not for owned-site SEO/citation-readiness, and because faceless AI-avatar content works against the "real, tested, first-hand expertise" quality bar that Lily Ray's research shows AI systems (and Google's raters) are increasingly checking for in B2B/informational content.

**2. Koray Tugberk Gubur's "48 custom AI agents" workflow as a starting-point recommendation.**
*(Source: `/research/sources.md`, Expert 4 bio: "48 AI Agents for Semantic SEO," free via ChatGPT Plus. No direct, dated post link was captured for this specific claim in the original research.)* The underlying principle (structured, repeatable AI workflows for semantic content production) is sound and shows up elsewhere in this playbook. But the specific implementation, 48 custom-built agents covering the full content pipeline, isn't documented publicly in enough technical detail in the collected material to be replicable, and assumes engineering resources most B2B SaaS marketing teams (including a junior marketer building this playbook) don't have. I kept the underlying idea (structured, brief-driven AI production, see 2.1 and 3.1) without the specific tooling requirement.

---

## My Original Idea

**AI-automated broken link discovery, split into a two-track decision: reclaim the link, or validate the content brief.**

None of the 10 sources proposed this exact mechanism. The closest pieces are Kevin Indig's "Trusted" stage (validating content through third-party/UGC signals, 3.3) and Nathan Gotch's citation-extraction workflow (4.3), but both of those track links and citations that already point at content that exists. This idea works one step earlier: finding links that used to point at *something*, and no longer do.

The idea: run an AI fetching workflow across external sites in your niche to find broken outbound links (dead pages, old resources, competitor pages that now 404) on topics relevant to your content strategy. For every broken link found, the decision splits two ways:

- **If you already have a genuinely equivalent, live page**, this is straightforward broken-link reclamation: reach out to the site owner, tell them their link is dead, and offer your page as the replacement. This is one of the fastest, cheapest backlinks available, because you're solving a real problem for them, not asking for a favor.
- **If you don't have an equivalent page yet, don't skip it.** Treat the broken link itself as a validated content brief: at least one external site once considered this exact topic worth linking to. That's a stronger signal than keyword search volume alone, because search volume only tells you people are searching for something; a broken link tells you someone already decided the topic was worth recommending to their own audience. Add it to the content backlog with a "pre-validated by broken link" flag, and prioritize it above topics that are only backed by keyword-volume data.

Why it could work: right now, this playbook (like all 10 sources) treats content production (Part 3) and off-site link acquisition (Part 4) as two separate workstreams that happen to feed the same site. This idea collapses them into a single discovery signal. Instead of writing content first and hoping it earns links later, or building links to content that already exists, broken link discovery tells you what to write and who is likely to link to it in the same step.

---

## Weaknesses of This Playbook

- **It's built entirely from public, self-reported claims.** Figures like "2,300% AI traffic growth," "975% more visibility," and "86% AI search visibility" come directly from the experts' own posts and videos. None of them are independently verified in this research, and several of the experts sell tools (Rankability, EasyGen) whose success stories double as product marketing. I specifically checked the "86% AI search visibility" figure for Rankability: it traces back to Nathan Gotch's own "About" page on his personal site, not a dated, sourced post. It's a first-party marketing claim with no independent verification available in this research.
- **The source material has real gaps in recency and relevance.** The YouTube collection for Mike King consists mostly of off-topic videos (see "Who I Would Not Recommend" below), so his section of this playbook leans more heavily on LinkedIn posts than intended. Several of Lily Ray's YouTube transcripts are from 2024–early 2025, older than the "last 3–6 months" window the research was supposed to target. I also spot-checked several source dates directly: Matt Diggity's "100% AI Content Website" post (anchor of Disagreement #1) turned out to be from February 2023, nearly three years outside the target window, despite being filed under "Recent content" in `/research/sources.md`. I kept it in this playbook because it's still the clearest documented example of that specific approach in the material collected, but it should have been caught during initial source vetting, and it's a reminder that "recent content" labels in my own research need spot-checking, not just trusting the collection date.
- **This playbook assumes access to paid tooling** (Ahrefs, Rankability-style platforms, AI visibility trackers like Profound/Otterly) that a small or early-stage B2B SaaS team may not have budget for. Several of the concrete workflows (2.4, 4.3, 5.1) get noticeably harder to execute manually at scale.
- **It's US/English-market and Google-centric.** All 10 experts and nearly all cited data (Similarweb, BrightEdge, GSC) reflect English-language, US-heavy search behavior. None of the sources address how this changes for non-English markets or non-Google-dominant regions.
- **AI search changes fast enough that parts of this will age quickly.** Several sources (Glen Allsopp, Kevin Indig) explicitly note tooling and platform behavior changing month to month. A playbook this specific has a shelf life measured in months, not years; it should be treated as a living document, re-checked against fresher sources at least quarterly.
- **The disagreements aren't fully resolved, only adjudicated by judgment call.** Section "Where Experts Disagree" reflects my read of which approach fits a B2B SaaS context better. A different team with a different risk tolerance (e.g., an affiliate site like Matt Diggity's own) could reasonably make different calls on all three.

---

## Who I Would NOT Recommend Following, and Why

**Matt Diggity, when it comes to trusting his specific numbers at face value.**
His engineering-style, single-variable experiments (the $491K case study: https://diggitymarketing.com/ai-seo-genius-case-study/, and the 2,300% AI traffic growth framework cited in Part 3) are genuinely useful and I cited them directly in this playbook. But he's also the one expert in this research where I caught a headline claim, the "100% AI Content Website" experiment anchoring Disagreement #1, filed as recent when it's actually from 2023. That's not disqualifying on its own, but it means I'd treat his content as a source of *ideas to test yourself*, not as verified data to cite downstream without checking the date first.

**Mike King, specifically his YouTube channel, not his written work.**
His written frameworks (Relevance Engineering, Qforia, the LinkedIn posts on query fan-out and AI Mode patents) are among the most technically substantive material in this whole research set, and I cited them directly in Parts 2 and 3. But when I actually pulled his recent YouTube uploads for this research, the videos returned were things like "Google Home Beatbox," a "Thanks Obama Challenge" post, and a comedic trailer for an internal show, none relevant to AI-powered SEO content production at all. If someone were researching this topic and went looking for Mike King's *video* content specifically expecting SEO teaching, they'd come away with a badly wrong impression of what he actually knows. I'd point people to his written work only, not his channel.

**Ruben Hassid, with a caveat.**
His prompting framework (Post 3, cited in 3.5's disagreement) is genuinely useful and I used it. But a large share of his recent content is built around his own follower-growth story and product (EasyGen), and the growth tactics he documents (AI avatar/voice cloning, scaling five LinkedIn accounts to 1.56M combined followers) are personal-brand and platform-growth tactics, not SEO content production tactics, even though they get filed under "AI content" broadly. Someone using him as a primary source for a B2B SaaS SEO playbook (rather than a secondary source for one specific prompting technique) would end up building a LinkedIn personal-brand strategy, not an SEO content system.

---

## Sources

Full detail on all 10 experts and selection criteria: [`/research/sources.md`](./research/sources.md)
LinkedIn post collections: [`/research/linkedin-posts/`](./research/linkedin-posts/)
YouTube transcript collections: [`/research/youtube-transcripts/`](./research/youtube-transcripts/)
