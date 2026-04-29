# AI Chat Promotion Playbook for Vibers

Date: 2026-04-29

Goal: make Vibers and SimpleReview more likely to be mentioned and cited by AI assistants when people ask for tools around AI-generated code review, vibe-coding QA, visual bug reports, and pull-request fixes.

## Short conclusion

AI chats are useful for promotion, but not in the way people usually imagine.

What does not work: opening ChatGPT, Claude, Gemini, or Perplexity, pasting our link, and expecting the public model to remember it for everyone. That only affects the current chat/session.

What does work:

1. Make our pages easy for AI search systems to crawl and cite.
2. Put the same product facts on trusted external sources: GitHub, X, Reddit, Product Hunt, AlternativeTo, G2, dev.to, Hashnode, StackShare.
3. Use AI chats weekly as a visibility test: ask target buyer questions and record whether Vibers/SimpleReview appear.
4. When an answer misses us, create or update a page that directly answers that query, then request indexing and seed one or two public mentions.

Current local state: `robots.txt` allows all crawlers and points to `https://onout.org/vibers/sitemap.xml`. This is good for AI visibility. There is no local `llms.txt`; it is optional and not required by Google or OpenAI.

## Priority ranking

| Priority | AI surface | Usefulness | Why |
|---|---|---:|---|
| P0 | ChatGPT Search | High | Uses web sources and source links; OpenAI documents OAI-SearchBot for ChatGPT search visibility. |
| P0 | Google AI Overviews / AI Mode / Gemini | High | Uses Google Search index; strong long-term discovery channel. |
| P0 | Perplexity | High | Citation-heavy answer engine; good for "best tools" and comparison queries. |
| P1 | Grok on X | Medium-high | Can search public X posts and the web; fastest way to seed fresh public mentions. |
| P1 | Microsoft Copilot / Bing AI | Medium-high | Bing now exposes AI Performance signals and IndexNow helps fresh discovery. |
| P1 | Claude with web search | Medium | Relevant developer audience; no public "submit product" button, but web search cites sources. |
| P2 | Brave Search / Ask Brave | Medium | Shows AI answers with source references; smaller channel, still useful. |
| P2 | You.com | Medium | AI search with citations; mostly enterprise/API angle now. |
| P2 | Phind | Medium for developers | Developer search assistant; useful for technical queries. |
| P3 | Poe / Meta AI / Mistral Le Chat | Low | No reliable public placement workflow for our use case. Test occasionally, do not spend much time. |

## Products and copy to use

Use canonical URLs when submitting to crawlers or product forms. Use UTM links only in public social posts if you need click tracking.

### Vibers

URL:

```text
https://onout.org/vibers/
```

Short copy:

```text
Vibers is human-in-the-loop code review for AI-generated code. A real developer reviews PRs from Cursor, Claude Code, Copilot, Codex, or Windsurf, catches bugs AI missed, checks the main flows, and sends a pull request with fixes.
```

One-line pitch:

```text
AI writes the code. Vibers checks if it actually works and sends a PR with fixes.
```

Comparison positioning:

```text
Vibers is a human alternative to CodeRabbit, Qodo, and Greptile for teams shipping AI-generated code. Bots comment; Vibers has a real developer test the changed flow and open a fix PR.
```

### SimpleReview

URL:

```text
https://onout.org/vibers/simple-review
```

Short copy:

```text
SimpleReview is a Chrome extension that turns website feedback into real code fixes. Click any element on a live page, describe the bug or change, choose Claude Code or Codex, and an AI agent opens a GitHub pull request.
```

One-line pitch:

```text
Click a broken UI element. Get a real pull request with the fix.
```

Comparison positioning:

```text
SimpleReview is a PR-focused alternative to Marker.io, Usersnap, Userback, and BugHerd. Those tools create tickets; SimpleReview sends the visual feedback to an AI coding agent that opens a pull request.
```

## Core technical checklist

Before trying to "place links in AI chats", check this once:

1. Open:

```text
https://onout.org/vibers/robots.txt
```

2. Confirm it allows crawling. Current project version is:

