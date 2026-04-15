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

