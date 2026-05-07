# Headless CMS keyword research summary — 2026-05-07

Source: Semrush Keyword Magic, US database, broad-match seeds.
Two passes: (1) bare-word seeds for ~33 CMSes, (2) disambiguating re-runs for noisy seeds.

## Important caveat — bare-word seeds pull noise

Several CMSes share their name with unrelated higher-volume terms. The bare-seed CSVs include
that noise. **Do not treat the raw "Total Vol/mo" of bare-seed CSVs as a meaningful CMS keyword
footprint without manual filtering.**

Examples observed in bare-seed batch:
- `crystallize` (e-commerce CMS) → top result "crystal palace vs fredrikstad" 6.12M/mo (English football)
- `contentful` (CMS) → top result "content marketing" 2.24M/mo (generic SEO term)
- `builder_io` → top result "resume io resume builder" 8100/mo (resume tool)
- `keystatic` → top result "m audio keystation 88" 880/mo (MIDI keyboard)
- `vault-cms` → top result "cms spinal cord stimulator" (medical)
- `spinal-cms` → same medical-device noise

## Re-run results (2026-05-07 disambiguating queries)

| Original seed | Re-run seed | Status | Rows | Brand-relevant kws | Brand-relevant vol |
|---------------|-------------|--------|-----:|-------------------:|-------------------:|
| `sanity cms` (timed out) | `sanity headless cms` | OK | 29 | 28 | 390/mo |
| `crystallize` (football noise) | `crystallize commerce` | OK | 405 | 2 | 10/mo |
| `contentful` (content-marketing noise) | `contentful cms` | OK | 2,246 | 170 | 2,530/mo |
| `builder_io` (resume noise) | `builder.io cms` | OK | 22 | 21 | 530/mo |
| `keystatic` (MIDI keyboard noise) | `keystatic cms` | OK | 1 | 1 | 20/mo |
| `vault cms` (HashiCorp/medical noise) | `vault headless cms`, `vault cms platform`, `fjord vault cms` | **FAILED** — Semrush returned 0 rows for all 3 disambiguated seeds; "Export button not found" because no data |

**Vault CMS conclusion:** It has effectively zero US search demand under any disambiguating
phrasing we tried. Stays in Tier 3 round-up, no dedicated page.

## Clean-signal CMSes (top keyword matches the CMS itself)

Sorted by clean brand-keyword volume (filtered to terms containing the brand name).

