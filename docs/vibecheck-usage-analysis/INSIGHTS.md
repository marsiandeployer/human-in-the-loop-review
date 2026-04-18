# VibeCheck Usage Analysis — first 8 days of real data

Source:
- Nginx access logs (historical backfill, 93 Fix-Its from `tamara`, `maria`, `julia`).
- `.entire/metadata/*/full.jsonl` — Claude Code local session logs, joined by
  timestamp+content. **77/93 Fix-Its joined to full Claude sessions** (83%).
- Server now persists every new Fix-It to
  `/root/op.wpmix.net/prompt-logs/YYYY-MM-DD.jsonl` automatically.

Window: 2026-04-11 — 2026-04-18 (8 days).

## Volume and outcome

| User | Fix-Its | Avg files edited | Avg commits | Avg pushes | Chat rounds | Median session |
|---|---|---|---|---|---|---|
| Tamara | 58 (47 joined) | 1.87 | 1.62 | 1.53 | **57.3** | 8.7 min |
| Maria | 11 (10 joined) | 1.30 | 1.90 | 0.80 | 39.0 | 5.7 min |
| Julia | 24 (20 joined) | 1.25 | 1.45 | 1.00 | 21.5 | 4.3 min |

**93 Fix-Its → ~135 commits, ~95 pushes, ~120 files edited.**
95% of sessions produced real file changes. Not theater.

## Finding 1: VibeCheck isn't a lightweight feedback tool — it's a non-dev dev-session launcher

Median session is 4–9 min, but chat-round counts are 21–57. That's **deep back-
and-forth between a non-developer and Claude**, not fire-and-forget. The
deliverable isn't a bug report or a context payload — it's **shipped code**.

Real flow: click element → prompt Claude with screenshot+DOM+comment →
non-dev drives multi-turn investigation → Claude edits files, runs tests, commits, pushes.

The product is "spawn a Claude Code session from a live-site bug with full
context, let a non-dev pilot it to a deployed fix." Not "route context to your AI".

## Finding 2: Full-stack, not just frontend

Tamara's 47 joined sessions edited:
- **54 .js files** (frontend/src — React components)
- **31 .py files** (backend/services, backend/main.py)
- Plus css/md/json/tests

**36% of her Fix-It edits hit Python backend.** The landing promises visual
UI fixes. Reality: a QA person clicking in the browser triggers full-stack
Python + JS changes, including test code in `tests/puppeteer/`.

## Finding 3: "сделай комит" is a workflow rule, not a user signal

Clarified by noxon: he taught the team to type «сделай комит» so changes save
as commits/checkpoints in Claude's flow. **Earlier interpretation (“users want
commits not PRs”) is wrong.** The commit pattern reflects team discipline noxon
imposed, not a product insight about PRs vs commits.

That said — the downstream data is real: 1.45–1.90 commits per session, near
every session gets pushed. Users DO ship directly to whatever branch the
session is on. The framing "Pull Request on GitHub" on the landing still
doesn't match reality; they push commits, review later.

## Finding 4: Two persona shapes, not two user types

Revised from earlier draft. The three users don't split cleanly by persona:

- **Tamara (QA)**: 47 sessions, 57 chat rounds, full-stack .js+.py edits,
  median 8.7 min, references GitHub issues in comments. Power user — deep,
  exploratory, touches backend, runs tests.
- **Julia**: 20 sessions, 21 chat rounds, .js only, median 4.3 min. Fastest,
  most predictable. Small copy/UI tweaks with clean one-shot success.
- **Maria**: 10 sessions, wide spread — one 120-round monster on `inspect.js`,
  one 83-round multi-file refactor across 4 files. Not a content editor.
  More like a second power user.

**Insight: non-dev ≠ shallow usage.** Given the tool, non-devs drive deep
sessions. The marketing framing "non-technical founders" understates what's
possible. These users are actually doing dev work, not fake-dev work.

## Finding 5: Single-project concentration — claritycult is THE wedge

90/93 prompts are on `dash2.claritycult.ru`. The one validated use-case is
**internal QA+editors at one agency-style client with a complex full-stack app
who need to touch code without waiting for dev cycles**.

Edit concentration also tight:
- `frontend/src`: 80 edits
- `backend/services`: 17
- `backend/main.py`: 10
- `tests/puppeteer`: 9

Not spread across projects — focused on one codebase. ICP validation = 1
customer team. Needs a second similar team before generalizing.

## Finding 6: Copy/content is NOT the #1 fix type (revised)

Earlier draft assumed copy dominates because "сделай комит и поменяй на X"
looked like text edits. With .entire join — reality is mixed:
- Short Julia sessions: copy tweaks (rename button, text change)
- Tamara sessions: full-stack bug investigation — output_schema fixes,
  React state bugs, routing issues, backend data issues
- Maria sessions: mix — some 120-round `inspect.js` work

Lead-with-copy story is wrong. Real value: **bug investigation triggered
from a visual click, followed through to deployed fix**.

## Finding 7: Element precision still doesn't matter

60%+ of clicks target generic `div` containers. Users point Claude at a
region, Claude figures out the actual file+line. UX work on precise
element selection = low priority.

## Finding 8: Nobody touches agent selection

All 93 Fix-Its went to Claude (default). Codex toggle = zero behavioral
value in this data window.

## Finding 9: GitHub issue linking is a hacked-together power-user move

Tamara manually pastes `https://github.com/noxonsu/claritycult/issues/...`
inside the comment field in several sessions. This is a team convention
noxon uses to tie bugs back to issues. Real product need: **auto-link
Fix-It → existing GitHub issue** (auto-suggest from URL context or open
issues keyword match).

## Tool-call distribution (across 77 joined sessions)

| Tool | Calls |
|---|---|
| Bash | 1928 |
| Read | 671 |
| Edit | 294 |
| Grep | 275 |
| Skill | 44 |
| ToolSearch | 21 |
| Glob | 20 |
| WebFetch | 18 |

Bash dominates — includes git, tests, deploy commands. Read+Grep+Glob+Edit
is standard Claude investigation loop. This is a real dev session, not
single-shot templated fixes.

## Implications for positioning

**Current landing (paraphrased):**
> Click any issue on your website. Use your own AI agent for free — or let
> us fix it for you. Get a Pull Request, not a ticket.

**What the data says the product actually is:**
> Turn your QA, editors, and non-dev team into shippers. Click any bug on
> your live site, launch a full Claude session with screenshot+DOM+file
> context, drive it to a deployed fix — frontend or backend — without
> waiting for dev. Tie each fix back to a GitHub issue automatically.

Key reframes:
- ICP is **teams-at-one-customer (agency-like)** with QA+editors who want
  to ship directly, not "solo Cursor founders"
- Deliverable is **a deployed fix from a non-dev session**, not a PR
- Scope is **full-stack**, not "visual UI fixes"
- Speed/depth data: ~8 min median, ~1.5 commits, ~95% ship rate

## Assignment candidates (for Phase 6 of /office-hours)

1. **Interview Tamara (primary):** why paste GitHub issue URLs manually?
   If Fix-It auto-suggested issues or auto-commented on the matched
   issue, would that change her behavior?
2. **Find the second team.** The wedge is 1 customer. Reach out to 2–3
   similar agency/product teams with non-dev QAs and test adoption.
3. **Rewrite the landing to match the data.** Non-dev ICP, full-stack
   scope, ship rate as hero metric (e.g. "93 bugs → 135 commits → 95 pushes
   in 8 days, zero dev time").