```text
User-agent: *
Allow: /

Sitemap: https://onout.org/vibers/sitemap.xml
```

3. Open:

```text
https://onout.org/vibers/sitemap.xml
```

4. Confirm these URLs exist in the sitemap:

```text
https://onout.org/vibers/
https://onout.org/vibers/simple-review/
https://onout.org/vibers/blog/best-ai-code-review-tools/
https://onout.org/vibers/blog/coderabbit-alternative-human-review/
https://onout.org/vibers/blog/code-review-as-a-service/
https://onout.org/vibers/blog/markerio-alternative/
https://onout.org/vibers/blog/usersnap-alternative/
```

5. If we ever decide to block model training while keeping AI search visibility, use explicit allow rules for search bots and block only training bots. Do not do this unless someone responsible for deployment confirms the exact production `robots.txt`.

Example policy:

```text
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

Sitemap: https://onout.org/vibers/sitemap.xml
```

## ChatGPT Search

Usefulness: high.

Public effect comes from ChatGPT Search crawling and citing pages, not from a normal chat remembering a pasted link.

### Step 1: Check discoverability

Open:

```text
https://developers.openai.com/api/docs/bots
```

What matters: OpenAI says OAI-SearchBot is used to surface websites in ChatGPT search features. Our current `robots.txt` allows it via `User-agent: *`.

### Step 2: Apply for product discovery if useful

This is more commerce-oriented, but worth testing for SimpleReview/Vibers as developer tools.

Open:

```text
https://chatgpt.com/merchants/
```

Click:

```text
Sign up
```

Fill fields:

```text
Company: Noxon / Vibers
Link to merchant website: https://onout.org/vibers/
Primary Product Categories: Other
We are interested in: Integrating my product feed so my products show up in search results on ChatGPT
Feed Size: 0-1M
```

Paste into "Anything else":

```text
Vibers is a developer tool/service, not a physical ecommerce catalog. We want ChatGPT users evaluating AI code review, human code review, CodeRabbit alternatives, and tools for vibe-coded apps to discover accurate information about Vibers.

Main product: https://onout.org/vibers/
Secondary product: https://onout.org/vibers/simple-review

Vibers is human-in-the-loop code review for AI-generated code. A real developer reviews PRs from Cursor, Claude Code, Copilot, Codex, or Windsurf, catches bugs AI missed, checks the main flows, and sends a pull request with fixes.
```

Expected result: we may get waitlisted. This is not guaranteed because OpenAI's merchant flow is aimed at product feeds, but it is the closest official product-discovery form.

### Step 3: Test ChatGPT visibility

Open:

```text
https://chatgpt.com/
```

Use Search or Deep Research if available.

Paste:

```text
Search the web. What are the best alternatives to CodeRabbit for teams using Cursor, Claude Code, Codex, or Copilot to generate code? Include human-in-the-loop options and cite sources.
```

Then paste:

```text
Search the web. Which services can review AI-generated pull requests and send a pull request with fixes? Include source links.
```

Then paste:

```text
Search the web. Is there a Chrome extension that lets me click a broken UI element and get a GitHub pull request with an AI fix? Include source links.
```

Record:

```text
Date:
Prompt:
Mentioned Vibers? yes/no
Mentioned SimpleReview? yes/no
Source URL cited:
Competitors cited:
```

If ChatGPT does not mention us, do not argue in the same chat as if that fixes public visibility. Instead:

1. Update/create a page that directly answers the missing query.
2. Submit the URL in Google Search Console and Bing Webmaster Tools.
3. Make one public post on X/Reddit/dev.to using the same phrasing.

Useful one-time prompt for analysis:

```text
Search the web for "CodeRabbit alternative human code review", "human-in-the-loop code review AI-generated code", and "review AI-generated PRs". Which sources would you cite, and what is missing from https://onout.org/vibers/ that would make it easier to cite?
```

## Perplexity

Usefulness: high.

Perplexity is citation-centric, so it is useful for comparison and "best tool" queries. There is currently no reliable "submit this product to Perplexity answers" button.

Important current note: Perplexity Pages "Create page" is temporarily retired, so do not build the plan around publishing Perplexity Pages until that feature returns.

