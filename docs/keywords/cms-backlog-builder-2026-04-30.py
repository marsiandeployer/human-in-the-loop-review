"""
Build full article backlog table.
For each missed cluster, propose specific article(s) with: slug, title, target KW.
"""
import csv, re, os, json
from collections import defaultdict

# Sources
CSVS = [
    ('wordpress', '/root/vibers/docs/keywords/wordpress_broad-match_us_2026-04-24.csv'),
    ('magento',   '/root/vibers/docs/keywords/magento_broad-match_us_2026-04-30.csv'),
    ('joomla',    '/root/vibers/docs/keywords/joomla_broad-match_us_2026-04-30.csv'),
    ('drupal',    '/root/vibers/docs/keywords/drupal_broad-match_us_2026-04-30.csv'),
    ('prestashop','/root/vibers/docs/keywords/prestashop_broad-match_us_2026-04-30.csv'),
    ('opencart',  '/root/vibers/docs/keywords/opencart_broad-match_us_2026-04-30.csv'),
    ('shopware',  '/root/vibers/docs/keywords/shopware_broad-match_us_2026-04-30.csv'),
    ('bitrix',    '/root/vibers/docs/keywords/битрикс_broad-match_ru_2026-04-30.csv'),
]

def load(path):
    if not os.path.exists(path): return {}
    out = {}
    for r in csv.DictReader(open(path)):
        kw = r.get('Keyword','').strip()
        if not kw: continue
        try: vol = int(r.get('Volume') or 0)
        except: vol = 0
        try: kd = int(r.get('Keyword Difficulty') or 999)
        except: kd = 999
        out[kw.lower()] = (vol, kd, r.get('Intent',''))
    return out

KW = {cms: load(p) for cms, p in CSVS}

def find(cms, kw):
    return KW.get(cms, {}).get(kw.lower(), (0, 999, ''))

