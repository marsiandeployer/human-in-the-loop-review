#!/usr/bin/env python3
"""Analyze Semrush CSVs for 38 self-hosted libraries.

For each library:
  - filter keywords that contain the lib name (drops generic-word collisions,
    e.g. "caramel frappe", "mocha frappe", "discourse analysis")
  - extract top keywords by volume, intent split, total volume
  - suggest 5–10 article topic ideas based on top long-tail patterns
  - write docs/keywords/libs/<slug>.md

Also writes a summary table to docs/keywords/libs/_summary.md
which is the body for GitHub issue #69.
"""
import csv
import re
from pathlib import Path
from collections import Counter, defaultdict

KEYWORDS_DIR = Path("/root/vibers/docs/keywords")
OUT_DIR = KEYWORDS_DIR / "libs"
OUT_DIR.mkdir(exist_ok=True)
DATE = "2026-05-01"

# (slug, display_name, match_terms[], forbidden_terms[]) — relevance filter.
# A keyword is "relevant" if any match_term appears as substring (case-insensitive),
# AND no forbidden_term appears. Forbidden lists kill generic-word collisions
# (drinks for Frappe, aviation for Plane, restaurants for Rasa, etc).
FORBIDDEN_DEFAULT = []
LIBS = [
    ("rocket-chat",         "Rocket.Chat",           ["rocket.chat", "rocketchat", "rocket chat"]),
    ("mautic",              "Mautic",                ["mautic"]),
    ("discourse",           "Discourse",             ["discourse forum", "discourse hosting", "discourse self", "discourse install", "discourse plugin", "discourse theme", "discourse vs", "discourse alternative", "discourse api", "discourse docker", "discourse setup", "civilized discourse"]),
    ("flarum",              "Flarum",                ["flarum"]),
    ("nodebb",              "NodeBB",                ["nodebb", "node bb", "node-bb"]),
    ("redmine",             "Redmine",               ["redmine"]),
    ("erpnext",             "ERPNext",               ["erpnext", "erp next", "erp-next"]),
    ("frappe",              "Frappe",                ["frappe framework", "frappe erp", "frappe cloud", "frappe docker", "frappe bench", "frappe app", "frappe install", "frappe hosting", "frappe vs", "frappe api", "frappe books", "frappe hr", "frappe crm"]),
    ("rasa",                "Rasa",                  ["rasa chatbot", "rasa nlu", "rasa core", "rasa open", "rasa pro", "rasa x ", "rasa-x", "rasa framework", "rasa stack", "rasa python", "rasa install", "rasa docker", "rasa rest", "rasa vs", "rasa alternative", "rasa bot", "rasa training", "rasa story", "rasa model", "rasa action"]),
    ("espocrm",             "EspoCRM",               ["espocrm", "espo crm", "espo-crm"]),
    ("suitecrm",            "SuiteCRM",              ["suitecrm", "suite crm", "suite-crm"]),
    ("chatwoot",            "Chatwoot",              ["chatwoot"]),
    ("zammad",              "Zammad",                ["zammad"]),
    ("freescout",           "FreeScout",             ["freescout", "free scout"]),
    ("live-helper-chat",    "Live Helper Chat",      ["live helper chat", "livehelperchat"]),
    ("typebot",             "Typebot",               ["typebot"]),
    ("flowise",             "Flowise",               ["flowise"]),
    ("dify",                "Dify",                  ["dify"]),
    ("langflow",            "Langflow",              ["langflow", "lang flow"]),
    ("open-webui",          "Open WebUI",            ["open webui", "open-webui", "openwebui"]),
    ("appsmith",            "Appsmith",              ["appsmith"]),
    ("tooljet",             "ToolJet",               ["tooljet"]),
    ("budibase",            "Budibase",              ["budibase"]),
    ("posthog",             "PostHog",               ["posthog"]),
    ("matomo",              "Matomo",                ["matomo"]),
    ("plausible-analytics", "Plausible Analytics",   ["plausible analytics", "plausible.io", "plausibleio"]),
    ("medusa",              "Medusa",                ["medusajs", "medusa.js", "medusa js", "medusa commerce", "medusa store", "medusa admin", "medusa next", "medusa shopify", "medusa headless", "medusa ecommerce", "medusa e-commerce", "medusa stripe", "medusa plugin", "medusa cart", "medusa product", "medusa api"]),
    ("saleor",              "Saleor",                ["saleor"]),
    ("sylius",              "Sylius",                ["sylius"]),
    ("vendure",             "Vendure",               ["vendure"]),
    ("cal-com",             "Cal.com",               ["cal.com", "calcom", "cal-com", "cal scheduling", "cal booking"]),
    ("cal-diy",             "Cal.diy",               ["cal.diy", "caldiy", "cal diy", "cal-diy"]),
    ("snipe-it",            "Snipe-IT",              ["snipe-it", "snipe it", "snipeit"]),
    ("invoice-ninja",       "Invoice Ninja",         ["invoice ninja", "invoiceninja"]),
    ("listmonk",            "listmonk",              ["listmonk", "list monk"]),
    ("openproject",         "OpenProject",           ["openproject", "open project", "open-project"]),
    ("plane",               "Plane",                 ["plane.so", "planeso", "plane.io", "plane io", "plane open source", "plane self-host", "plane self host", "plane project management", "plane work item", "plane jira alternative", "plane software jira", "plane.tools"]),
    ("taiga",               "Taiga",                 ["taiga.io", "taigaio", "taiga io", "taiga project", "taiga scrum", "taiga kanban", "taiga agile", "taiga vs", "taiga jira", "taiga self", "taiga docker", "taiga install", "taiga api", "taiga github"]),
]