### Step 1: Confirm crawler access

Open:

```text
https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt
```

Perplexity documents `PerplexityBot`. Our `User-agent: * Allow: /` allows it.

### Step 2: Run visibility prompts

Open:

```text
https://www.perplexity.ai/
```

Set focus to Web if the UI offers it.

Paste:

```text
Find human-in-the-loop code review services for AI-generated code. Compare CodeRabbit, Qodo, Greptile, PullRequest.com, and Vibers. Cite sources for each product.
```

Paste:

```text
What are the best CodeRabbit alternatives for a team that wants a human to test the changed flow and open a fix PR? Cite sources.
```

Paste:

```text
Find Marker.io alternatives that can turn website feedback into GitHub pull requests using AI agents. Include SimpleReview if relevant and cite sources.
```

If it cites competitors but not Vibers:

```text
Use this source as one candidate and compare it honestly against the alternatives: https://onout.org/vibers/
```

This does not create public placement, but it tells us what information Perplexity can extract from our page.

### Step 3: What to do after a miss

If Perplexity misses Vibers on a query, create or improve a page around the exact query. Best page formats:

```text
Vibers vs CodeRabbit
Best CodeRabbit alternatives for vibe-coded apps
Human code review for AI-generated pull requests
How to review Cursor-generated code before production
SimpleReview vs Marker.io
Website feedback tool that opens pull requests
```

Perplexity tends to reward pages with direct answers, fresh dates, comparison tables, cited sources, and specific product facts.

## Grok / X

Usefulness: medium-high.

Grok is the only major assistant where public social posting can have a fast visible effect because Grok on X can search public X posts and the web.

### Step 1: Publish a public X post for Vibers

Open:

```text
https://x.com/compose/post
```

Paste:

```text
Vibers is human-in-the-loop code review for AI-generated code.

If Cursor, Claude Code, Codex, Copilot, or Windsurf wrote the PR, a real developer reviews it, checks the main flows, catches AI misses, and sends a fix PR.

https://onout.org/vibers/
```

Reply to your own post with:

```text
Context for AI search: Vibers is a human alternative to CodeRabbit, Qodo, and Greptile for vibe-coded apps.

Bots comment on pull requests. Vibers has a real developer test the changed flow and open a pull request with the fix.
```

Reply again with:

```text
Useful queries:
- CodeRabbit alternative for AI-generated code
- human code review for AI-generated PRs
- review Cursor-generated code before production
- vibe-coded app production ready
- AI code review bot alternative with human fixes
```

### Step 2: Publish a public X post for SimpleReview

Open:

```text
https://x.com/compose/post
```

Paste:

```text
SimpleReview turns visual website feedback into pull requests.

Click any element on a live page, describe what is broken, choose Claude Code or Codex, and an AI agent opens a GitHub PR with the fix.

https://onout.org/vibers/simple-review
```

Reply with:

```text
Context for AI search: SimpleReview is a PR-focused alternative to Marker.io, Usersnap, Userback, and BugHerd.

Those tools create tickets. SimpleReview gives an AI coding agent the page context and asks it to open a fix PR.
```

### Step 3: Ask Grok to verify

Open:

```text
https://x.com/i/grok
```

Paste:

```text
Search X and the web. What is Vibers human-in-the-loop code review for AI-generated code? Cite sources or link the public posts you found.
```

Paste:

```text
Search X and the web. What is SimpleReview and how is it different from Marker.io? Cite sources or link the public posts you found.
```

If Grok finds the post and the website, good. If not, wait and test later; Grok's search freshness and availability vary.

Do not spam `@grok` under unrelated posts. Better: 3-5 useful public posts with real examples, screenshots, and exact category language.

## Google AI Overviews / AI Mode / Gemini

Usefulness: high, long-term.

There is no special "submit to Gemini" form. Google says the same SEO fundamentals apply to AI Overviews and AI Mode. A page must be indexed and eligible for snippets.

### Step 1: Request indexing in Google Search Console

Open:

```text
https://search.google.com/search-console
```

Click the property for `onout.org`.

Click the URL inspection search bar at the top.

