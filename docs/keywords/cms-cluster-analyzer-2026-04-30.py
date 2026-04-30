"""
Find article opportunities NOT yet covered by:
  - Phase 1 (10 pillars)
  - Tier 1+2 backlog (22 ideas)
Filter: vol >= 80, KD <= 30
"""
import csv, re, os
from collections import defaultdict

# Already proposed/shipped — match by keyword fragment
ALREADY = [
    # Phase 1 pillars
    'how to fix and customize bitrix', 'how to fix magento 2', 'how to fix joomla',
    'how to fix prestashop', 'how to fix shopware', 'how to fix and improve wordpress',
    'how to fix opencart', 'how to fix and customize cs-cart', 
    'how to fix and customize shop-script', 'how to fix drupal',
    # Existing /vibers/ articles
    'critical error', 'database connection', 'hide header in elementor',
    'remove powered by astra', 'duplicate page', 'wordpress 6.9 broke',
    'disable comments', 'wordpress emergency', 'fix-and-improve',
    'edit anything in opencart', 'fix-woocommerce-checkout-slow',
    # Tier 1/2 backlog already proposed
    'magento seo expert', 'magento seo agency', 'magento seo consultant',
    'magento vs shopify', 'drupal vs wordpress', 'wordpress vs drupal',
    'hire drupal developer', 'hire opencart developer',
    'shopware vs shopify', 'cost of shopware 6', 'magento shopware migration',
    'prestashop stripe double charge', 'collasable info wordpress',
    'wordpress security news', 'wordpress seo services', 'wordpress multisite',
    'magento development services', 'drupal development services',
    'wordpress multisite vs drupal', 'black friday shopware',
    'joomla: extension seaching', 'joomla: how to find all form errors',
    'joomla 3: change footer info', 'prestashop update assistant',
    'тарифы битрикс 24', 'битрикс резервное копирование', 'битрикс бэкап',
    # Generic patterns to deprioritize (commercial NAV, branded)
    'localhost', 'wp-admin url', 'wordpress.com', 'wordpress.org',
]

CSVS = [
    ('wordpress', '/root/vibers/docs/keywords/wordpress_broad-match_us_2026-04-24.csv'),
    ('magento',   '/root/vibers/docs/keywords/magento_broad-match_us_2026-04-30.csv'),
    ('joomla',    '/root/vibers/docs/keywords/joomla_broad-match_us_2026-04-30.csv'),
    ('drupal',    '/root/vibers/docs/keywords/drupal_broad-match_us_2026-04-30.csv'),
    ('prestashop','/root/vibers/docs/keywords/prestashop_broad-match_us_2026-04-30.csv'),
    ('opencart',  '/root/vibers/docs/keywords/opencart_broad-match_us_2026-04-30.csv'),
    ('shopware',  '/root/vibers/docs/keywords/shopware_broad-match_us_2026-04-30.csv'),
    ('cs-cart',   '/root/vibers/docs/keywords/cs-cart_broad-match_us_2026-04-30.csv'),
    ('webasyst',  '/root/vibers/docs/keywords/shop-script_broad-match_ru_2026-04-30.csv'),
    ('bitrix',    '/root/vibers/docs/keywords/битрикс_broad-match_ru_2026-04-30.csv'),
]

