#!/usr/bin/env python3
"""Extract pain-point keywords across all 38 libraries.

Pain point = user has a specific problem the article can solve.
NOT pain points: generic "install X", "what is X", "X github", "X pricing".
ARE pain points: errors, broken features, "how to do X feature", config issues.

Output: docs/keywords/libs/_pain-points.md
"""
import csv
import re
from pathlib import Path
from collections import defaultdict

KEYWORDS_DIR = Path("/root/vibers/docs/keywords")
OUT_FILE = KEYWORDS_DIR / "libs" / "_pain-points.md"
DATE = "2026-05-01"

# Lib slug -> display name + match terms (re-used from main analyzer)
import sys
sys.path.insert(0, str(KEYWORDS_DIR))
from importlib import import_module
mod = import_module("libs-analyzer-2026-05-01")
LIBS = mod.LIBS
FORBIDDEN = mod.FORBIDDEN
relevant = mod.relevant

# Pain-point signals (substring match, lowercased keyword).
# Each signal carries a category for grouping and a "boost" — keywords with strong
# pain signals (errors, crashes) ranked above weaker ones (just "how to").
PAIN_SIGNALS = [
    # Errors / brokenness — strongest pain
    ("error",         "errors / fixes",         3),
    ("not working",   "errors / fixes",         3),
    ("doesn't work",  "errors / fixes",         3),
    ("doesnt work",   "errors / fixes",         3),
    ("won't",         "errors / fixes",         3),
    ("wont ",         "errors / fixes",         3),
    ("can't",         "errors / fixes",         3),
    ("cant ",         "errors / fixes",         3),
    ("fix ",          "errors / fixes",         3),
    (" fix",          "errors / fixes",         3),
    ("broken",        "errors / fixes",         3),
    ("issue",         "errors / fixes",         2),
    ("problem",       "errors / fixes",         2),
    ("failed",        "errors / fixes",         3),
    ("fail ",         "errors / fixes",         3),
    ("crash",         "errors / fixes",         3),
    ("stuck",         "errors / fixes",         3),
    ("slow",          "performance",            2),
    ("timeout",       "errors / fixes",         3),
    ("500",           "errors / fixes",         3),
    ("502",           "errors / fixes",         3),
    ("503",           "errors / fixes",         3),
    ("504",           "errors / fixes",         3),
    ("404",           "errors / fixes",         3),
    ("403",           "errors / fixes",         3),
    ("permission denied", "errors / fixes",     3),
    ("undefined",     "errors / fixes",         2),
    ("missing",       "errors / fixes",         2),
    ("invalid",       "errors / fixes",         2),
    ("cors",          "errors / fixes",         3),
    # How-to (specific task, not install)
    ("how to ",       "how-to (specific task)", 2),
    ("how do i ",     "how-to (specific task)", 2),
    ("how can i ",    "how-to (specific task)", 2),
    # Config / customisation
    ("configure",     "config / customisation", 2),
    ("setup ",        "config / customisation", 1),
    (" setup",        "config / customisation", 1),
    ("enable ",       "config / customisation", 2),
    ("disable ",      "config / customisation", 2),
    ("custom ",       "config / customisation", 1),
    ("change ",       "config / customisation", 1),
    ("integrate",     "integration",            2),
    ("integration",   "integration",            2),
    ("connect ",      "integration",            2),
    ("webhook",       "integration",            2),
    # Migration / backup
    ("migrate",       "migration / backup",     2),
    ("migration",     "migration / backup",     2),
    ("import ",       "migration / backup",     2),
    ("export ",       "migration / backup",     2),
    ("backup",        "migration / backup",     2),
    ("restore",       "migration / backup",     2),
    # Comparison (decision pain)
    (" vs ",          "comparison / decision",  1),
    ("alternative",   "comparison / decision",  1),
    ("vs.",           "comparison / decision",  1),
]

# Drop these — they are install/branding/general queries we already cover
NEGATIVE_SIGNALS = [
    "install",            # already covered as own article topic
    "installation",
    "what is",            # cornerstone — already covered
    "wikipedia",
    "logo",
    "definition",
    "meaning",
    "stock",
    "pricing",            # already covered
    "price ",
    "github",             # too navigational
    "youtube",
    "linkedin",
    "twitter",
    "documentation",      # navigational
    " docs ",
    "homepage",
    "tutorial",           # too generic
    "for beginners",
    "review",             # already covered
    "demo",               # already covered
    "screenshots",
    "logo png",
]

def has_pain(kw: str):
    s = kw.lower()
    if any(neg in s for neg in NEGATIVE_SIGNALS):
        return None
    best = None
    for signal, category, boost in PAIN_SIGNALS:
        if signal in s:
            if best is None or boost > best[1]:
                best = (category, boost)
    return best  # (category, boost) or None