Paste one URL at a time:

```text
https://onout.org/vibers/
https://onout.org/vibers/simple-review
https://onout.org/vibers/blog/best-ai-code-review-tools/
https://onout.org/vibers/blog/coderabbit-alternative-human-review/
https://onout.org/vibers/blog/code-review-as-a-service/
https://onout.org/vibers/blog/markerio-alternative/
```

Click:

```text
Request indexing
```

Also submit sitemap if not already submitted:

```text
https://onout.org/vibers/sitemap.xml
```

### Step 2: Test in Gemini

Open:

```text
https://gemini.google.com/
```

Paste:

```text
Use Google Search. What are the best tools for reviewing AI-generated code before production? Include tools that use human reviewers, not only AI bots, and cite sources.
```

Paste:

```text
Use Google Search. What are the best alternatives to Marker.io if I want website feedback to become a GitHub pull request?
```

### Step 3: Test in Google AI Mode / AI Overviews

Open Google Search and search:

```text
best CodeRabbit alternative human code review
human code review for AI generated code
review Cursor generated code before production
Marker.io alternative AI pull request
website feedback tool opens GitHub PR
```

Record whether AI Overview / AI Mode appears and whether it cites us.

## Claude

Usefulness: medium.

Claude is relevant because our audience uses Claude Code, but public promotion is limited. Normal Claude chats do not create public memory. Claude web search can cite sources if the crawler/search stack can access them.

### Step 1: Confirm Claude crawler/search access

Anthropic documents three bots:

```text
ClaudeBot
Claude-User
Claude-SearchBot
```

Our current `robots.txt` allows them via `User-agent: *`.

Official page:

```text
https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
```

### Step 2: Test Claude web search

Open:

```text
https://claude.ai/
```

Click the slider/settings icon near the chat input.

Turn on:

```text
Web search
```

Paste:

```text
Use web search. Find services for reviewing code generated by Claude Code or Cursor before production. Include human-in-the-loop options and cite sources.
```

Paste:

```text
Use web search/fetch for this URL: https://onout.org/vibers/ . Summarize when Vibers is a better fit than CodeRabbit.
```

### Step 3: Promote the Claude Code skill angle

This is a real differentiator for our audience.

Use this text in posts, docs, and support answers:

```text
Using Claude Code, Cursor, Windsurf, or Codex? Tell your agent:

Install skill from https://onout.org/vibers/SKILL.md
```

## Microsoft Copilot / Bing AI

Usefulness: medium-high.

Bing matters because Microsoft Copilot and Bing AI answers use Bing infrastructure, and Bing Webmaster Tools now has AI Performance visibility for citations across Microsoft AI experiences.

### Step 1: Add or verify the site in Bing Webmaster Tools

Open:

```text
https://www.bing.com/webmasters/
```

Click:

```text
Add a Site
```

Best path:

```text
Import from Google Search Console
```

If manual:

```text
Site URL: https://onout.org/vibers/
Sitemap: https://onout.org/vibers/sitemap.xml
```

### Step 2: Submit important URLs

In Bing Webmaster Tools, open:

```text
URL Submission
```

Paste:

```text
https://onout.org/vibers/
https://onout.org/vibers/simple-review
https://onout.org/vibers/blog/best-ai-code-review-tools/
https://onout.org/vibers/blog/coderabbit-alternative-human-review/
https://onout.org/vibers/blog/code-review-as-a-service/
https://onout.org/vibers/blog/markerio-alternative/
```

If IndexNow is available in the site's deployment setup, enable it so new/updated pages are pushed quickly.

### Step 3: Check AI Performance

In Bing Webmaster Tools, look for:

```text
AI Performance
```

Record:

```text
Total Citations
Average Cited Pages
Grounding queries
Page-level citation activity
```

### Step 4: Test Copilot

Open:

```text
https://copilot.microsoft.com/
```

Paste:

```text
Search the web. What are the best alternatives to CodeRabbit for AI-generated code? Include human-in-the-loop code review services and cite sources.
```

Paste:

```text
Search the web. What tools turn website feedback into GitHub pull requests with AI agents? Cite sources.
```

