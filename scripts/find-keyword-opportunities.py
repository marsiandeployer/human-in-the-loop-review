#!/usr/bin/env python3
"""Find SEO keyword opportunities from Semrush CSV.

Usage: python3 find-keyword-opportunities.py docs/keywords/wordpress_broad-match_us_2026-04-24.csv
"""
import csv, re, sys, os
from collections import defaultdict

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else 'docs/keywords/wordpress_broad-match_us_2026-04-24.csv'
COVERED_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'covered-keywords.txt')

# Pattern → multiplier
PATTERNS = [
    (3.0, [
        r'^there has been a critical error',
        r'^error establishing database',
        r'briefly unavailable for scheduled maintenance',
        r'memory exhausted',
        r'^http error',
    ]),
    (2.5, [
        r'^how to (fix|repair|recover|restore|debug|troubleshoot)',
        r'^(fix|repair|recover|restore) wordpress',
        r'wordpress .* (not working|broken|crashed|fails?|error|issues?|problems?|stuck|hangs?)',
        r'wordpress .* (won\'t|wont|can\'t|cant|doesn\'t|doesnt) (load|work|open|update|save)',
    ]),
    (2.0, [
        r'^how to (disable|remove|delete|hide|stop|turn off)',
        r'^(disable|remove|delete|hide|stop|turn off) wordpress',
        r'wordpress (disable|remove|delete|hide|stop|turn off)',
    ]),
    (1.5, [
        r'^how to (change|update|reset|edit|modify|customize|migrate)',
        r'^(change|update|reset) wordpress',
        r'wordpress (change|update|reset|migrate)',
        r'wordpress .* (slow|down|loading)',
    ]),
    (1.0, [
        r'^how to (add|install|setup|configure|enable|create|make)',
        r'^(add|install|setup) .* wordpress',
    ]),
]

# Hard exclude — never recommend
EXCLUDE = [
    r'\b(news|blog|podcast|release|announcement)\b',
    r'\b(best|top \d|vs\b|versus)\b',
    r'\b(price|pricing|cost|cheap|free)\b',
    r'\b(hosting|domain)\b',
    r'\b(tutorial|course|learn|beginner|guide)\b(?!.*(error|fix|broken))',
    r'\b(theme|plugin|template)s?\s*(free|download|list)',
    r'\bwordpress\s*$',  # just "wordpress"
    r'^wordpress (com|org|website|site|blog|news)$',
]

def load_covered():
    if not os.path.exists(COVERED_PATH):
        return set()
    with open(COVERED_PATH) as f:
        return {line.strip().lower() for line in f if line.strip() and not line.startswith('#')}

def cluster_root(kw):
    """Return canonical root for clustering similar keywords."""
    # Strip common stopwords and reorder
    kw = re.sub(r'\bwordpress\b', '', kw)
    kw = re.sub(r'\b(how to|the|a|an|on|in|for|to|from|of|my|your|website|site|blog|been|has|there|this|that|is|are|been|with|and|or|com|org|using)\b', '', kw)
    kw = re.sub(r'\s+', ' ', kw).strip()
    # Sort tokens for clustering similar phrases
    tokens = sorted(set(re.findall(r'\w+', kw)))
    return ' '.join(tokens)

def score_keyword(kw):
    kw_l = kw.lower()
    for excl in EXCLUDE:
        if re.search(excl, kw_l):
            return 0.0
    for mult, patterns in PATTERNS:
        for p in patterns:
            if re.search(p, kw_l):
                return mult
    return 0.0

def main():
    covered = load_covered()
    rows = []
    with open(CSV_PATH) as f:
        for r in csv.DictReader(f):
            try:
                vol = int(r['Volume'])
                kd = int(r['Keyword Difficulty']) if r['Keyword Difficulty'] else 100
            except ValueError:
                continue
            if r['Intent'] != 'Informational' or kd > 25 or kd < 1 or vol < 100:
                continue
            mult = score_keyword(r['Keyword'])
            if mult == 0:
                continue
            rows.append({
                'kw': r['Keyword'],
                'vol': vol, 'kd': kd, 'cpc': r['CPC (USD)'],
                'score': vol * mult,
                'mult': mult,
            })

    # Cluster
    clusters = defaultdict(list)
    for row in rows:
        clusters[cluster_root(row['kw'])].append(row)

    # Build cluster summary
    covered_token_sets = [set(re.findall(r'\w+', cluster_root(c))) for c in covered]
    cluster_list = []
    for root, members in clusters.items():
        members.sort(key=lambda x: -x['vol'])
        primary = members[0]['kw']
        # Skip if covered: Jaccard similarity ≥ 0.6 OR covered tokens ⊆ primary tokens
        primary_tokens = set(re.findall(r'\w+', cluster_root(primary)))
        if not primary_tokens:
            continue
        skip = False
        for cov_tokens in covered_token_sets:
            if not cov_tokens:
                continue
            inter = len(primary_tokens & cov_tokens)
            min_len = min(len(primary_tokens), len(cov_tokens))
            containment = inter / min_len if min_len else 0
            if containment >= 0.6:
                skip = True; break
        if skip:
            continue
        cluster_list.append({
            'primary': primary,
            'total_vol': sum(m['vol'] for m in members),
            'min_kd': min(m['kd'] for m in members),
            'max_score': max(m['score'] for m in members),
            'variants': [m['kw'] for m in members[:5]],
            'count': len(members),
        })

    cluster_list.sort(key=lambda x: -x['max_score'])

    print(f"# Keyword Opportunities ({CSV_PATH})\n")
    print(f"Total clusters: {len(cluster_list)} (covered filtered: {len(covered)})\n")
    print("| # | Primary keyword | Cluster vol | Min KD | Variants | Score |")
    print("|---|---|---|---|---|---|")
    for i, c in enumerate(cluster_list[:30], 1):
        slug = re.sub(r'[^a-z0-9]+', '-', c['primary'].lower()).strip('-')
        variants = '<br>'.join(c['variants'][:3])
        print(f"| {i} | **{c['primary']}**<br>`{slug}` | {c['total_vol']} | {c['min_kd']} | {variants} ({c['count']}) | {int(c['max_score'])} |")

if __name__ == '__main__':
    main()
