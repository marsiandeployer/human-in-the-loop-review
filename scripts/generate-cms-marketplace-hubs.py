#!/usr/bin/env python3
"""Create researched SimpleReview CMS marketplace hubs.

This is for the top-level /cms/ announcement pages only. It is intentionally
not a deep-article generator: deep SEO pages still need per-topic research.
"""

from __future__ import annotations

import html
from pathlib import Path
from string import Template


ROOT = Path("/root/vibers")
DATE = "2026-05-02"


HUBS = [
    {
        "slug": "woocommerce",
        "name": "WooCommerce",
        "short": "Woo",
        "color": "#7f54b3",
        "marketplace": "Woo Marketplace",
        "audience": "WooCommerce store owners, agencies, and plugin maintainers",
        "headline": "Fix WooCommerce stores without waiting on the plugin agency",
        "sub": "Click the broken checkout, product template, shipping notice, or cart block. SimpleReview reads the WordPress theme and WooCommerce extension paths, then prepares a fix you can upload to the store.",
        "paths": "wp-content/plugins/woocommerce/, wp-content/themes/[theme]/woocommerce/, functions.php, theme.json",
        "can_fix": ["cart and checkout copy", "template overrides", "email text", "coupon display", "shipping notices", "theme CSS", "hook snippets", "block template issues"],
        "human": "payment gateways, subscription renewals, tax logic, order data, and migrations",
        "banner_url": "store.example.com/checkout/",
        "target": "checkout total mismatch",
        "comment": "fix Woo checkout total mismatch",
        "sources": [
            ("WooCommerce extension developer docs", "https://developer.woocommerce.com/docs/extensions/getting-started-extensions/"),
            ("Woo Marketplace developer docs", "https://developer.woocommerce.com/docs/woo-marketplace/"),
        ],
    },
    {
        "slug": "modx",
        "name": "MODX",
        "short": "MODX",
        "color": "#76a900",
        "marketplace": "MODX Extras",
        "audience": "MODX site owners, integrators, and Extras developers",
        "headline": "Fix MODX templates and Extras without turning every tweak into a ticket",
        "sub": "Select the broken chunk, TV output, snippet result, or manager layout. SimpleReview maps it to chunks, templates, snippets, plugins, and package files, then prepares a fix for upload.",
        "paths": "core/components/, assets/components/, chunks, snippets, templates, plugins",
        "can_fix": ["chunk markup", "template variables", "language strings", "snippet parameters", "FormIt labels", "manager copy", "CSS", "package docs"],
        "human": "custom Extras, access policies, multi-context routing, migrations, and payment logic",
        "banner_url": "modx.example.com/resources/42",
        "target": "broken FormIt validation message",
        "comment": "fix MODX form validation copy",
        "sources": [
            ("MODX Extras documentation", "https://docs.modx.com/current/en/extras/index"),
            ("MODX Community", "https://community.modx.com/"),
            ("Submit an Extra", "https://extras.modx.com/submit-extra"),
        ],
    },
    {
        "slug": "strapi",
        "name": "Strapi",
        "short": "Strapi",
        "color": "#4945ff",
        "marketplace": "Strapi Marketplace",
        "audience": "Strapi teams, Next.js agencies, and plugin developers",
        "headline": "Fix Strapi admin and content API issues without hand-debugging",
        "sub": "Click the broken collection view, plugin panel, API response, or content workflow. SimpleReview reads Strapi config, schemas, policies, routes, and plugin code before preparing a site-ready fix.",
        "paths": "src/api/, src/admin/, src/plugins/, config/, database/migrations/",
        "can_fix": ["admin copy", "content-type schemas", "policies", "routes", "plugin panels", "API labels", "permissions copy", "validation messages"],
        "human": "data migrations, auth logic, custom providers, production config, and plugin architecture",
        "banner_url": "cms.example.com/admin/content-manager",
        "target": "plugin panel throws null collectionTypes",
        "comment": "fix Strapi plugin null state",
        "sources": [
            ("Strapi 5 documentation", "https://docs.strapi.io/"),
            ("Submit a Strapi plugin", "https://strapi.io/marketplace/submit-plugin"),
        ],
    },
    {
        "slug": "directus",
        "name": "Directus",
        "short": "Directus",
        "color": "#6644ff",
        "marketplace": "Directus Marketplace",
        "audience": "Directus admins, data teams, and extension developers",
        "headline": "Fix Directus extensions and Studio workflows without blind edits",
        "sub": "Click the broken interface, module, operation, or Studio field. SimpleReview reads extension code and Directus configuration, then prepares the smallest safe fix for your Directus project.",
        "paths": "extensions/interfaces/, extensions/modules/, extensions/operations/, schema snapshots, flows",
        "can_fix": ["interface labels", "module panels", "flow operation copy", "extension props", "schema notes", "validation text", "admin UI spacing", "docs snippets"],
        "human": "schema migrations, permission models, data integrity, custom auth, and API security",
        "banner_url": "data.example.com/admin/content/articles",
        "target": "custom interface missing from Studio",
        "comment": "fix Directus interface registration",
        "sources": [
            ("Directus Marketplace docs", "https://docs.directus.io/user-guide/marketplace/overview"),
            ("Directus extension guides", "https://docs.directus.io/guides/extensions"),
            ("Directus Extensions Marketplace", "https://directus.io/extensions"),
        ],
    },
    {
        "slug": "craft-cms",
        "name": "Craft CMS",
        "short": "Craft",
        "color": "#e5422b",
        "marketplace": "Craft Plugin Store",
        "audience": "Craft CMS teams, Twig developers, and plugin vendors",
        "headline": "Fix Craft CMS Twig templates and plugin UX with a pull request",
        "sub": "Click the broken entry template, field layout, plugin setting, or front-end component. SimpleReview follows Craft's Twig and plugin conventions before preparing a fix.",
        "paths": "templates/, modules/, plugins/, config/project/, src/",
        "can_fix": ["Twig templates", "field instructions", "plugin copy", "control panel labels", "GraphQL docs", "module settings", "CSS", "project config notes"],
        "human": "plugin architecture, project config conflicts, migrations, permissions, and commerce checkout",
        "banner_url": "craft.example.com/admin/entries/news",
        "target": "entry card layout breaks in Twig",
        "comment": "fix Craft entry Twig layout",
        "sources": [
            ("Craft Plugin Store", "https://plugins.craftcms.com/"),
            ("Publishing to the Craft Plugin Store", "https://craftcms.com/docs/5.x/extend/plugin-store"),
        ],
    },
    {
        "slug": "statamic",
        "name": "Statamic",
        "short": "Statamic",
        "color": "#ff269e",
        "marketplace": "Statamic Marketplace",
        "audience": "Statamic site owners, Laravel teams, and addon creators",
        "headline": "Fix Statamic blueprints, Antlers templates, and addons faster",
        "sub": "Click the broken field, collection view, Antlers output, or addon panel. SimpleReview maps the change to blueprints, content, templates, and addon code, then prepares a fix.",
        "paths": "resources/views/, content/, blueprints/, users/, addons/",
        "can_fix": ["Antlers templates", "blueprint labels", "collection copy", "field instructions", "addon views", "navigation output", "CSS", "docs blocks"],
        "human": "custom Laravel addons, data migrations, permissions, multisite, and complex publishing workflows",
        "banner_url": "statamic.example.com/cp/collections/pages",
        "target": "blueprint field label confuses editors",
        "comment": "fix Statamic blueprint field label",
        "sources": [
            ("Statamic Addons", "https://statamic.com/marketplace/addons"),
            ("Statamic addon overview", "https://statamic.dev/addons/overview"),
            ("Building a Statamic addon", "https://statamic.dev/addons/building-an-addon"),
        ],
    },
    {
        "slug": "payload-cms",
        "name": "Payload CMS",
        "short": "Payload",
        "color": "#111111",
        "marketplace": "Payload plugin ecosystem",
        "audience": "Payload and Next.js teams building custom admin experiences",
        "headline": "Fix Payload admin fields and plugin code without hand-debugging",
        "sub": "Click a confusing field, broken custom component, or plugin panel. SimpleReview reads collections, fields, hooks, access rules, and plugin config before preparing a fix.",
        "paths": "src/collections/, src/globals/, src/components/, payload.config.ts, plugins/",
        "can_fix": ["field labels", "admin descriptions", "custom components", "hooks copy", "plugin config", "access-rule comments", "email templates", "docs examples"],
        "human": "access control, database migrations, custom auth, queues, and production plugin architecture",
        "banner_url": "payload.example.com/admin/collections/pages",
        "target": "custom admin field renders blank",
        "comment": "fix Payload admin field fallback",
        "sources": [
            ("Payload plugins overview", "https://payloadcms.com/docs/plugins/overview"),
            ("Building a Payload plugin", "https://payloadcms.com/docs/plugins/build-your-own"),
        ],
    },
    {
        "slug": "umbraco",
        "name": "Umbraco",
        "short": "Umbraco",
        "color": "#3544b1",
        "marketplace": "Umbraco Marketplace",
        "audience": "Umbraco editors, .NET agencies, and package developers",
        "headline": "Fix Umbraco templates, document types, and packages without guesswork",
        "sub": "Click the broken block, editor label, Razor template, or package setting. SimpleReview reads views, models, package files, and backoffice conventions before preparing a fix.",
        "paths": "Views/, App_Plugins/, Models/, Controllers/, wwwroot/",
        "can_fix": ["Razor views", "Block Grid labels", "dictionary items", "package UI copy", "CSS", "view components", "template snippets", "docs"],
        "human": "content migrations, custom property editors, commerce, security, and major upgrades",
        "banner_url": "umbraco.example.com/umbraco#/content",
        "target": "Block Grid label wrong in backoffice",
        "comment": "fix Umbraco Block Grid label",
        "sources": [
            ("Listing a package on Umbraco Marketplace", "https://docs.umbraco.com/umbraco-cms/extending/packages/listing-on-marketplace"),
            ("Umbraco Marketplace introduction", "https://docs.umbraco.com/umbraco-dxp/marketplace/introduction"),
        ],
    },
    {
        "slug": "nopcommerce",
        "name": "nopCommerce",
        "short": "nopCommerce",
        "color": "#4ab2f1",
        "marketplace": "nopCommerce Marketplace",
        "audience": "nopCommerce merchants, .NET developers, and plugin vendors",
        "headline": "Fix nopCommerce themes and plugins without hand-debugging",
        "sub": "Click the broken widget, checkout text, theme block, or plugin panel. SimpleReview follows nopCommerce plugin and theme paths before preparing a fix you can upload or review.",
        "paths": "src/Plugins/, src/Presentation/Nop.Web/Themes/, Views/, plugin.json",
        "can_fix": ["theme views", "widget labels", "plugin descriptions", "resource strings", "CSS", "admin copy", "email templates", "documentation"],
        "human": "payment plugins, tax rules, shipping logic, checkout customizations, and database migrations",
        "banner_url": "shop.example.com/admin/plugin/list",
        "target": "plugin view not updating after rebuild",
        "comment": "fix nopCommerce plugin view path",
        "sources": [
            ("nopCommerce Marketplace", "https://www.nopcommerce.com/en/marketplace"),
            ("Plugins in nopCommerce", "https://docs.nopcommerce.com/en/getting-started/advanced-configuration/plugins-in-nopcommerce.html"),
            ("nopCommerce plugin system", "https://docs.nopcommerce.com/en/developer/tutorials/description-of-plugin-system.html"),
        ],
    },
    {
        "slug": "dnn",
        "name": "DNN",
        "short": "DNN",
        "color": "#0f75bc",
        "marketplace": "DNN Store",
        "audience": "DNN portal owners, .NET agencies, and extension developers",
        "headline": "Fix DNN modules, themes, and portal UX without hand-debugging",
        "sub": "Click the broken module, skin area, Persona Bar setting, or extension text. SimpleReview maps the issue to DNN extension files and prepares a fix you can upload or review.",
        "paths": "DesktopModules/, Portals/_default/Skins/, Providers/, App_Code/",
        "can_fix": ["module labels", "theme markup", "skin CSS", "settings text", "Razor module snippets", "extension docs", "resource strings", "admin copy"],
        "human": "compiled modules, providers, security roles, portal migrations, and legacy upgrades",
        "banner_url": "portal.example.com/Admin/Extensions",
        "target": "module settings label unclear",
        "comment": "fix DNN module settings label",
        "sources": [
            ("DNN extension docs", "https://docs.dnncommunity.org/content/features/extensibility/extensions/index.html"),
            ("DNN Store", "https://store.dnnsoftware.com/"),
        ],
    },
    {
        "slug": "concrete-cms",
        "name": "Concrete CMS",
        "short": "Concrete",
        "color": "#2d72d9",
        "marketplace": "Concrete CMS Marketplace",
        "audience": "Concrete CMS site owners, block developers, and theme vendors",
        "headline": "Fix Concrete CMS blocks, themes, and add-ons without losing editability",
        "sub": "Click the broken block, dashboard screen, composer field, or theme area. SimpleReview follows Concrete packages, blocks, and theme overrides before preparing a fix.",
        "paths": "application/blocks/, packages/, application/themes/, application/controllers/",
        "can_fix": ["block templates", "theme areas", "dashboard copy", "composer labels", "package docs", "CSS", "view templates", "language strings"],
        "human": "custom blocks, package architecture, permissions, migrations, and marketplace packaging",
        "banner_url": "concrete.example.com/dashboard/pages",
        "target": "custom block layout breaks editor",
        "comment": "fix Concrete CMS block template",
        "sources": [
            ("Concrete CMS Marketplace", "https://market.concretecms.com/"),
            ("Concrete CMS submitting code", "https://www.concretecms.com/community/submitting-code"),
        ],
    },
    {
        "slug": "typo3",
        "name": "TYPO3",
        "short": "TYPO3",
        "color": "#ff8700",
        "marketplace": "TYPO3 Extension Repository",
        "audience": "TYPO3 integrators, agencies, and extension maintainers",
        "headline": "Fix TYPO3 sitepackage and extension UX without hand-debugging",
        "sub": "Click the broken Fluid template, TypoScript output, backend label, or extension screen. SimpleReview maps it to sitepackage and extension files before preparing a fix.",
        "paths": "packages/sitepackage/, Configuration/TypoScript/, Resources/Private/Templates/, ext_localconf.php",
        "can_fix": ["Fluid templates", "TypoScript snippets", "backend labels", "sitepackage CSS", "extension docs", "language files", "partial templates", "form labels"],
        "human": "Extbase architecture, access control, migrations, composer upgrades, and security-sensitive extensions",
        "banner_url": "typo3.example.com/typo3/module/web/layout",
        "target": "Fluid partial outputs wrong CTA",
        "comment": "fix TYPO3 Fluid partial CTA",
        "sources": [
            ("Publish to TYPO3 TER", "https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ExtensionArchitecture/HowTo/PublishExtension/PublishToTER/Index.html"),
            ("TYPO3 Composer repository", "https://get.typo3.org/misc/composer/repository"),
        ],
    },
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_sources(sources: list[tuple[str, str]]) -> tuple[str, str]:
    links = "\n".join(
        f'        <li><a href="{esc(url)}" rel="nofollow">{esc(label)}</a></li>'
        for label, url in sources
    )
    json_links = ", ".join('"%s"' % esc(url) for _, url in sources)
    return links, json_links


def render_page(hub: dict) -> str:
    source_items, source_json = render_sources(hub["sources"])
    fixes = "\n".join(f'        <div class="fix-item">{esc(item)}</div>' for item in hub["can_fix"])
    faq = [
        (f"Can SimpleReview edit {hub['name']} safely?", f"Yes for narrow file-level edits in {hub['paths']}. For {hub['human']}, use Vibers human review before merge."),
        (f"Where should announcements for {hub['name']} point?", f"Use this hub, https://onout.org/{hub['slug']}/, as the forum and marketplace announcement URL. Deep guides should only be linked when answering a specific technical problem."),
        (f"Does this replace a {hub['name']} developer?", "No. It removes the waiting time for small template, copy, UI, and documentation fixes. Complex engineering still needs a specialist and human review."),
        ("How does the site fix workflow work?", "Connect Git or SFTP/SSH, click the problem in the browser, describe the change, and let SimpleReview draft a focused fix that can be uploaded to the site or reviewed first."),
    ]
    faq_json = ",\n      ".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (esc(q), esc(a))
        for q, a in faq
    )
    faq_html = "\n".join(
        f'      <div class="faq-item"><div class="faq-q">{esc(q)}</div><div class="faq-a">{esc(a)}</div></div>'
        for q, a in faq
    )
    slug = hub["slug"]
    color = hub["color"]
    template = Template("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$headline — SimpleReview for $name</title>
  <meta name="description" content="$description">
  <meta name="keywords" content="$name SimpleReview, fix $name site, $name developer, $marketplace">
  <link rel="canonical" href="https://onout.org/$slug/">
  <link rel="icon" type="image/x-icon" href="../favicon.ico">
  <link rel="icon" type="image/png" sizes="512x512" href="../favicon.png">
  <link rel="apple-touch-icon" href="../apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:title" content="$headline">
  <meta property="og:description" content="$og_description">
  <meta property="og:url" content="https://onout.org/$slug/">
  <meta property="og:image" content="https://onout.org/vibers/assets/vibers-logo-source.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="$headline">
  <meta name="twitter:description" content="$og_description">
  <meta name="twitter:image" content="https://onout.org/vibers/assets/vibers-logo-source.jpg">
  <link rel="alternate" hreflang="en" href="https://onout.org/$slug/">
  <link rel="alternate" hreflang="x-default" href="https://onout.org/$slug/">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-LQLZ1SZS26"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-LQLZ1SZS26');</script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "inLanguage": "en",
    "headline": "$headline",
    "description": "$sub",
    "url": "https://onout.org/$slug/",
    "datePublished": "$date",
    "dateModified": "$date",
    "author": { "@type": "Organization", "name": "Vibers", "url": "https://onout.org/vibers/" },
    "publisher": {
      "@type": "Organization",
      "name": "Vibers",
      "url": "https://onout.org/vibers/",
      "logo": { "@type": "ImageObject", "url": "https://onout.org/vibers/favicon.png" }
    },
    "mainEntityOfPage": { "@type": "WebPage", "@id": "https://onout.org/$slug/" },
    "citation": [$source_json]
  }
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","inLanguage":"en","mainEntity":[$faq_json]}
  </script>
  <style>
    *{box-sizing:border-box}html{font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;-webkit-text-size-adjust:100%}body{margin:0;background:#fff;color:#1a1a1a;font-size:16px;line-height:1.62;-webkit-font-smoothing:antialiased}a{color:$color;text-decoration:none}a:hover{text-decoration:underline}code{background:#f1f1f1;border-radius:4px;padding:1px 5px;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.92em;overflow-wrap:anywhere}.page{max-width:900px;margin:0 auto;padding:24px 32px 48px}.site-nav{font-size:13px;color:#888;margin-bottom:32px}.site-nav a{color:#888;border-bottom:1px solid #ddd}.hero{border-bottom:2px solid #1a1a1a;padding:28px 0 32px;margin-bottom:32px}.hero-badge{display:inline-flex;align-items:center;gap:8px;color:$color;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;margin-bottom:14px}.hero-badge:before{content:"";width:7px;height:7px;border-radius:50%;background:$color}h1{font-size:48px;line-height:1.05;letter-spacing:-.9px;margin:0 0 16px;color:#151515}h2{font-size:29px;line-height:1.18;letter-spacing:-.4px;margin:0 0 16px;color:#151515}h3{font-size:18px;margin:0 0 8px;color:#151515}p{margin:0 0 14px}.hero-sub{font-size:19px;color:#333;max-width:760px;line-height:1.48}.cta-group{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;border-radius:8px;padding:12px 22px;font-weight:700}.btn-primary{background:$color;color:#fff}.btn-secondary{background:#fff;color:#151515;border:1px solid #d8d8d8}section{margin:38px 0}.what-fixes{border:1px solid #e8e8e8;border-radius:8px;padding:24px}.fixes-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px 24px;margin-top:16px}.fix-item{font-size:15px;color:#333;display:flex;gap:8px}.fix-item:before{content:"->";color:$color;font-weight:800;flex-shrink:0}.steps{display:grid;gap:16px}.step{display:flex;gap:16px;align-items:flex-start;border:1px solid #e8e8e8;border-radius:8px;padding:18px}.step>div:last-child{min-width:0}.step-num{flex-shrink:0;width:32px;height:32px;border-radius:50%;background:$color;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800}.vs-section{background:#fafafa;border:1px solid #e6e6e6;border-radius:8px;padding:24px}.case-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.case-card{border:1px solid #e8e8e8;border-radius:8px;padding:18px}.faq-item{border-bottom:1px solid #e8e8e8;padding:15px 0}.faq-q{font-weight:700;font-size:17px;margin-bottom:6px}.faq-a{color:#444;font-size:15px}.source-list{padding-left:20px}.cta-box{background:#151515;color:#fff;border-radius:8px;padding:30px;text-align:center}.cta-box h2{color:#fff}.cta-box p{color:#ddd}footer{border-top:1px solid #e8e8e8;margin-top:46px;padding-top:22px;color:#888;font-size:13px}
    .sc-banner{background:#0f0f0f;border-radius:12px;overflow:hidden;margin:0 0 34px;box-shadow:0 4px 32px rgba(0,0,0,.18);position:relative}.sc-chrome{background:#e8e8e8;border-bottom:1px solid #d0d0d0;padding:8px 12px;display:flex;align-items:center;gap:8px}.sc-dots{display:flex;gap:5px}.sc-dots span{width:10px;height:10px;border-radius:50%;display:block}.sc-dots span:nth-child(1){background:#ff5f57}.sc-dots span:nth-child(2){background:#ffbd2e}.sc-dots span:nth-child(3){background:#28c840}.sc-url{flex:1;background:#fff;border:1px solid #c8c8c8;border-radius:4px;padding:4px 12px;font-size:12px;color:#444;margin:0 8px}.sc-ext-icon{width:20px;height:20px;border-radius:4px;animation:extPulse 28s infinite}@keyframes extPulse{0%,10%{box-shadow:none}11.5%{box-shadow:0 0 0 6px rgba(255,107,53,.7)}13%,100%{box-shadow:none}}.sc-viewport{min-height:380px;position:relative;background:#fff;overflow:hidden}.sc-content-row{position:relative;min-height:380px;overflow:hidden;background:#f6f6f6}.sc-site{padding-right:220px;min-height:380px}.sc-topbar{background:#1d1d1b;color:#fff;font-size:10px;padding:6px 18px;display:flex;justify-content:space-between}.sc-header{background:#fff;border-bottom:1px solid #e0e0e0;padding:12px 18px;display:flex;justify-content:space-between;align-items:center}.sc-logo{font-size:15px;font-weight:900}.sc-logo span{color:$color}.sc-pill{background:$color;color:#fff;border-radius:18px;padding:4px 12px;font-size:11px;font-weight:800}.sc-target{max-width:500px;margin:22px 0 0 28px;background:#fff;border:1px solid #e5e7eb;border-radius:6px;overflow:hidden;animation:targetSel 28s infinite;outline-offset:3px;position:relative}@keyframes targetSel{0%,21%{outline:none;box-shadow:none}23%,86%{outline:3px solid #ff6b35;box-shadow:0 0 0 4px rgba(255,107,53,.18)}90%,100%{outline:none;box-shadow:none}}.sc-target:after{content:"Selected";position:absolute;top:-10px;right:10px;background:#ff6b35;color:#fff;font-size:8px;font-weight:800;letter-spacing:.4px;text-transform:uppercase;padding:2px 6px;border-radius:3px;opacity:0;animation:selBadge 28s infinite}@keyframes selBadge{0%,21%{opacity:0}23%,86%{opacity:1}90%,100%{opacity:0}}.sc-target-head{background:#fff;border-bottom:1px solid #e5e7eb;padding:10px 14px;font-size:12px;font-weight:900;color:#151515}.sc-row{display:flex;justify-content:space-between;gap:12px;padding:11px 14px;border-bottom:1px solid #e5e7eb;font-size:11px;color:#3f3f46}.sc-row:last-child{border-bottom:none}.sc-alert{position:absolute;left:28px;top:265px;width:500px;background:#fff7ed;border:1px solid #fb923c;border-left:4px solid #f97316;border-radius:6px;padding:10px 14px;font-size:11px;color:#7c2d12;opacity:0;animation:alertShow 28s infinite}@keyframes alertShow{0%,55%{opacity:0;transform:translateY(8px)}61%,93%{opacity:1;transform:translateY(0)}96%,100%{opacity:0}}.sc-sidebar{width:205px;background:#f8fafc;border-left:1px solid #e5e7eb;position:absolute;right:0;top:0;bottom:0;z-index:5;padding:11px 10px;animation:sbSlide 28s infinite}@keyframes sbSlide{0%,11%{transform:translateX(100%);opacity:0}14%,93%{transform:translateX(0);opacity:1}96%,100%{transform:translateX(100%);opacity:0}}.sc-panel-logo{font-size:12px;font-weight:900;color:#ff6b35;margin-bottom:10px}.sc-card{background:#fff;border:1px solid #e5e7eb;border-radius:6px;padding:9px;margin-bottom:8px;font-size:10px;color:#374151;opacity:0}.sc-c1{animation:card1 28s infinite}.sc-c2{animation:card2 28s infinite}.sc-c3{animation:card3 28s infinite}@keyframes card1{0%,57%{opacity:0;transform:translateY(8px)}61%,93%{opacity:1;transform:translateY(0)}96%,100%{opacity:0}}@keyframes card2{0%,64%{opacity:0;transform:translateY(8px)}68%,93%{opacity:1;transform:translateY(0)}96%,100%{opacity:0}}@keyframes card3{0%,71%{opacity:0;transform:translateY(8px)}75%,93%{opacity:1;transform:translateY(0)}96%,100%{opacity:0}}.sc-card b{display:block;color:#111827;margin-bottom:3px}.sc-popup{position:absolute;right:420px;top:184px;width:245px;background:#fff;border:1px solid #d7d7d8;border-radius:8px;box-shadow:0 12px 36px rgba(0,0,0,.18);z-index:8;padding:11px;opacity:0;animation:popupShow 28s infinite}@keyframes popupShow{0%,24%{opacity:0;transform:translateY(8px)}26%,93%{opacity:1;transform:translateY(0)}96%,100%{opacity:0}}.sc-popup-title{font-size:10px;font-weight:900;color:$color;margin-bottom:7px}.sc-popup-ta{min-height:50px;background:#f8fafc;border:1px solid #e5e7eb;border-radius:5px;padding:8px;font-size:10px;color:#111827;line-height:1.35}.sc-type{display:inline-block;white-space:nowrap;overflow:hidden;border-right:1px solid #111827;max-width:0;animation:typeText 28s infinite steps(42,end)}@keyframes typeText{0%,27%{max-width:0}46%,93%{max-width:220px}96%,100%{max-width:0}}.sc-popup-fix{margin-top:8px;background:$color;color:#fff;border-radius:5px;padding:7px 10px;text-align:center;font-size:10px;font-weight:900}.sc-cursor{position:absolute;width:18px;height:18px;z-index:20;pointer-events:none;left:360px;top:235px;opacity:0;animation:scCur 28s infinite}.sc-cursor:before{content:"";position:absolute;width:0;height:0;border-left:14px solid #111827;border-top:9px solid transparent;border-bottom:9px solid transparent;transform:rotate(-28deg);filter:drop-shadow(0 2px 2px rgba(0,0,0,.25))}.sc-cursor:after{content:"";position:absolute;left:5px;top:10px;width:7px;height:12px;background:#111827;transform:rotate(-28deg);border-radius:2px}@keyframes scCur{0%{left:360px;top:235px;opacity:0}2%{left:360px;top:235px;opacity:1}10%{left:695px;top:24px;opacity:1}14%{left:695px;top:24px;opacity:1}20%{left:430px;top:156px;opacity:1}26%{left:180px;top:232px;opacity:1}49%{left:180px;top:304px;opacity:1}74%{left:610px;top:208px;opacity:1}93%{left:610px;top:208px;opacity:1}96%,100%{opacity:0}}.sc-progress{height:4px;background:#2a2a2e}.sc-progress-fill{height:100%;width:0;background:#ff6b35;animation:prog 28s infinite linear}@keyframes prog{0%{width:0}93%{width:100%}96%,100%{width:0}}.sc-caption{background:#111827;color:#e5e7eb;padding:10px 14px;font-size:12px}
    @media(max-width:760px){.page{padding:18px 18px 42px}h1{font-size:32px}h2{font-size:24px}.hero-sub{font-size:17px}.fixes-grid,.case-grid{grid-template-columns:1fr}.btn{width:100%}.sc-banner{display:none}}
  </style>
</head>
<body>
<main class="page">
  <nav class="site-nav"><a href="/vibers/">Vibers</a> &nbsp;/&nbsp; <a href="/simple-review/">SimpleReview</a> &nbsp;/&nbsp; $name</nav>
  <header class="hero">
    <div class="hero-badge">SimpleReview for $name</div>
    <h1>$headline</h1>
    <p class="hero-sub">$sub</p>
    <div class="cta-group">
      <a class="btn btn-primary" href="https://chromewebstore.google.com/detail/baiophhkajldflnpaaijgdigbkomkimm?utm_source=onout_${slug}_hub&utm_medium=hero_cta">Get SimpleReview for Chrome</a>
      <a class="btn btn-secondary" href="/vibers/">Need human review?</a>
    </div>
  </header>

  <div id="sc-banner-fallback" class="sc-banner" aria-label="Animated SimpleReview demo for $name">
    <div class="sc-chrome">
      <div class="sc-dots"><span></span><span></span><span></span></div>
      <div class="sc-url">$banner_url</div>
      <img class="sc-ext-icon" src="../favicon.png" alt="SimpleReview">
    </div>
    <div class="sc-viewport">
      <div class="sc-content-row">
        <div class="sc-site">
          <div class="sc-topbar"><span>$name</span><span>Live site / admin</span></div>
          <div class="sc-header"><div class="sc-logo">$short<span>Review</span></div><div class="sc-pill">Connected repo</div></div>
          <div class="sc-target">
            <div class="sc-target-head">$target</div>
            <div class="sc-row"><span>Platform path</span><code>$first_path</code></div>
            <div class="sc-row"><span>Issue type</span><span>file-level fix</span></div>
            <div class="sc-row"><span>Output</span><strong>Site fix</strong></div>
          </div>
          <div class="sc-alert"><strong>Risk check:</strong> SimpleReview drafts the small diff; Vibers reviews changes touching $human.</div>
        </div>
        <div class="sc-sidebar">
          <div class="sc-panel-logo">SimpleReview</div>
          <div class="sc-card sc-c1"><b>Detected $name</b>Mapped the selected UI to project files.</div>
          <div class="sc-card sc-c2"><b>Patch scope</b>Keep the diff narrow: copy, template, config, or docs.</div>
          <div class="sc-card sc-c3"><b>Ready to upload</b>Includes changed files, test notes, and rollback guidance.</div>
        </div>
        <div class="sc-popup">
          <div class="sc-popup-title">Comment to SimpleReview</div>
          <div class="sc-popup-ta"><span class="sc-type">$comment</span></div>
          <div class="sc-popup-fix">Fix it</div>
        </div>
        <div class="sc-cursor"></div>
      </div>
    </div>
    <div class="sc-progress"><div class="sc-progress-fill"></div></div>
    <div class="sc-caption">SimpleReview turns a visible $name problem into a fix you can upload to the site instead of a vague support ticket.</div>
  </div>

  <section class="what-fixes">
    <h2>What SimpleReview can fix on $name</h2>
    <p>Use this hub as the public announcement URL for forums and directories. It is optimized for $audience; deep technical guides should be linked only when answering a matching problem.</p>
    <div class="fixes-grid">
$fixes
    </div>
  </section>

  <section>
    <h2>How it works</h2>
    <div class="steps">
      <div class="step"><div class="step-num">1</div><div><h3>Open the $name page or admin screen</h3><p>SimpleReview detects the platform and keeps the task anchored to the real UI the user wants to change.</p></div></div>
      <div class="step"><div class="step-num">2</div><div><h3>Click the broken element</h3><p>The extension captures the selected context and maps it to likely paths such as <code>$paths</code>.</p></div></div>
      <div class="step"><div class="step-num">3</div><div><h3>Describe the change in plain language</h3><p>The agent drafts a focused diff instead of rewriting unrelated parts of the CMS project.</p></div></div>
      <div class="step"><div class="step-num">4</div><div><h3>Upload the fix to the site</h3><p>Apply small file-level fixes through Git, SFTP/SSH, or your normal deployment flow; escalate $human to Vibers human review.</p></div></div>
    </div>
  </section>

  <section class="vs-section">
    <h2>Where this fits</h2>
    <p><strong>Good fit:</strong> small recurring CMS fixes that should become a site update. <strong>Not a fit for unattended AI:</strong> $human. That split keeps the forum promise honest: SimpleReview is a practical tool, not a replacement for senior platform engineering.</p>
  </section>

  <section class="use-cases">
    <h2>Use cases</h2>
    <div class="case-grid">
      <div class="case-card"><h3>Site owners</h3><p>Fix visible copy, layout, and admin issues without waiting for a maintenance retainer slot.</p></div>
      <div class="case-card"><h3>Agencies</h3><p>Turn the boring tickets into site-ready fixes so senior developers stay focused on architecture and integration work.</p></div>
      <div class="case-card"><h3>Plugin and addon developers</h3><p>Use the hub as a support-friendly announcement page for $marketplace users.</p></div>
      <div class="case-card"><h3>Forum helpers</h3><p>Link this hub for the product overview, then link deep guides only when the thread asks for that specific fix.</p></div>
    </div>
  </section>

  <section class="faq-section">
    <h2>FAQ</h2>
$faq_html
  </section>

  <section>
    <h2>Sources checked for this hub</h2>
    <ul class="source-list">
$source_items
    </ul>
  </section>

  <section class="cta-box">
    <h2>Send a $name fix to your site</h2>
    <p>Use SimpleReview for narrow platform edits that can be uploaded through Git, SFTP/SSH, or your normal deploy flow. Bring Vibers in when the change needs human signoff before production.</p>
    <div class="cta-group" style="justify-content:center">
      <a class="btn btn-primary" href="https://chromewebstore.google.com/detail/baiophhkajldflnpaaijgdigbkomkimm?utm_source=onout_${slug}_hub&utm_medium=bottom_cta">Install SimpleReview</a>
      <a class="btn btn-secondary" href="/vibers/">Get human review</a>
    </div>
  </section>

  <footer>
    <p>SimpleReview for $name is a product by <a href="/vibers/">Vibers</a>. This hub is the public forum and marketplace announcement target for <a href="https://onout.org/$slug/">onout.org/$slug/</a>.</p>
  </footer>
</main>
<script>
(function(){
  var banner = document.querySelector('#sc-banner-fallback');
  if(!banner) return;
  function restartAll(){
    var s = document.createElement('style');
    s.textContent = '#sc-banner-fallback.r, #sc-banner-fallback.r *, #sc-banner-fallback.r *::before, #sc-banner-fallback.r *::after { animation: none !important; }';
    document.head.appendChild(s);
    banner.classList.add('r');
    void banner.offsetWidth;
    banner.classList.remove('r');
    document.head.removeChild(s);
  }
  var triggered = false;
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting && !triggered){
        triggered = true;
        restartAll();
        setTimeout(function(){ triggered = false; }, 28000);
      }
    });
  }, {threshold: 0.3});
  io.observe(banner);
})();
</script>
</body>
</html>
""")
    return template.substitute(
        audience=esc(hub["audience"]),
        banner_url=esc(hub["banner_url"]),
        color=esc(color),
        comment=esc(hub["comment"]),
        date=DATE,
        description=esc(hub["sub"][:155]),
        faq_html=faq_html,
        faq_json=faq_json,
        first_path=esc(hub["paths"].split(",")[0]),
        fixes=fixes,
        headline=esc(hub["headline"]),
        human=esc(hub["human"]),
        marketplace=esc(hub["marketplace"]),
        name=esc(hub["name"]),
        og_description=esc(hub["sub"][:190]),
        paths=esc(hub["paths"]),
        short=esc(hub["short"]),
        slug=esc(slug),
        source_items=source_items,
        source_json=source_json,
        sub=esc(hub["sub"]),
        target=esc(hub["target"]),
    )


def main() -> None:
    for hub in HUBS:
        out = ROOT / hub["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(hub), encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