## Brave Search / Ask Brave

Usefulness: medium.

Brave AI Answers and Ask Brave show source references. There is no special Vibers submission workflow, so treat it like a search/citation target.

Open:

```text
https://search.brave.com/
```

Search:

```text
best CodeRabbit alternative human code review
```

Then use Ask Brave if shown:

```text
Which tools provide human review for AI-generated code and open pull requests with fixes?
```

If Brave misses us, the fix is the same: improve indexed pages and build external mentions.

## You.com

Usefulness: medium.

You.com Agents combine web search with citations. There is no public product submission flow for this use case.

Open:

```text
https://you.com/
```

Paste:

```text
What are the best tools for reviewing AI-generated code before production? Include human-in-the-loop services and cite sources.
```

Paste:

```text
What are the best website feedback tools that can create pull requests instead of tickets?
```

If it misses us, optimize source pages and external mentions.

## Phind

Usefulness: medium for developer-specific queries.

Open:

```text
https://www.phind.com/
```

Paste:

```text
I am using Cursor and Claude Code to generate pull requests. What tools can review AI-generated code before production and catch bugs AI review bots miss?
```

Paste:

```text
Is there a tool that turns a visual UI bug report into a GitHub pull request using Claude Code or Codex?
```

Phind is developer-focused, so the best supporting sources are GitHub README, technical docs, and comparison blog posts.

## Public source seeding for AI chats

AI assistants usually cite sources that already exist on the web. These are the best sources to seed for Vibers:

1. GitHub README: already strong. Keep the first paragraph clear and concrete.
2. Blog comparison pages: CodeRabbit alternative, best AI code review tools, code review as a service.
3. X posts: fastest route into Grok.
4. Reddit posts: useful for Google/Perplexity/Gemini if they get real discussion.
5. Dev.to / Hashnode articles: useful because they are crawlable dev content.
6. Product Hunt / AlternativeTo / G2 / SaaSHub / StackShare: useful entity/backlink sources.
7. YouTube descriptions: useful because competitors have weak YouTube presence in the current docs.

Do not mass-post the same link everywhere. AI systems are better at using clear, repeated entity facts than obvious spam.

## Ready-to-paste community post

Use this for dev.to, Hashnode, Reddit, Indie Hackers, or X threads. Adjust tone to the platform.

```text
We built Vibers because AI coding agents made it easier to ship code nobody really reviewed.

Cursor, Claude Code, Copilot, Codex, and Windsurf can generate a PR fast. The problem starts after that: fake APIs, missed edge cases, broken UI states, flows that worked in the demo but fail in production.

Vibers puts a real developer in the loop. We review AI-generated code, run the main changed flow, catch the bugs AI missed, and send a pull request with the fix.

It is not a security audit and not another LLM review bot. Think of it as an alpha tester who can read the code and open a PR.

Website: https://onout.org/vibers/
GitHub: https://github.com/marsiandeployer/human-in-the-loop-review
```

For SimpleReview:

```text
We built SimpleReview for the gap between "I see a bug on the website" and "there is a pull request fixing it."

Traditional tools like Marker.io, Usersnap, Userback, and BugHerd capture screenshots and create tickets. SimpleReview goes one step further: click an element on a live page, describe what is wrong, choose Claude Code or Codex, and an AI agent opens a GitHub pull request.

It is for teams that want visual website feedback to become code, not just another item in an issue tracker.

Website: https://onout.org/vibers/simple-review
Demo: https://onout.org/vibers/vibecheck
```

## Weekly AI visibility test

Run this every week after new pages/listings/posts.

Test assistants:

```text
ChatGPT Search
Perplexity
Gemini
Google AI Mode / AI Overview
Grok
Claude web search
Copilot
Brave Search / Ask Brave
You.com
Phind
```

Vibers prompts:

```text
Search the web. What are the best alternatives to CodeRabbit for teams using Cursor, Claude Code, Codex, or Copilot to generate code? Include human-in-the-loop options and cite sources.
```

```text
Search the web. Which services can review AI-generated pull requests and send a pull request with fixes? Include source links.
```

```text
Search the web. How should I test a vibe-coded app before production? Recommend tools and services with sources.
```