| CMS | Slug | Brand-relevant vol | Brand-relevant kws | Backlog |
|-----|------|-------------------:|-------------------:|---------|
| Storyblok | `storyblok` | 13,250/mo | 631 | `libs/storyblok.md` |
| Ghost CMS | `ghost-cms` | 11,490/mo | 650 | `libs/ghost-cms.md` |
| Contentstack | `contentstack` | 9,440/mo | 512 | `libs/contentstack.md` |
| Contentful | `contentful` (re-run) | 2,530/mo | 170 | `libs/contentful.md` |
| Hygraph | `hygraph` | 2,300/mo | 226 | `libs/hygraph.md` |
| Hashnode | `hashnode` | 2,250/mo | 126 | `libs/hashnode.md` |
| Decap CMS | `decap-cms` | 1,460/mo | 25 | `libs/decap-cms.md` |
| Sitecore XM Cloud | `sitecore-xm` | 1,440/mo | 125 | `libs/sitecore-xm.md` |
| DatoCMS | `datocms` | 1,310/mo | 150 | `libs/datocms.md` |
| Optimizely CMS | `optimizely-cms` | 1,070/mo | 93 | `libs/optimizely-cms.md` |
| ButterCMS | `buttercms` | 850/mo | 123 | `libs/buttercms.md` |
| Kontent.ai | `kontent-ai` | 650/mo | 60 | `libs/kontent-ai.md` |
| TinaCMS | `tinacms` | 590/mo | 39 | `libs/tinacms.md` |
| Builder.io | `builder-io` (re-run) | 530/mo | 21 | `libs/builder-io.md` |
| CloudCannon | `cloudcannon` | 430/mo | 76 | `libs/cloudcannon.md` |
| Sanity | `sanity` (re-run) | 390/mo | 28 | `libs/sanity.md` |
| Prismic | `prismic-cms` | 380/mo | 53 | `libs/prismic-cms.md` |
| KeystoneJS | `keystonejs` | 330/mo | 324 | `libs/keystonejs.md` |
| Pages CMS | `pages-cms` | 270/mo | 21 | `libs/pages-cms.md` |
| microCMS | `microcms` | 260/mo | 51 | `libs/microcms.md` |
| ApostropheCMS | `apostrophecms` | 240/mo | 41 | `libs/apostrophecms.md` |
| JekyllPad | `jekyllpad` | 140/mo | 1 | `libs/jekyllpad.md` |
| Spinal CMS | `spinal-cms` | 70/mo | 12 | `libs/spinal-cms.md` |
| Cosmic | `cosmic-cms` | 60/mo | 9 | `libs/cosmic-cms.md` |
| Caisy | `caisy-cms` | 50/mo | 3 | `libs/caisy-cms.md` |
| Flotiq | `flotiq` | 30/mo | 7 | `libs/flotiq.md` |
| Front Matter CMS | `front-matter-cms` | 20/mo | 1 | `libs/front-matter-cms.md` |
| Prepr CMS | `prepr-cms` | 20/mo | 2 | `libs/prepr-cms.md` |
| Keystatic | `keystatic` (re-run) | 20/mo | 1 | `libs/keystatic.md` |
| Crystallize | `crystallize` (re-run) | 10/mo | 2 | `libs/crystallize.md` |
| GitCMS | `gitcms` | 10/mo | 1 | `libs/gitcms.md` |
| Sitepins | `sitepins` | 10/mo | 1 | `libs/sitepins.md` |
| Vault CMS | `vault-cms` | 10/mo | 3 | `libs/vault-cms.md` |
| StudioCMS | `studiocms` | 0/mo | 2 | `libs/studiocms.md` |

## Tier recommendations (post-filter brand-relevant volume)

- 🟢 **Tier 1 (≥2k brand-volume)** — Storyblok, Ghost CMS, Contentstack, Contentful,
  Hygraph, Hashnode. Worth a hub + ≥1 first-hand article each (only when we deploy
  and find real artifacts).
- 🟡 **Tier 2 (300–2k brand-volume)** — Decap, Sitecore XM Cloud, DatoCMS, Optimizely CMS,
  ButterCMS, Kontent.ai, TinaCMS, Builder.io, CloudCannon, Sanity, Prismic, KeystoneJS.
  Comparison-page candidates; not standalone hubs.
- 🔴 **Tier 3 (<300 brand-volume)** — Pages CMS, microCMS, ApostropheCMS, JekyllPad,
  Spinal, Cosmic, Caisy, Flotiq, Front Matter CMS, Prepr, Keystatic, Crystallize,
  GitCMS, Sitepins, Vault, StudioCMS. Mention only in a "small-footprint headless
  CMS landscape" round-up, no dedicated pages.

## Files

CSVs in this directory: 38 (33 bare-seed + 5 disambiguated re-runs).
Per-CMS backlog markdown files: 34 in `docs/keywords/libs/` (one per CMS we
pulled data for; bare-seed duplicates of contentful / crystallize / builder_io /
keystatic are NOT regenerated — the disambiguated re-run is the canonical one).

## Re-run queue (2026-05-07) — completed

- ✅ `sanity` → re-queried as `sanity headless cms` (29 kws, 390/mo brand-relevant)
- ✅ `crystallize` → re-queried as `crystallize commerce` (405 kws, 10/mo brand-relevant)
- ✅ `contentful` → re-queried as `contentful cms` (2,246 kws, 2,530/mo brand-relevant)
- ✅ `builder_io` → re-queried as `builder.io cms` (22 kws, 530/mo brand-relevant)
- ✅ `keystatic` → re-queried as `keystatic cms` (1 kw, 20/mo brand-relevant)
- ❌ `vault cms` → tried `vault headless cms`, `vault cms platform`, `fjord vault cms`
  — all returned 0 rows. Vault CMS has no measurable US search demand. Stays in Tier 3.
