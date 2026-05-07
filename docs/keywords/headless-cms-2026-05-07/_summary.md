# Headless CMS keyword research summary — 2026-05-07

Source: Semrush Keyword Magic, US database, broad-match seeds (one seed per CMS name).
Batch script: `/tmp/cms_semrush_batch.sh` (committed history available in `git log`).

## Important caveat — bare-word seeds pull noise

Several CMSes share their name with unrelated higher-volume terms. The CSVs include
that noise. **Do not treat the raw "Total Vol/mo" as a meaningful CMS keyword footprint
without manual filtering.**

Examples observed:
- `crystallize` (e-commerce CMS) → top result "crystal palace vs fredrikstad" 6.12M/mo (English football)
- `contentful` (CMS) → top result "content marketing" 2.24M/mo (generic SEO term)
- `builder_io` → top result "resume io resume builder" 8100/mo (resume tool)
- `keystatic` → top result "m audio keystation 88" 880/mo (MIDI keyboard)
- `vault-cms` → top result "cms spinal cord stimulator" (medical)
- `spinal-cms` → same medical-device noise

Re-query with disambiguating terms (`<name> headless`, `<name> cms`, `<name>.com`) before
building per-lib backlogs for these.

## Clean-signal CMSes (top keyword matches the CMS itself)

Sorted by clean brand-keyword volume.

| CMS | Slug | Brand kw vol | KD | All kws |
|-----|------|-------------:|----|--------:|
| Storyblok | `storyblok` | 4,400/mo | — | 631 |
| Ghost CMS | `ghost-cms` | 4,400/mo | — | 650 (best non-trivial) |
| Contentstack | `contentstack` | 2,900/mo | — | 512 |
| Hashnode | `hashnode` | 1,300/mo | — | 129 |
| Decap CMS | `decap-cms` | 1,000/mo | — | 25 |
| Hygraph | `hygraph` | 590/mo | — | 226 |
| DatoCMS | `datocms` | 480/mo | — | 151 |
| Sitecore XM Cloud | `sitecore-xm` | 320/mo | — | 125 |
| ButterCMS | `buttercms` | 320/mo | — | 123 |
| TinaCMS | `tinacms` | 320/mo | — | 39 |
| KeystoneJS | `keystonejs` | 210/mo | — | 324 |
| Optimizely CMS | `optimizely-cms` | 210/mo | — | 258 |
| Kontent.ai | `kontent_ai` | 170/mo | — | 60 |
| Prismic CMS | `prismic-cms` | 170/mo | — | 53 |
| ApostropheCMS | `apostrophecms` | 170/mo | — | 41 |
| JekyllPad | `jekyllpad` | 140/mo | — | 1 |
| Studio CMS | `studiocms` | 70/mo | — | 3 |

## Tier recommendations

- 🟢 **Tier 1 (≥1k brand-volume)** — Storyblok, Ghost, Contentstack, Hashnode, Decap.
  Worth a hub + ≥1 first-hand article each (only when we deploy and find real artifacts).
- 🟡 **Tier 2 (170-590 brand-volume)** — Hygraph, DatoCMS, Sitecore XM Cloud, ButterCMS,
  TinaCMS, Kontent.ai, Prismic, Optimizely CMS, KeystoneJS, ApostropheCMS.
  Comparison-page candidates; not standalone hubs.
- 🔴 **Tier 3 (<170 brand-volume)** — JekyllPad, Studio CMS, microCMS, CloudCannon,
  Caisy, Cosmic, Crystallize, Vault, Flotiq, Front Matter CMS, Prepr CMS, GitCMS,
  Sitepins, Spinal CMS, Pages CMS, Builder.io (after noise removal).
  Only mention in a "small-footprint headless CMS landscape" round-up, no dedicated pages.

## Files

CSVs in this directory: 33. Per-CMS backlog markdown files (`docs/keywords/libs/<slug>.md`)
to be generated from these CSVs in a later pass — current `libs/*.md` files are from the
2026-05-01 lib batch and don't yet include these 33.

## Re-run queue

- `sanity` (failed at 16:06 in the batch)
- `crystallize` → re-query `crystallize commerce` to disambiguate
- `contentful` → re-query `contentful cms`
- `builder_io` → re-query `builder.io cms` or `builder.io visual editor`
- `keystatic` → re-query `keystatic cms`
- `vault cms` → re-query `vault headless cms` (HashiCorp Vault pollutes results)