def parse_csv(path: Path):
    rows = []
    with path.open() as f:
        for r in csv.DictReader(f):
            try:
                vol = int(r.get("Volume") or 0)
            except Exception:
                vol = 0
            kw = (r.get("Keyword") or "").strip()
            intent = r.get("Intent") or ""
            try:
                kd = int(r.get("Keyword Difficulty") or 0)
            except Exception:
                kd = 0
            try:
                cpc = float(r.get("CPC (USD)") or 0)
            except Exception:
                cpc = 0.0
            rows.append({"kw": kw, "vol": vol, "intent": intent, "kd": kd, "cpc": cpc})
    return rows

# Forbidden terms per slug — keywords containing any of these are dropped
# even if they match the inclusion filter. Used for ambiguous library names.
FORBIDDEN = {
    "plane": [
        "focal plane", "focal-plane", "second focal", "first focal",
        "boeing", "777", "md-11", "md11", "airbus", "airplane", "aircraft", "aviation",
        "plain", "geometry", "axis", "math", "coordinate",
        "wing", "flight", "pilot", "airport", "passenger",
    ],
    "frappe": [
        "milkshake", "frappuccino", "frapuccino", "latte", "mocha", "caramel",
        "starbucks", "mcdonald", "mcdonalds", "dunkin", "drink", "recipe",
        "iced coffee", "iced-coffee", "chocolate", "vanilla", "ice cream",
        "calories", "espresso", "smoothie", "creme", "cream",
    ],
    "rasa": [
        "restaurant", "menu", "nyc", "east greenwich", "rhode island",
        "california ", "rasa restaurant", "yelp", "reservation",
        "ayurveda", "ayurvedic", "skincare", "tea", "spa",
        "tabula rasa", "tabularasa", "rasa malai", "rasa gulla",
    ],
    "discourse": [
        "discourse analysis", "critical discourse", "discourse marker",
        "academic discourse", "discourse community", "discourse essay",
        "discourse meaning", "discourse definition",
    ],
    "medusa": [
        "greek mythology", "myth", "hair salon", "medusa salon",
        "medusa head", "medusa gorgon", "medusa story", "perseus",
        "medusa tattoo", "medusa makeup", "medusa snake", "medusa cartoon",
        "medusa monster", "medusa goddess", "medusa film", "medusa movie",
    ],
    "saleor": [
        "salor", "salero",
    ],
    "matomo": [
        "matamoros", "matomi",
    ],
    "plane": [
        "focal plane", "focal-plane", "second focal", "first focal",
        "boeing", "777", "md-11", "md11", "airbus", "airplane", "aircraft", "aviation",
        "plain", "geometry", "axis", "math", "coordinate",
        "wing", "flight", "pilot", "airport", "passenger",
    ],
    "taiga": [
        "taiga forest", "siberian taiga", "taiga biome", "taiga animals",
        "taiga climate", "taiga vegetation", "taiga ecosystem",
        "taiga tundra", "taiga vs tundra", "taiga drink", "taiga restaurant",
        "taiga sushi", "taiga moss", "taiga plants", "taiga weather",
    ],
    "vendure": [
        "vendor ", "venture", "vendure atlanta", "vendure kitchen",
        "vendure restaurant", "vendure menu", "vendure georgia",
    ],
    "sylius": [
        "stylus",
    ],
    "dify": [
        "edify",
    ],
    "cal-com": [
        "benefits cal", "benifits cal", "benfits cal", "benefit cal", "edd.cal",
        "calfresh", "calworks", "covered cal", "cal poly", "cal state",
        "calhfa", "calpers", "calsavers", "covered california",
    ],
    "cal-diy": [
        "low cal", "lowcal", "low-cal", "starbucks", "calorie", "drink",
    ],
}