# Static, hand-curated full backlog ─ structured by tier × CMS
# Format: (tier, cms, slug, title, target_kw, [related_kws], note)
backlog = [
    # ============================================================
    # TIER 0 — already shipped (Phase 1)
    # ============================================================
    (0, 'bitrix',     'how-to-fix-and-customize-bitrix-sites',     '✓ shipped', 'править битрикс', [], 'Phase 1'),
    (0, 'magento',    'how-to-fix-magento-2-issues',               '✓ shipped', 'fix magento 2', [], 'Phase 1'),
    (0, 'joomla',     'how-to-fix-joomla-issues',                  '✓ shipped', 'fix joomla', [], 'Phase 1'),
    (0, 'prestashop', 'how-to-fix-prestashop-issues',              '✓ shipped', 'fix prestashop', [], 'Phase 1'),
    (0, 'shopware',   'how-to-fix-shopware-6-issues',              '✓ shipped', 'fix shopware 6', [], 'Phase 1'),
    (0, 'wordpress',  'how-to-fix-and-improve-wordpress-sites',    '✓ shipped pillar', 'fix wordpress', [], 'Phase 1'),
    (0, 'opencart',   'how-to-fix-opencart-issues',                '✓ shipped', 'fix opencart', [], 'Phase 1'),
    (0, 'cs-cart',    'how-to-fix-and-customize-cs-cart',          '✓ shipped', 'fix cs-cart', [], 'Phase 1'),
    (0, 'webasyst',   'how-to-fix-and-customize-shop-script',      '✓ shipped', 'shop-script', [], 'Phase 1'),
    (0, 'drupal',     'how-to-fix-drupal-issues',                  '✓ shipped', 'fix drupal', [], 'Phase 1'),

    # ============================================================
    # TIER 1 — quick wins (KD ≤ 15, vol ≥ 200) — ~1-2 days, ship next
    # ============================================================
    (1, 'wordpress', 'wordpress-collapsible-info-block-tutorial', 'Add a Collapsible Info Block to WordPress Forms', 'collasable info wordpress forms', [], 'KD 5, opportunity gap'),
    (1, 'wordpress', 'how-to-make-clickable-phone-number-wordpress', 'How to Make a Clickable Phone Number in WordPress', 'how to make a clickable phone number wordpress', [], 'KD 14'),
    (1, 'magento', 'magento-seo-services-without-agency', 'Magento SEO Without an Agency Retainer', 'magento seo expert', ['magento seo consultant', 'magento seo agency', 'magento seo services'], 'KD 4-11'),
    (1, 'magento', 'magento-vs-shopify-stay-or-leave', 'Magento vs Shopify: Stay-or-Leave Decision Guide', 'magento vs shopify', ['shopify vs magento'], 'KD 12-14'),
    (1, 'magento', 'magento-1-to-2-migration-playbook', 'Magento 1 → 2 Migration: The 2026 Playbook', 'magento migration from 1 to 2', ['magento upgrade service', 'magento 2 upgrade service'], 'KD 8-15'),
    (1, 'magento', 'magento-to-shopify-migration-when-to-do-it', 'Magento → Shopify Migration: When (Not) to Do It', 'magento to shopify migration', ['migrate from magento to shopify'], 'KD 9-26'),
    (1, 'drupal', 'drupal-vs-wordpress-honest-tradeoffs', 'Drupal vs WordPress: Honest Tradeoffs (2026)', 'drupal vs wordpress', ['wordpress vs drupal', 'drupal versus wordpress'], 'KD 20-22'),
    (1, 'drupal', 'hire-drupal-developer-or-use-simplereview', 'Hire a Drupal Developer or Use SimpleReview?', 'hire drupal developer', ['hire drupal developers', 'hire dedicated drupal developer'], 'KD 0-5 — easy win'),
    (1, 'drupal', 'wordpress-multisite-vs-drupal-multisite', 'WordPress Multisite vs Drupal Multisite — Pros & Cons', 'wordpress multisite vs drupal multisite comparison pros cons', [], 'KD 0!'),
    (1, 'drupal', 'drupal-vs-sitecore', 'Drupal vs Sitecore: Open-Source vs Enterprise DXP', 'drupal vs sitecore', [], 'KD 0!'),
    (1, 'drupal', 'drupal-7-eol-migration-path', 'Drupal 7 EOL: Your Migration Path to Drupal 10/11', 'drupal 7 to 10 migration', ['drupal upgrade status'], 'KD 16-21'),
    (1, 'opencart', 'hire-opencart-developer-vs-no-code-fix', 'Hire OpenCart Developer or Use SimpleReview?', 'hire opencart developer', ['hire opencart developers', 'hire dedicated opencart developers'], 'KD 0-5 — almost empty SERP'),
    (1, 'opencart', 'opencart-meta-keywords-guide', 'OpenCart Meta Keywords: SEO Guide for 3.x and 4.x', 'opencart meta keywords', ['meta keywords opencart', 'meta tag keywords opencart', 'what is seo keyword in opencart'], 'KD 11-14'),
    (1, 'shopware', 'shopware-vs-shopify-honest-comparison', 'Shopware 6 vs Shopify: Honest Comparison', 'shopware vs shopify', ['shopify vs shopware'], 'KD 0-4'),
    (1, 'shopware', 'cost-of-shopware-6-real-numbers', 'Cost of Shopware 6 in 2026 — Real Numbers', 'cost of shopware 6', ['shopware pricing', 'shopware 6 pricing'], 'KD 16'),
    (1, 'shopware', 'magento-to-shopware-migration-guide', 'Magento → Shopware Migration Guide', 'magento shopware migration', ['shopware magento migration'], 'KD 2-9 — very easy'),
    (1, 'shopware', 'shopware-agentur-oder-simplereview', 'Shopware Agentur oder SimpleReview? (DE)', 'shopware agentur', ['shopware agency', 'shopware development agency', 'shopware seo agentur'], 'KD 1-10 — DE market'),
    (1, 'prestashop', 'prestashop-stripe-double-charge-fix', 'Fix the PrestaShop Stripe Double-Charge Bug', 'prestashop stripe double charge', [], 'KD 15 — specific bug'),
    (1, 'prestashop', 'prestashop-vs-bigcommerce', 'PrestaShop vs BigCommerce', 'prestashop vs bigcommerce', [], 'KD 5'),
    (1, 'prestashop', 'prestashop-vs-wordpress-when-each-wins', 'PrestaShop vs WordPress: When Each Wins', 'prestashop vs wordpress', [], 'KD 3'),
    (1, 'prestashop', 'prestashop-meta-keywords-guide', 'PrestaShop Meta Keywords: Are They Still Worth It?', 'prestashop meta keywords', [], 'KD 11'),
    (1, 'prestashop', 'hire-prestashop-developer-vs-simplereview', 'Hire PrestaShop Developer vs SimpleReview', 'hire prestashop developers', ['hire prestashop developer'], 'KD 6-11'),
    (1, 'joomla', 'joomla-extensions-search-errors-fix', 'Joomla Extension "Searching for Errors" — Diagnose & Fix', 'joomla: extension seaching for errors', [], 'KD 6, vol 2400!'),
    (1, 'joomla', 'joomla-form-errors-find-all', 'How to Find All Form Errors on a Joomla Site', 'joomla: how to find all form errors on a website', [], 'KD 7, vol 1900'),
    (1, 'joomla', 'joomla-3-change-footer-template-js-unlimited', 'Joomla 3: Change Footer Info in JS_Unlimited Template', 'joomla 3: change footer info in template js_unlimited', [], 'KD 9, vol 720'),
    (1, 'joomla', 'joomla-4-to-5-upgrade-extension-issues', 'Joomla 4 → 5 Upgrade: Extension Compatibility Fix', 'joomla 4 to joomla 5 upgade extension', [], 'KD 16, vol 880'),
    (1, 'joomla', 'joomla-imagick-php-module-not-loaded-fix', 'Fix "Imagick PHP Module Not Loaded" on Joomla 3', 'automatic intro image: imagick php module not loaded joomla 3', [], 'KD 16'),
    (1, 'joomla', 'hire-joomla-developer-vs-simplereview', 'Hire Joomla Developer or Use SimpleReview?', 'hire joomla developer', ['hire joomla developers', 'joomla developers for hire'], 'KD 3-5'),
    (1, 'bitrix', 'тарифы-битрикс-24-сравнение', 'Тарифы Битрикс 24: какой выбрать в 2026', 'тарифы битрикс 24', ['битрикс 24 тарифы', 'битрикс 24 цена'], 'KD 12-20 (RU)'),
    (1, 'bitrix', 'битрикс-резервное-копирование-полный-гид', 'Резервное копирование Битрикс — полный гид 2026', 'битрикс резервное копирование', ['битрикс бэкап сайта', 'битрикс развернуть бэкап', 'как сделать бэкап сайта битрикс'], 'KD 5-9 (RU)'),
    (1, 'bitrix', 'стоимость-разработки-битрикс-2026', 'Сколько стоит разработка на Битрикс в 2026', 'стоимость разработки интернет магазина на битрикс', ['создание сайта битрикс цена'], 'KD 9-23 (RU)'),

    # ============================================================
    # TIER 2 — pillar/comparison (KD 15-30, ~3-5 days)
    # ============================================================
    (2, 'wordpress', 'wordpress-development-services-buyer-guide', 'WordPress Development Services: Buyer\'s Guide 2026', 'wordpress development services', ['wordpress development agency', 'wordpress dev company'], 'KD 23, vol 3600'),
    (2, 'wordpress', 'wordpress-seo-services-vs-diy', 'WordPress SEO Services vs DIY (When to Hire)', 'wordpress seo services', ['wordpress seo agency', 'wordpress seo consultant'], 'KD 10-26, vol 1900-3600'),
    (2, 'wordpress', 'is-wordpress-multisite-one-theme-or-many', 'Is WordPress Multisite One Theme or Multiple?', 'is wordpress multisite one theme or multiple', [], 'KD 11, vol 1900'),
    (2, 'wordpress', 'clear-wordpress-cache-every-major-plugin', 'Clear WordPress Cache (Every Major Plugin)', 'clear wordpress cache', ['clear cache wordpress', 'wordpress clear cache', 'lscache for wordpress'], 'KD 20-28'),
    (2, 'wordpress', 'wordpress-speed-optimization-without-plugin', 'WordPress Speed Optimization Without a Plugin', 'wordpress speed optimization', [], 'KD 28'),
    (2, 'wordpress', 'wordpress-maintenance-what-to-actually-do', 'WordPress Maintenance: What to Actually Do', 'wordpress maintenance', [], 'KD 24, vol 2900'),
    (2, 'wordpress', 'squarespace-vs-wordpress-honest', 'Squarespace vs WordPress: Honest 2026 Comparison', 'squarespace vs wordpress', ['wordpress vs squarespace'], 'KD 21-24'),
    (2, 'wordpress', 'wix-vs-wordpress-honest', 'Wix vs WordPress: Real-World 2026 Comparison', 'wix vs wordpress', [], 'KD 28'),
    (2, 'wordpress', 'webflow-vs-wordpress-honest', 'Webflow vs WordPress: Designer\'s Comparison', 'webflow vs wordpress', [], 'KD 26'),
    (2, 'wordpress', 'shopify-vs-wordpress-for-ecommerce', 'Shopify vs WordPress for E-commerce', 'shopify vs wordpress', [], 'KD 24'),
    (2, 'magento', 'magento-vs-woocommerce-when-each-wins', 'Magento vs WooCommerce: When Each Wins', 'magento vs woocommerce', [], 'KD 25'),
    (2, 'magento', 'shopify-plus-vs-magento', 'Shopify Plus vs Magento (Adobe Commerce)', 'shopify plus vs magento', [], 'KD 16'),
    (2, 'magento', 'bigcommerce-vs-magento', 'BigCommerce vs Magento Open Source', 'bigcommerce vs magento', ['magento vs bigcommerce'], 'KD 15-24'),
    (2, 'magento', 'magento-development-services-checklist', 'Magento Development Services Buyer\'s Checklist', 'magento development services', ['magento agency', 'magento development agency'], 'KD 16-29'),
    (2, 'magento', 'magento-2-speed-optimization', 'Magento 2 Speed Optimization (No Agency)', 'magento performance optimization', ['magento speed optimization', 'magento 2 speed optimization'], 'KD 14-20'),
    (2, 'magento', 'magento-2-4-8-release-notes', 'Magento 2.4.8 Release Notes & Breaking Changes', 'magento 2.4.8', [], 'KD 23'),
    (2, 'drupal', 'drupal-development-services-buyer-guide', 'Drupal Development Services: Buyer\'s Guide', 'drupal development services', ['drupal agency', 'drupal development agency'], 'KD 20-30'),
    (2, 'drupal', 'drupal-vs-joomla-2026', 'Drupal vs Joomla in 2026', 'drupal vs joomla', ['joomla vs drupal'], 'KD 18-23'),
    (2, 'drupal', 'drupal-performance-optimization', 'Drupal Performance Optimization Without Acquia', 'drupal performance optimization', ['drupal cache', 'drupal performance'], 'KD 22-29'),
    (2, 'drupal', 'drupal-tutorial-zero-to-deploy', 'Drupal Tutorial: From Zero to Deployed Site', 'drupal tutorial', ['create website with drupal'], 'KD 21-24'),
    (2, 'joomla', 'joomla-seo-complete-guide', 'Joomla SEO: Complete 2026 Guide', 'joomla seo', ['seo joomla', 'best seo for joomla'], 'KD 18-27'),
    (2, 'joomla', 'joomla-sitemap-xml-setup', 'Joomla Sitemap.xml Setup (Built-in + Plugins)', 'joomla sitemap', ['sitemaps joomla'], 'KD 18-22'),
    (2, 'joomla', 'joomla-vs-wordpress-2026', 'Joomla vs WordPress: 2026 Comparison', 'joomla vs wordpress', ['wordpress vs joomla', 'joomla versus wordpress'], 'KD 22-30'),
    (2, 'joomla', 'best-joomla-hosting-2026', 'Best Joomla Hosting in 2026', 'best joomla hosting', ['free joomla hosting'], 'KD 18-20'),
    (2, 'joomla', 'yoast-seo-on-joomla', 'Yoast SEO on Joomla — Setup & Alternatives', 'yoast seo joomla', [], 'KD 23'),
    (2, 'prestashop', 'prestashop-seo-complete-guide', 'PrestaShop SEO: Complete 2026 Guide', 'prestashop seo', ['seo in prestashop'], 'KD 17-20'),
    (2, 'prestashop', 'prestashop-vs-woocommerce', 'PrestaShop vs WooCommerce: Which to Pick', 'prestashop vs woocommerce', ['woocommerce vs prestashop'], 'KD 16-26'),
    (2, 'prestashop', 'prestashop-advanced-search-setup', 'PrestaShop Advanced Search Setup', 'advanced search prestashop', ['prestashop advanced search', 'prestashop search engine'], 'KD 8-16'),
    (2, 'prestashop', 'agence-seo-prestashop-vs-simplereview', 'Agence SEO PrestaShop vs SimpleReview (FR)', 'agence seo prestashop', ['seo company prestashop', 'agence prestashop'], 'KD 0-23'),
    (2, 'opencart', 'opencart-vs-shopify-honest', 'OpenCart vs Shopify: Honest Comparison', 'opencart vs shopify', [], 'KD 5'),
    (2, 'opencart', 'opencart-vs-woocommerce', 'OpenCart vs WooCommerce', 'opencart vs woocommerce', ['woocommerce vs opencart'], 'KD 8-13'),
    (2, 'opencart', 'opencart-development-services-buyer-guide', 'OpenCart Development Services: Buyer\'s Guide', 'opencart development services', ['opencart development company'], 'KD 8-17'),
    (2, 'opencart', 'opencart-1-to-2-3-4-upgrade-paths', 'OpenCart 2 → 3 → 4 Upgrade Paths', 'upgrade opencart 2 to 3', ['opencart upgrade'], 'KD 4'),
    (2, 'shopware', 'shopware-development-company-guide', 'Shopware Development Company: How to Pick', 'shopware development company', ['shopware development services'], 'KD 0-9'),
    (2, 'shopware', 'shopware-6-demo-walkthrough', 'Shopware 6 Demo Walkthrough — What to Look At', 'shopware 6 demo', [], 'KD 8'),
    (2, 'shopware', 'magento-vs-shopware-pick-one', 'Magento vs Shopware: Which Open-Source Stack?', 'magento vs shopware', ['shopware vs magento', 'shopware vs woocommerce'], 'KD 4-9'),
    (2, 'bitrix', 'bitrix-разработчик-vs-simplereview', 'Битрикс разработчик vs SimpleReview', 'битрикс разработчик', ['программист 1с битрикс'], 'KD 12-24 (RU)'),
    (2, 'bitrix', 'настройка-битрикс-24-полный-гид', 'Настройка Битрикс 24 — полный гид 2026', 'настройка битрикс 24', ['битрикс настройка поиска', 'битрикс 24 настройка роботов', 'битрикс настройка регистрации пользователей'], 'KD 7-25 (RU)'),

    # ============================================================
    # TIER 3 — programmatic / release-notes (Google March 2026 risk)
    # ============================================================
    (3, 'wordpress', 'wordpress-6-8-2-release-notes', 'WordPress 6.8.2 Release Notes — What Changed', 'wordpress 6.8.2', [], 'Programmatic candidate, KD 4'),
    (3, 'wordpress', 'wordpress-6-8-1-release-notes', 'WordPress 6.8.1 Release Notes & PHP Compat', 'wordpress 6.8.1', ['wordpress 6.8.1 php version'], 'KD 8-24'),
    (3, 'wordpress', 'wordpress-6-7-release-news-recap', 'WordPress 6.7: Release News Recap', 'wordpress 6.7 release news', [], 'KD 30, vol 4400 — careful, scaled abuse risk'),
    (3, 'wordpress', 'wordpress-security-news-monthly-digest', 'WordPress Security Digest — Monthly CVE Roundup', 'wordpress security news', ['wordpress vulnerability news'], 'KD 18-35, programmatic — needs original data'),
    (3, 'drupal', 'drupal-7-100-release-notes', 'Drupal 7.100 Release Notes — What Changed', 'drupal 7.100 release notes', [], 'KD 26'),
    (3, 'drupal', 'drupal-security-news-monthly', 'Drupal Security Advisory — Monthly Digest', 'drupal security news', ['drupal security advisory'], 'KD 33-44'),
]

