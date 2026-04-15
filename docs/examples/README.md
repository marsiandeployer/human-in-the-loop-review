# Landing Examples

This folder is the source of truth for examples shown in the `/vibers/` landing page slider.

Use one file per case.

Required structure for every case:

- `title` — short and specific
- `summary` — one sentence explaining the bug
- `before` — screenshot URL or local asset path
- `after` — screenshot URL or local asset path
- `prompt` — English prompt that could realistically drive the fix

Optional fields:

- `proof` — PR, commit, issue, or live page link
- `notes` — short implementation note if the landing copy needs context

If a bug is hard to reproduce later, keep the exact capture or page link in `proof` so the example still points to the concrete screen where the issue was seen.

Current examples:

- `mobile-floor-map-fix.md`
- `paycif-mobile-layout.md`
- `chat-message-wrapping.md`
- `poster-preview-loading.md`
- `floor-map-edge-slots.md`
- `brand-identity-screen-orientation.md`

Asset files that are not already public can be stored in `docs/examples/assets/`.
