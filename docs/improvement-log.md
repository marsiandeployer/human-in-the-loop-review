# Improvement Log — onout.org/vibers Prototype Evaluation

## Score Tracking

| Criterion | R1 | R2 | Delta | Notes |
|-----------|----|----|-------|-------|
| Clarity | 6 | 6 | 0 | Summary visible above fold now, but R2 evaluator hit CF cache |
| Visual Identity | 7 | 7 | 0 | Stable — CV style is distinct |
| Interaction Completeness | 7 | 8 | +1 | Fixed: privacy links, setup error handling |
| CTA Effectiveness | 5 | 5 | 0 | Install button added but not seen (CF cache); needs star repo link |
| Persona Fit | 7 | 7 | 0 | Stable — good targeting |
| Competitive Differentiation | 7 | 7 | 0 | Comparison table still hidden behind click |
| Trust & Credibility | 5 | 5 | 0 | 1 testimonial added but needs more |
| **Average** | **6.3** | **6.4** | **+0.1** | |

## Changes Applied (not yet re-evaluated on live)

### Round 1 → Round 2 (bug fixes)
- privacy.html: canonical URL fixed (`onout.org/vibers` instead of `onout.org/vibers/`)
- privacy.html: back-link changed from `/vibers/` to `/`
- setup.html: `.catch(() => showSuccess())` → shows error alert
- index.html footer: added Privacy link

### Round 2 → Applied (UX overhaul)
- Moved description + metrics above fold (visible without clicks)
- Added big purple "Install GitHub App — Free" button as primary CTA
- Skill command demoted to secondary CTA with better label
- Added real testimonial from MethasMP/Paycif with PR link
- Opened Problem and Example sections by default (`<details open>`)
- Star badge is now a clickable link to GitHub repo

## Remaining Issues (from both evaluators)
1. **Trustpilot widget**: `min-review-count=10` — shows nothing if < 10 reviews
2. **More testimonials needed**: only 1 real client (Paycif)
3. **Reviewer bio ambiguity**: "Senior engineers" (plural) but 1 GitHub avatar
4. **No "reviews completed" counter**: need to track and display
5. **Cloudflare caching**: visitors may see stale version — purge needed
6. **Tagline repeats title**: wasted space above fold
7. **"0 Clarifying questions" metric**: confusing without context