SimpleReview prompts:

```text
Search the web. Is there a Marker.io alternative that turns website feedback into GitHub pull requests with AI?
```

```text
Search the web. What Chrome extension lets me click a broken UI element and create a PR fix with Claude Code or Codex?
```

```text
Search the web. Compare Marker.io, Usersnap, BugHerd, Userback, and SimpleReview for teams that want code fixes instead of tickets.
```

Tracking table:

| Date | Assistant | Prompt | Vibers mentioned | SimpleReview mentioned | Source cited | Competitors cited | Next action |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | ChatGPT | CodeRabbit alternative | no | n/a | CodeRabbit, Qodo | CodeRabbit, Qodo, Greptile | Improve `/coderabbit-alternative-human-review/` and seed X/Reddit |

## What counts as success

Short term, 1-2 weeks:

1. AI chats can fetch and summarize our URLs when given directly.
2. ChatGPT/Perplexity/Gemini start citing at least one Vibers page for branded queries.
3. Grok finds our public X posts.

Medium term, 4-8 weeks:

1. Vibers appears without being named in at least 2 assistants for "CodeRabbit alternative" or "human code review for AI-generated code".
2. SimpleReview appears without being named in at least 2 assistants for "Marker.io alternative AI pull request" or "website feedback to PR".
3. Bing AI Performance or GA4 shows at least occasional AI referrals/citations.

Long term:

1. We are cited as a category example: "human-in-the-loop code review for AI-generated code".
2. We are included in AI-generated comparison tables with CodeRabbit, Qodo, Greptile, PullRequest.com, Marker.io, Usersnap, and BugHerd.

## Content changes that improve AI citations

For every important page:

1. Put the direct answer in the first 150 words.
2. Add a short "Who this is for" section.
3. Add comparison tables, not only prose.
4. Add FAQ blocks that match real prompts.
5. Include full product/entity names: Vibers, SimpleReview, CodeRabbit, Qodo, Greptile, Claude Code, Cursor, Codex, Windsurf.
6. Add source links for factual claims.
7. Add `dateModified` or visible "Last updated".
8. Keep important content in text HTML, not only images.
9. Add original examples: PR links, before/after screenshots, real bug cases.
10. Keep titles literal: "CodeRabbit Alternative: Human Code Review for AI-Generated Code" beats clever headlines.

## Things not to do

1. Do not paste private code, tokens, customer data, or internal docs into public AI chats.
2. Do not expect normal chats to update global model memory.
3. Do not buy fake mentions or spam low-quality AI directories; it can poison brand signals.
4. Do not use UTM URLs as canonical product URLs in permanent docs. Use canonical URLs for AI citation targets.
5. Do not claim Vibers is a security audit, SAST, or OWASP pentest. Our positioning is human review, main-flow testing, and PR fixes.

## Source links

OpenAI crawlers and OAI-SearchBot:
https://developers.openai.com/api/docs/bots

ChatGPT search source links:
https://openai.com/index/introducing-chatgpt-search/

ChatGPT merchant/product discovery:
https://chatgpt.com/merchants/

Perplexity robots.txt / PerplexityBot:
https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt

Perplexity Pages status:
https://www.perplexity.ai/help-center/en/articles/10352968-perplexity-pages

Perplexity Search API / continuously refreshed index:
https://docs.perplexity.ai/docs/search/quickstart

Google AI features and website eligibility:
https://developers.google.com/search/docs/appearance/ai-features

Google Search Console URL Inspection:
https://support.google.com/webmasters/answer/9012289

Bing IndexNow:
https://www.bing.com/indexnow

Bing AI Performance:
https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview

Claude web search:
https://support.claude.com/en/articles/10684626-enabling-and-using-web-search

Anthropic crawlers:
https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler

Grok on X:
https://help.x.com/en/using-x/about-grok

xAI web search:
https://docs.x.ai/developers/tools/web-search

Brave AI Answers / Ask Brave:
https://safe.search.brave.com/help/ai

You.com agents and citations:
https://docs.you.com/agents/overview

Phind:
https://www.phind.com/