# Theme-bucket signals to group missed topics
BUCKETS = [
    ('how-to-tutorial',     [r'^how to ', r' tutorial$', r'^how do ', r'guide$', r'^create ', r'^add ', r'^build ', r'^make ']),
    ('hosting-recommend',   [r'\bhost', r'managed (?:hosting|wp)']),
    ('plugin-themes-best',  [r'\bbest \w+ (?:plugin|theme|template|extension|module)', r'top \w+ (?:plugin|theme)', r'free \w+ (?:plugin|theme)']),
    ('specific-vendor-bug', [r'\b(?:elementor|divi|astra|avada|generatepress|kadence|wpforms|yoast|wpml|woocommerce|gravity ?forms|contact form 7|jetpack|wp rocket|w3 total cache|litespeed|all in one wp|advanced custom fields|acf|gutenberg)\b']),
    ('migration-from',      [r'(?:migrate|migration|move|switch) (?:from |to )', r'\bto wordpress\b', r'\bto shopify\b', r'\bto bigcommerce\b']),
    ('upgrade-version',     [r'\bupgrade\b', r'\b(?:[0-9]\.[0-9]+|to [0-9]+)\b', r'update to', r'обновить', r'обновлен']),
    ('compare-vs',          [r'\bvs\b', r'\bversus\b', r'compare']),
    ('payment-gateway',     [r'\bpaypal\b', r'\bstripe\b', r'\bsquare\b', r'\bauthorize\.net\b', r'\bpayment\b', r'оплат', r'юmoney', r'sbp']),
    ('captcha-spam',        [r'captcha', r'recaptcha', r'спам', r'spam']),
    ('seo-meta',            [r'\bseo\b', r'sitemap', r'robots\.?txt', r'\bschema\b', r'meta keywords', r'meta description', r'noindex', r'canonical']),
    ('multilang-translate', [r'multilang', r'translation', r'translate', r'\bwpml\b', r'\bpolylang\b', r'перевод']),
    ('backup-restore',      [r'backup', r'restore', r'бэкап', r'резервн']),
    ('speed-perf',          [r'\bslow\b', r'\bspeed\b', r'optimization', r'optimize', r'cache', r'медленн', r'performance']),
    ('security-hack',       [r'\bhack\b', r'malware', r'vulnerab', r'\bsecurity\b', r'взлом', r'вирус']),
    ('admin-login',         [r'\blogin\b', r'admin password', r'2fa', r'two-factor', r'wp-login']),
    ('checkout-cart',       [r'\bcheckout\b', r'cart abandon', r'shopping cart']),
    ('product-catalog',     [r'\bproduct\b', r'catalog', r'category page']),
    ('email-newsletter',    [r'newsletter', r'mailchimp', r'email subscribe']),
    ('search-functionality',[r'\bsearch\b', r'autocomplete', r'live search', r'search bar', r'поиск']),
    ('forms-contact',       [r'contact form', r'contact page', r'\bform\b', r'форма']),
    ('child-theme',         [r'child theme', r'parent theme', r'дочерн']),
    ('woocommerce',         [r'\bwoocommerce\b', r'\bwoo\b']),
    ('error-fatal',         [r'fatal', r'\b500\b', r'\b502\b', r'\b504\b', r'white screen', r'wsod', r'critical error', r'крит']),
    ('hide-remove',         [r'\bhide\b', r'\bremove\b', r'\bdisable\b', r'powered by', r'удалить', r'скрыть']),
    ('developer-hire',      [r'\bhire\b', r'\bfreelancer\b', r'\bdeveloper\b', r'\bagency\b', r'разработч', r'фрилансер']),
    ('cost-pricing',        [r'\bcost\b', r'\bprice\b', r'pricing', r'how much does', r'цена', r'стоимость']),
]

def is_already(kw):
    k = kw.lower()
    return any(a in k for a in ALREADY)

def bucket(kw):
    out = []
    for name, pats in BUCKETS:
        if any(re.search(p, kw, re.IGNORECASE) for p in pats):
            out.append(name)
    return out or ['general']

def load(path):
    if not os.path.exists(path): return []
    rows = []
    for r in csv.DictReader(open(path)):
        kw = r.get('Keyword','').strip()
        if not kw or 'http' in kw.lower() or '.com' in kw.lower(): continue
        if 'magenta' in kw.lower(): continue
        try: vol = int(r.get('Volume') or 0)
        except: vol = 0
        try: kd = int(r.get('Keyword Difficulty') or 999)
        except: kd = 999
        intent = r.get('Intent','')
        rows.append((kw, vol, kd, intent))
    return rows

# Per CMS: find missed buckets with strong volume potential
for cms, path in CSVS:
    rows = load(path)
    candidates = [(kw, vol, kd, intent) for kw, vol, kd, intent in rows
                  if vol >= 80 and kd <= 30 and not is_already(kw)
                  and not (intent.startswith('Navigational') and len(kw.split()) <= 2)]
    
    by_bucket = defaultdict(list)
    for kw, v, kd, intent in candidates:
        for b in bucket(kw):
            by_bucket[b].append((v, kd, kw, intent))
    
    # Score buckets by total top-10 volume of unique candidates
    scored = []
    for b, items in by_bucket.items():
        items.sort(key=lambda x: -x[0])
        # dedupe by stem (first 3 keyword tokens)
        seen = set()
        unique = []
        for it in items:
            sig = ' '.join(it[2].lower().split()[:3])
            if sig in seen: continue
            seen.add(sig); unique.append(it)
        top10v = sum(v for v,_,_,_ in unique[:10])
        scored.append((top10v, b, unique[:8]))
    scored.sort(reverse=True)
    
    print(f"\n{'='*78}\n# {cms.upper()} — {len(candidates)} missed candidates (vol≥80, KD≤30, not in backlog)\n{'='*78}")
    for top10v, b, items in scored[:7]:
        if top10v < 200 or not items: continue
        print(f"\n  ◆ {b:<22} | top10 vol = {top10v}")
        for v, kd, kw, intent in items[:5]:
            print(f"      {v:>5} | KD={kd:>2} | {kw[:75]}")