def relevant(kw: str, terms, forbidden):
    s = kw.lower()
    if not any(t in s for t in terms):
        return False
    if any(f in s for f in forbidden):
        return False
    return True

def article_ideas(slug, display, top_kw):
    """Suggest article angles from the long-tail."""
    ideas = []
    name_l = display.lower()
    # Heuristic patterns: look for intent signals
    pat_groups = [
        # High-intent first — drives most traffic + buyer intent
        (" alternative", f"{display} alternatives — open-source landscape"),
        (" vs ", f"{display} vs X — when to pick which"),
        (" install", f"How to install {display} — full step-by-step guide"),
        (" docker", f"How to deploy {display} with Docker (production-ready setup)"),
        (" hosting", f"{display} hosting — self-host vs managed (cost & ops)"),
        (" pricing", f"{display} pricing — free, cloud, enterprise compared"),
        (" tutorial", f"{display} for beginners — complete tutorial"),
        (" review", f"Honest {display} review — pros, cons, when to pick it"),
        (" plugin", f"Top {display} plugins/extensions reviewed"),
        (" theme", f"{display} theming guide — customize the UI"),
        (" api", f"{display} API tutorial — first integration in 30 min"),
        (" demo", f"{display} live demo — try before you self-host"),
        (" config", f"Production {display} config — security & performance"),
        (" not working", f"Common {display} errors and how to fix them"),
        (" error", f"Common {display} errors and how to fix them"),
        (" backup", f"Backup & restore strategy for {display}"),
        (" migration", f"Migrate to {display} — from SaaS to self-hosted"),
        (" upgrade", f"Upgrade {display} safely — version-to-version notes"),
        (" github", f"Reading the {display} source — what to know before forking"),
    ]
    # Iterate patterns by priority; pick the highest-volume keyword that triggers each.
    seen = set()
    for marker, idea in pat_groups:
        for kw, vol in top_kw:
            if marker in kw.lower() and idea not in seen:
                ideas.append((idea, kw, vol))
                seen.add(idea)
                break
        if len(ideas) >= 8:
            break
    # Always-on cornerstone
    cornerstone = f"What is {display}? — the complete guide for self-hosters"
    ideas.insert(0, (cornerstone, "(cornerstone)", 0))
    return ideas

summary_rows = []

