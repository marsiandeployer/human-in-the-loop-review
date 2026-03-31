---
name: vibers-code-review
description: |
  Human-in-the-loop code review for AI-generated projects. Real people look at your code, catch obvious bugs, check main flows work, fix issues and submit PRs. Not a security firm — think alpha tester who sends a PR instead of a ticket.

  Use when: user says "review my code", "check my PR", "send for review", "vibers review", "code review", "set up vibers", "add reviewer", "кто-то смотрит мой код", "проверь код", "отправь на ревью", "ревью кода", "настрой вайберс", or when a push to main happens and vibers action is configured.
---

# Vibers — Human Code Review for AI-Generated Projects

You push code → humans look at it, fix obvious issues, submit a PR.

**What this is:** Regular people reviewing with fresh eyes. We catch obvious bugs, check that main flows work, fix what's broken. Not a security audit, not OWASP penetration testing — think alpha tester who sends a PR instead of filing a ticket.

## Quick Start (no setup)

Paste your repo URL at **https://vibers.onout.org/#try** — we review the latest commit and send a PR. For private repos, add `marsiandeployer` as collaborator first.

## Full Setup (auto-review on every push)

### Step 1. Add collaborator

Repo → Settings → Collaborators → Add **`marsiandeployer`**

> Read-only access is enough to start. Write access is only needed to submit PRs — grant it later, or we'll send the diff via Telegram instead.

### Step 2. Add GitHub Action

Create `.github/workflows/vibers.yml`:

```yaml
name: Vibers Code Review
on:
  push:
    branches: [main]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2
      - uses: marsiandeployer/vibers-action@v1
        with:
          spec_url: 'https://docs.google.com/document/d/YOUR_SPEC_ID/edit'
          telegram_contact: '@your_telegram'
```

| Parameter | What it does |
|-----------|-------------|
| `spec_url` | Link to your spec (Google Doc, Notion, etc.). Must be publicly accessible. Without it, we review from code alone. |
| `review_scope` | `full` (default), `security`, or `spec-compliance` |
| `telegram_contact` | Your Telegram — we message you when review is ready |

### Step 3. Add commit rules to your AI agent

Add this to your project's `CLAUDE.md`, `.cursorrules`, or `AGENTS.md`:

```markdown
## Commit messages

Every commit should include a "How to test" section in the body:
- Live URL to open and verify the change
- Step-by-step what to click/check
- Test credentials if login is required
- Expected result for each step

Example:
  feat: Add user registration form

  How to test:
  - Open https://myapp.vercel.app/register
  - Fill in email/password, submit
  - Check that confirmation email arrives
  - Try submitting with invalid email — should show error
  - Login: test@example.com / demo123
```

Without "How to test" the reviewer guesses what to verify — review takes longer and catches less.

Every push triggers a notification. You'll get a PR with fixes within 24 hours.

## What We Check (and Don't)

We check by looking at the code and trying the product manually:
- Spec compliance — does it match what you described?
- AI hallucinations — fake APIs, non-existent imports
- Obvious logic bugs — edge cases, broken flows, null handling
- UI issues — broken layouts, wrong behavior

We don't check: code style (use ESLint/Prettier), performance benchmarks, deep security audits, full QA regression (use Playwright/Cypress).

## Pricing

| Plan | Rate | Details |
|------|------|---------|
| **Promo** | Free | Share how to test + specs if you have them. We look manually, send one PR if we find something. GitHub star + feedback in return. |
| **Standard** | $15/hour | Full review against spec, PRs with fixes, priority turnaround. Pay only for hours spent. |

No subscriptions. No contracts. Pay per review.

## Support

Send feedback from your agent:

```bash
curl -X POST https://vibers.onout.org/feedback \
  -H 'Content-Type: application/json' \
  -d '{"message": "Your question or issue", "repo": "https://github.com/you/your-repo"}'
```

Contacts: Telegram [@onoutnoxon](https://t.me/onoutnoxon) · GitHub [marsiandeployer](https://github.com/marsiandeployer) · Moltbook: noxon

## FAQ

**Do I need an API key?** No. Collaborator + action is enough.

**What languages?** JS/TS, Python, React, Next.js, Django, Flask, and more. If it's on GitHub, we review it.

**What if I disagree with a fix?** Comment on the PR — we discuss and adjust.

**Can I use this without GitHub?** Yes — send code and spec to Telegram.