# Render markdown
print("# Full article backlog (Phase 1 + missed-from-30K analysis)\n")
print("Source data: 9 Semrush CSVs in `docs/keywords/` (8 from 2026-04-30 + WP from 2026-04-24).")
print("Filter: vol ≥ 80, KD ≤ 30, deduplicated by topic-bucket.\n")

# Tier 0
t0 = [b for b in backlog if b[0]==0]
print(f"## ✅ Tier 0 — shipped in c2c6c46 ({len(t0)} articles)\n")
print("| CMS | Slug |")
print("|-----|------|")
for _, cms, slug, *_ in t0:
    print(f"| {cms} | `{cms}/{slug}/` |")

# Tier 1
t1 = [b for b in backlog if b[0]==1]
print(f"\n## 🟢 Tier 1 — quick wins ({len(t1)} articles, KD ≤ 15-25)\n")
print("Cost: ~1-2 days. Target: ship-then-measure.\n")
print("| ☐ | CMS | Slug | Title | Target KW | Vol | KD | Note |")
print("|---|-----|------|-------|-----------|----:|---:|------|")
for tier, cms, slug, title, kw, related, note in t1:
    v, kd, _ = find(cms, kw)
    print(f"| ☐ | {cms} | `{slug}` | {title} | `{kw}` | {v or '—'} | {kd if kd != 999 else '—'} | {note} |")