for slug, display, terms in LIBS:
    csv_path = KEYWORDS_DIR / f"{slug}_broad-match_us_{DATE}.csv"
    if not csv_path.exists():
        print(f"MISSING: {csv_path}")
        continue
    all_rows = parse_csv(csv_path)
    forbidden = FORBIDDEN.get(slug, [])
    rel = [r for r in all_rows if relevant(r["kw"], terms, forbidden)]
    rel.sort(key=lambda r: r["vol"], reverse=True)

    total_vol = sum(r["vol"] for r in rel)
    total_all = sum(r["vol"] for r in all_rows)
    n_rel = len(rel)
    n_all = len(all_rows)

    # Intent breakdown (relevant only)
    intent_counter = Counter()
    for r in rel:
        for i in [x.strip() for x in r["intent"].split(",") if x.strip()]:
            intent_counter[i] += r["vol"]

    top10 = [(r["kw"], r["vol"]) for r in rel[:10]]
    ideas = article_ideas(slug, display, top10)

    # Build per-lib markdown
    md = []
    md.append(f"# {display} — keyword research & content backlog")
    md.append("")
    md.append(f"- **Source:** Semrush Keyword Magic, US, {DATE}")
    md.append(f"- **Raw CSV:** `docs/keywords/{slug}_broad-match_us_{DATE}.csv`")
    md.append(f"- **Filter:** match terms — `{', '.join(terms)}`")
    md.append("")
    md.append("## Volume snapshot")
    md.append("")
    md.append(f"- **Relevant keywords:** {n_rel:,} / {n_all:,} total in CSV")
    md.append(f"- **Total monthly volume (relevant):** {total_vol:,}")
    if n_all:
        md.append(f"- **Filter ratio:** {n_rel*100/n_all:.0f}% kept after relevance filter")
    if total_vol == 0:
        md.append("")
        md.append("> ⚠️ Zero relevant volume — Semrush returned mostly off-topic keywords (generic-word collision). Manual seed retry recommended.")
    md.append("")
    md.append("## Intent split (relevant volume)")
    md.append("")
    if intent_counter:
        for intent, vol in intent_counter.most_common():
            pct = vol * 100 / total_vol if total_vol else 0
            md.append(f"- **{intent}:** {vol:,} ({pct:.0f}%)")
    else:
        md.append("- _no intent data_")
    md.append("")
    md.append("## Top 25 keywords (relevant)")
    md.append("")
    md.append("| # | Keyword | Volume | KD | Intent |")
    md.append("|---|---------|-------:|---:|--------|")
    for i, r in enumerate(rel[:25], 1):
        md.append(f"| {i} | {r['kw']} | {r['vol']:,} | {r['kd']} | {r['intent']} |")
    md.append("")
    md.append("## Suggested article topics")
    md.append("")
    md.append("Order: cornerstone first, then long-tail in descending volume.")
    md.append("")
    for i, (idea, src_kw, src_vol) in enumerate(ideas, 1):
        if src_kw == "(cornerstone)":
            md.append(f"{i}. **{idea}** _(cornerstone)_")
        else:
            md.append(f"{i}. **{idea}** — driver kw: `{src_kw}` ({src_vol:,}/mo)")
    md.append("")
    md.append("## Notes for writers")
    md.append("")
    md.append(f"- Each article should naturally include `{display}` and one self-host alternative angle (e.g. vs Intercom, vs Zendesk, etc.)")
    md.append("- Cross-link to other libraries in the same niche where relevant.")
    md.append("- Add internal link back to onout.org/ (SimpleReview) only if topic touches code review / feedback / dev tooling.")
    md.append("")

    out = OUT_DIR / f"{slug}.md"
    out.write_text("\n".join(md))

    # Top 5 keywords for summary
    top5 = ", ".join(f"`{r['kw']}` ({r['vol']:,})" for r in rel[:5])
    first_article = ideas[1][0] if len(ideas) > 1 else ideas[0][0]
    summary_rows.append({
        "display": display,
        "slug": slug,
        "n_rel": n_rel,
        "n_all": n_all,
        "total_vol": total_vol,
        "top5": top5,
        "first_article": first_article,
    })

# Summary markdown
summary_rows.sort(key=lambda r: r["total_vol"], reverse=True)
sum_md = []
sum_md.append("# 38 self-hosted libraries — keyword research summary")
sum_md.append("")
sum_md.append(f"Source: Semrush Keyword Magic, US, {DATE}.  ")
sum_md.append(f"Per-library backlog: `docs/keywords/libs/<slug>.md`.  ")
sum_md.append(f"Raw CSVs: `docs/keywords/<slug>_broad-match_us_{DATE}.csv`.")
sum_md.append("")
sum_md.append("Sorted by relevant total monthly volume (desc).")
sum_md.append("")
sum_md.append("| # | Library | Relevant kws | Total volume | Top keywords | First article suggestion |")
sum_md.append("|---|---------|-------------:|-------------:|--------------|--------------------------|")
for i, r in enumerate(summary_rows, 1):
    sum_md.append(f"| {i} | **[{r['display']}](libs/{r['slug']}.md)** | {r['n_rel']:,} | {r['total_vol']:,} | {r['top5']} | {r['first_article']} |")
sum_md.append("")
sum_md.append("## Tier recommendations")
sum_md.append("")
big = [r for r in summary_rows if r["total_vol"] >= 10000]
mid = [r for r in summary_rows if 1000 <= r["total_vol"] < 10000]
small = [r for r in summary_rows if r["total_vol"] < 1000]
sum_md.append(f"- **Tier 1 (≥10k mo. volume) — {len(big)} libs:** prime candidates for full hub `/<lib>/` + 3–5 article cluster.")
for r in big:
    sum_md.append(f"  - {r['display']} ({r['total_vol']:,}/mo)")
sum_md.append(f"- **Tier 2 (1k–10k mo. volume) — {len(mid)} libs:** single hub article, possibly extend later.")
for r in mid:
    sum_md.append(f"  - {r['display']} ({r['total_vol']:,}/mo)")
sum_md.append(f"- **Tier 3 (<1k mo. volume) — {len(small)} libs:** comparison list inclusion only, no hub.")
for r in small:
    sum_md.append(f"  - {r['display']} ({r['total_vol']:,}/mo)")
sum_md.append("")

(OUT_DIR / "_summary.md").write_text("\n".join(sum_md))
print(f"Wrote {len(LIBS)} per-lib markdowns + _summary.md to {OUT_DIR}")
