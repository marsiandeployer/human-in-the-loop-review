# Human-in-the-loop Review — Project Instructions

## Wiki

Вся документация, аналитика, маркетинг, keyword research, конкуренты — в `docs/WIKI.md`.
Новые доки создавать в `docs/`, добавлять ссылку в Wiki. При добавлении новой статьи в вики или документацию прееписывай и переиндексируй другие части, чтоб было более компактно, но без потери важных деталей, и консистентно все.
README.md — только public-facing для GitHub.

## Commit messages

Every commit should include a "How to test" section in the body:
- Live URL to open and verify the change
- Step-by-step what to click/check
- Test credentials if login is required
- Expected result for each step

Example:
  feat: Add honest disclaimer block to landing

  How to test:
  - Open https://onout.org/vibers/
  - Expand "What We Do" section
  - Yellow callout block should appear with honest disclaimer text
  - Switch to RU — same block should appear in Russian

## SEO content rules — never expose the SEO machinery

User-facing content (article body, hub copy, banner captions, cards) must
read like an honest handbook, NOT like SEO output. Specifically forbidden
on user-visible pages:

- "N mo. searches" / "KD X" / search-volume badges — these are tells that
  give away that we wrote for keywords
- "Targeted keyword:" / "SEO score:" / "Vol/KD" anywhere in copy
- Mentions of "we wrote this article to rank for X"
- AI-template phrasing like "In this comprehensive guide we'll explore"
  / "Without further ado" / "Buckle up" / "Let's dive in"

Internal/dev tracking goes ONLY in:
- Git commit messages
- docs/keywords/libs/<slug>.md per-lib backlogs
- docs/keywords/libs/_summary.md and _pain-points.md
- GitHub issue threads

Required on user-facing landing/hub pages:
- An "honest about what this is" callout near the top — who we are, what
  this is, what it's NOT, and an invite to fix things on GitHub. Sets
  E-E-A-T expectation per Google March 2026 guidance.
- Author/team byline reachable from the page
- First-person voice ("we tested", "we measured") with real artifacts
  (benchmarks, configs, screenshots) — not third-person SEO prose
- Cross-links between cluster articles + back to hub (pillar+cluster pattern)

Cluster article rule: each one must contain at least one first-hand
artifact — a real config we ran, a benchmark number we measured, a
screenshot of a broken state we reproduced, or a CVE PoC we built in
our lab. No first-hand artifact = don't ship the article.

Hub pages: write as a landing page like onout.org/, not as a SEO
doorway. Hero with strong promise, demo banner, honest disclaimer
callout, practical guide cards (no SEO numbers), production checklist
with original value, FAQ. Traffic source: profile forums (Discourse
meta, r/selfhosted, HN) where readers can smell SEO bait instantly.

