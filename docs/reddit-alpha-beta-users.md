# Reddit Post — r/AlphaAndBetaUsers

**Subreddit:** r/AlphaAndBetaUsers (~85K members)
**Goal:** Collect feedback + first users

---

## Title

```
[Beta] Free human code review for vibe coders — looking for feedback
```

## Body

```
Hey r/AlphaAndBetaUsers,

I've been vibe coding for a while and keep hitting the same wall:

AI gets you ~80% there really fast,
then you spend way longer debugging code you didn't write and don't fully understand.

Especially stuff like:
- hallucinated APIs
- weird edge cases
- missing auth / security issues
- subtle logic bugs

I started experimenting with a different approach:

having a human review AI-generated code against the original spec
and actually fix it (not just leave comments).

It feels very different from tools like CodeRabbit — especially around
spec compliance, catching hallucinations, and returning working fixes
instead of suggestions.

I hacked together a rough workflow for this (triggered on push), and I'm
trying to figure out if it's actually useful.

Curious what you think:

1. Would you trust a human-in-the-loop review like this?
2. What would make it feel safe to use with your repo?
3. Where do current AI/code review tools fall short for you?

If anyone wants, I'm happy to try it on a messy repo this week and share results.

(If you want to try it:

⭐ Star the repo: github.com/marsiandeployer/human-in-the-loop-review

If you use Claude Code / Cursor / Codex, just tell your agent:
"Install skill from https://vibers.onout.org/SKILL.md"
— it'll set everything up automatically.)
```