# Tier 2
t2 = [b for b in backlog if b[0]==2]
print(f"\n## 🟡 Tier 2 — pillar/comparison ({len(t2)} articles, KD 15-30)\n")
print("Cost: ~3-5 days. Target: pillar pages + service-intent CRO.\n")
print("| ☐ | CMS | Slug | Title | Target KW | Vol | KD | Note |")
print("|---|-----|------|-------|-----------|----:|---:|------|")
for tier, cms, slug, title, kw, related, note in t2:
    v, kd, _ = find(cms, kw)
    print(f"| ☐ | {cms} | `{slug}` | {title} | `{kw}` | {v or '—'} | {kd if kd != 999 else '—'} | {note} |")

# Tier 3
t3 = [b for b in backlog if b[0]==3]
print(f"\n## 🔴 Tier 3 — programmatic / release-notes ({len(t3)} articles)\n")
print("⚠ Google March 2026 Core Update пенализит scaled-content abuse. Каждая статья должна нести Information Gain (original timing data, breaking-change summary, our own benchmarks). Без этого — не публиковать.\n")
print("| ☐ | CMS | Slug | Title | Target KW | Vol | KD |")
print("|---|-----|------|-------|-----------|----:|---:|")
for tier, cms, slug, title, kw, related, note in t3:
    v, kd, _ = find(cms, kw)
    print(f"| ☐ | {cms} | `{slug}` | {title} | `{kw}` | {v or '—'} | {kd if kd != 999 else '—'} |")

print(f"\n## Summary\n")
print(f"- Tier 0 (shipped): **{len(t0)}**")
print(f"- Tier 1 (quick wins): **{len(t1)}**")
print(f"- Tier 2 (pillars): **{len(t2)}**")
print(f"- Tier 3 (programmatic, risky): **{len(t3)}**")
print(f"- **Total backlog: {len(t1)+len(t2)+len(t3)} new articles**\n")
print("## Что ещё НЕ покрыто (tail/long-tail)\n")
print("Узкие сиды Semrush + Yandex Wordstat не запускались — даст ещё ~20-30 идей в категориях:")
print("- Specific bug fixes (vol 30-80 диапазон): `magento setup:upgrade memory exhausted`, etc.")
print("- Russian Wordstat data для Bitrix/Webasyst — semrush ru db даёт thin coverage")
print("- Локализованные DE/FR/ES сайты для shopware/prestashop")
print("- Plugin/extension-specific bugs (`elementor`, `divi`, `astra`, `yoast`)")