def parse_csv(path: Path):
    rows = []
    with path.open() as f:
        for r in csv.DictReader(f):
            try:
                vol = int(r.get("Volume") or 0)
            except Exception:
                vol = 0
            kw = (r.get("Keyword") or "").strip()
            try:
                kd = int(r.get("Keyword Difficulty") or 0)
            except Exception:
                kd = 0
            rows.append({"kw": kw, "vol": vol, "kd": kd, "intent": r.get("Intent") or ""})
    return rows

# Per-lib pain-point bucket
all_pains = []  # (lib_display, slug, kw, vol, kd, category, boost)
per_lib_pains = defaultdict(list)

for slug, display, terms in LIBS:
    csv_path = KEYWORDS_DIR / f"{slug}_broad-match_us_{DATE}.csv"
    if not csv_path.exists():
        continue
    forbidden = FORBIDDEN.get(slug, [])
    for r in parse_csv(csv_path):
        if not relevant(r["kw"], terms, forbidden):
            continue
        pain = has_pain(r["kw"])
        if pain is None:
            continue
        category, boost = pain
        entry = (display, slug, r["kw"], r["vol"], r["kd"], category, boost)
        all_pains.append(entry)
        per_lib_pains[slug].append(entry)

# Sort by volume * boost (heuristic: stronger pain on higher volume = better article candidate)
all_pains.sort(key=lambda e: e[3] * e[6], reverse=True)

# Build markdown
md = []
md.append("# Pain-point keywords — actionable article candidates")
md.append("")
md.append(f"Source: 38 lib CSVs (US, {DATE}). Filter: drop install/pricing/branding,")
md.append("keep keywords with concrete problem signals (errors, how-to-do-X, config, integration, migration).")
md.append("")
md.append(f"**Total pain keywords found:** {len(all_pains):,}")
md.append("")

# === Top global pain points (priority article candidates) ===
md.append("## Top 50 pain-point keywords (across all libs, by volume × boost)")
md.append("")
md.append("Sort = `volume × boost` (boost: errors/crashes=3, how-to/config/integration=2, comparison=1).")
md.append("Pick the top of this list to write articles that ship traffic fast.")
md.append("")
md.append("| # | Lib | Keyword | Vol | KD | Category | Suggested article |")
md.append("|---|-----|---------|----:|---:|----------|-------------------|")
for i, (display, slug, kw, vol, kd, cat, boost) in enumerate(all_pains[:50], 1):
    # Suggest an article title from the keyword
    title = f"How to fix `{kw}` in {display}" if cat == "errors / fixes" else \
            f"{display}: {kw}" if kw.startswith("how to") else \
            f"{display} — {kw} step by step"
    md.append(f"| {i} | {display} | `{kw}` | {vol:,} | {kd} | {cat} | {title} |")
md.append("")

# === Per-lib breakdown ===
md.append("## Pain points per library")
md.append("")
md.append("Only libs with ≥1 pain-point keyword shown. For each lib: top 10 by volume.")
md.append("")
for slug, display, terms in LIBS:
    pains = per_lib_pains.get(slug, [])
    if not pains:
        continue
    pains.sort(key=lambda e: e[3], reverse=True)
    total_pain_vol = sum(p[3] for p in pains)
    md.append(f"### {display} — {len(pains)} pain kws, {total_pain_vol:,} mo. volume")
    md.append("")
    md.append("| Keyword | Vol | KD | Category |")
    md.append("|---------|----:|---:|----------|")
    for _, _, kw, vol, kd, cat, _ in pains[:10]:
        md.append(f"| `{kw}` | {vol:,} | {kd} | {cat} |")
    md.append("")

# === Category roll-up ===
cat_totals = defaultdict(lambda: [0, 0])  # category -> [count, total_vol]
for _, _, _, vol, _, cat, _ in all_pains:
    cat_totals[cat][0] += 1
    cat_totals[cat][1] += vol
md.append("## Pain category roll-up")
md.append("")
md.append("| Category | Keyword count | Total mo. volume |")
md.append("|----------|--------------:|-----------------:|")
for cat, (n, vol) in sorted(cat_totals.items(), key=lambda x: x[1][1], reverse=True):
    md.append(f"| {cat} | {n:,} | {vol:,} |")
md.append("")

OUT_FILE.write_text("\n".join(md))
print(f"Wrote {OUT_FILE}")
print(f"Total pain keywords: {len(all_pains):,}")
print(f"Libs with pain: {sum(1 for v in per_lib_pains.values() if v)}/{len(LIBS)}")
