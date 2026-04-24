#!/usr/bin/env python3
"""Aggregate Haiku verdict batches → cluster → ranked report."""
import json, glob, re, os, sys
from collections import defaultdict

COVERED_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'covered-keywords.txt')

def load_covered():
    if not os.path.exists(COVERED_PATH):
        return set()
    with open(COVERED_PATH) as f:
        return {l.strip().lower() for l in f if l.strip() and not l.startswith('#')}

def cluster_root(kw):
    kw = kw.lower()
    kw = re.sub(r'\bwordpress\b', '', kw)
    kw = re.sub(r'\b(how to|the|a|an|on|in|for|to|from|of|my|your|website|site|blog|been|has|there|this|that|is|are|with|and|or|com|org|using|do|i|you|can)\b', '', kw)
    # Light stemming: drop trailing s
    tokens = sorted({re.sub(r's$', '', t) for t in re.findall(r'\w+', kw)})
    return ' '.join(tokens)

# Load all verdicts
all_kw = []
for f in sorted(glob.glob('/tmp/kw_verdict_*.json')):
    with open(f) as fh:
        all_kw.extend(json.load(fh))

print(f"# SimpleReview Keyword Opportunities (Haiku-scored)\n", flush=True)
print(f"Total keywords scored: {len(all_kw)}", flush=True)

# Score distribution
dist = defaultdict(int)
for k in all_kw:
    dist[k.get('score', 0)] += 1
print(f"\nScore distribution: " + " ".join(f"{s}={dist[s]}" for s in sorted(dist.keys())))

# Keep score ≥ 2
candidates = [k for k in all_kw if k.get('score', 0) >= 2]
print(f"Candidates with score ≥ 2: {len(candidates)}\n")

# Cluster
covered = load_covered()
covered_token_sets = [set(re.findall(r'\w+', cluster_root(c))) for c in covered]

clusters = defaultdict(list)
for k in candidates:
    clusters[cluster_root(k['kw'])].append(k)

cluster_list = []
for root, members in clusters.items():
    members.sort(key=lambda x: -x['vol'])
    primary = members[0]
    primary_tokens = set(re.findall(r'\w+', root))
    if not primary_tokens:
        continue
    skip = False
    for cov_t in covered_token_sets:
        if not cov_t: continue
        inter = len(primary_tokens & cov_t)
        m = min(len(primary_tokens), len(cov_t))
        if m and inter / m >= 0.6:
            skip = True; break
    if skip: continue
    total_vol = sum(m['vol'] for m in members)
    max_score = max(m['score'] for m in members)
    min_kd = min(m['kd'] for m in members)
    # Composite: volume × max_score × (1 / sqrt(kd))
    rank_score = total_vol * max_score / (min_kd ** 0.5)
    cluster_list.append({
        'primary': primary['kw'],
        'angle': primary.get('angle', ''),
        'total_vol': total_vol,
        'max_score': max_score,
        'min_kd': min_kd,
        'rank_score': rank_score,
        'variants': [m['kw'] for m in members[:5]],
        'count': len(members),
    })

cluster_list.sort(key=lambda x: -x['rank_score'])

print(f"Fresh clusters (after dedup): {len(cluster_list)}\n")
print("| # | Primary keyword | Angle | Vol | KD | Score | Variants |")
print("|---|---|---|---|---|---|---|")
for i, c in enumerate(cluster_list[:40], 1):
    slug = re.sub(r'[^a-z0-9]+', '-', c['primary'].lower()).strip('-')[:60]
    variants = '<br>'.join(c['variants'][:3])
    print(f"| {i} | **{c['primary']}**<br>`{slug}` | {c['angle']} | {c['total_vol']} | {c['min_kd']} | {c['max_score']} | {variants} ({c['count']}) |")
