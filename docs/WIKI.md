# Vibers Wiki

Internal knowledge base. For the public README see [../README.md](../README.md).

---

## Product

| Doc | Description |
|-----|-------------|
| [../SKILL.md](../SKILL.md) | AI Agent skill — client-facing quickstart (English) |
| [../REVIEW-RUNBOOK.md](../REVIEW-RUNBOOK.md) | Step-by-step review workflow for reviewers |
| [../CLAUDE.md](../CLAUDE.md) | Claude Code project instructions |
| [../simple-review/index.html](../simple-review/index.html) | **SimpleReview** — Chrome Extension "Website Feedback & Fix Tool". Click element → Fix It → code fix that can be uploaded to the site. Beta, free first fix. Landing at `/simple-review/` |

## Freelance Reply Automation

Internal workflow for preparing and publishing replies to Kwork and FL.ru projects.

### Canonical rule

Reply text is always written by the agent manually through `/root/.claude/skills/write-proposal-or-cover-letter/SKILL.md`. The browser scripts are not copywriters: they only read a finished `--message-file`, fill the marketplace form, save screenshots, and optionally submit.

### Skill registry

| Skill | Path | Purpose |
|---|---|---|
| `write-proposal-or-cover-letter` | `/root/.claude/skills/write-proposal-or-cover-letter/SKILL.md` | Single source of truth for proposal copy, SimpleReview angle, portfolio links, Kwork safety copy, and post-draft publishing links. |
| `reply-project-kwork` | `/root/.claude/skills/reply-project-kwork/SKILL.md` -> `/root/vibers/.agents/skills/reply-project-kwork/SKILL.md` | Safe Kwork dry-run/submit workflow using `/root/kwork/reply-project.js`. |
| `reply-project-flru` | `/root/.claude/skills/reply-project-flru/SKILL.md` -> `/root/vibers/.agents/skills/reply-project-flru/SKILL.md` | Safe FL.ru dry-run/submit workflow using `/root/flru/reply-project.js` and saved cookies. |
| `tz-estimation-audit` | `/root/.claude/skills/tz-estimation-audit/SKILL.md` | Must be used by the proposal skill when a reply includes estimate, stages, or custom development scope. |

### Platform scripts

| Platform | Script | Runtime docs | Drafts | Screenshots |
|---|---|---|---|---|
| Kwork | `/root/kwork/reply-project.js` | `/root/kwork/README.md`, `/root/kwork/docs/wiki.md` | `/root/kwork/replies/` | `/root/kwork/screenshots/` |
| FL.ru | `/root/flru/reply-project.js` | `/root/flru/README.md`, `/root/flru/docs/wiki.md` | `/root/flru/replies/` | `/root/flru/screenshots/` |

### Safety rules

- Dry-run first on both platforms; inspect the generated screenshot before submit.
- Submit only after explicit user approval with `--submit --confirm-spend`.
- Kwork minimum price is `5000` RUB and Kwork replies must not include external links, Telegram, email, phone, or calls to leave Kwork.
- FL.ru may include links where appropriate; SimpleReview URL is `https://onout.org/#ru`.
- For SimpleReview positioning, say `я`, not `мы`: the client checks the result, and I help if there is a blocker. Subscription/setup is `5000` RUB/month.
- Keep cookies outside git repos; FL.ru cookies live at `/root/flru/cookies.json` with private permissions.

### Last verified flow

On 2026-05-07 the FL.ru workflow was tested and submitted on project `5503877`: reply file `/root/flru/replies/project_5503877_manual_2026-05-07.txt`, price `35000` RUB, term `7` days, final screenshot `/root/flru/screenshots/flru_reply_after_submit_2026-05-07T16-02-44-612Z.png`.

### SimpleReview — Visual Feedback & Fix Chrome Extension

**Positioning:** "Website Feedback & Fix Tool" — отличие от конкурентов: не просто репортит баг, а чинит и даёт фикс, который можно залить на сайт.

**Direct competitors (visual feedback tools):**

| Tool | Pricing | Target | Key diff vs SimpleReview |
|------|---------|--------|----------------------|
| **Marker.io** | $39/mo+ | Agencies, QA teams | Reports only. Session replay, console logs, 20+ integrations. No fixes, no PR. |
| **BugHerd** | $50/mo+ (5 seats) | Web agencies, UAT | "Sticky notes on a webpage." Client-friendly Kanban, no login for clients. No code fixes. G2 4.8/5 |
| **Usersnap** | $39-249/mo | Product/SaaS teams, PM | Enterprise: AI sentiment, surveys, SDK, 50+ integrations. No code access. |
| **Feedbucket** | 14-day trial, paid | Agencies + clients | Reports only, no dev fixes. Widget (no extension). |
| **Userback** | Freemium + paid | Product teams, SaaS | NPS, surveys, session replay, roadmap. No code fixes. 20K+ teams. |
| **Huddlekit** | Free / $190-390 yr | Design studios, agencies | Multi-breakpoint preview, element inspector, share-by-link, task mgmt. Дёшево vs Marker/BugHerd. No code fixes, no PR. |
| **Jam.dev** | Free → $20/seat/mo | Frontend devs, QA, indies | Chrome ext: 1-click bug report + console/network/repro + Instant Replay. MCP for Cursor/Claude. No PR. |
| **Bird Eats Bug** | Free → $20-40/user/mo | SaaS QA + support | Screen recording + auto console/network/env logs. AI Bug Assistant. No PR. |
| **Ruttl** | Free → $8-19/mo | Designers, freelancers | Live website + Figma/PDF/image collaboration, mobile review. No code fixes. |
| **Pastel** | $24-99/mo | Marketing agencies | Annotations on live URL без extension (canvas mode), version comparison. No code fixes. |
| **MarkUp.io** | Free → $14/mo | Designers, video reviewers | Multi-format proofing (web/image/video/PDF). Adjacent (design, not dev). |
| **Webvizio** | $19-79/mo | Web agencies | Visual collab + kanban из веб-комментариев, GitHub integration. No code fixes. |
| **PageProofer** | $20-100/mo | Small studios | Sticky-note feedback, viewport screenshots. Lightweight BugHerd-аналог. |

**Полный список (12):** Marker.io, Userback, BugHerd, Usersnap, Ruttl, Pastel, MarkUp.io, Feedbucket, Webvizio, PageProofer, Jam.dev, Bird Eats Bug. → подробные профили в [COMPETITORS.md](COMPETITORS.md).

**Key message:** All of them → ticket. SimpleReview → site-ready fix. All paid, SimpleReview free (BYOK).

**Alternative-статьи (опубликованы 2026-04-18):** `/blog/markerio-alternative/`, `/blog/bugherd-alternative/`, `/blog/usersnap-alternative/`. Все таргетят low-KD KWs (KD 1-4) + "free X" intent.

→ Полный анализ + "alternative to" messaging: [COMPETITORS.md#visual-feedback-tools](COMPETITORS.md#visual-feedback-tools-simple-review-специфичные-конкуренты)
→ Marker.io keyword intelligence (4431 KW): [marker-io-keyword-insights.md](marker-io-keyword-insights.md)

## Marketing & SEO

| Doc | Description |
|-----|-------------|
| [COMPETITORS.md](COMPETITORS.md) | 11 competitors — pricing, features, SEO strategies, keywords |
| [competitive-research/](competitive-research/) | Ad copy analysis (SonarSource, Google Ads) |
| [keywords/](keywords/) | SEMrush keyword exports (6 CSV files, 2026-04-14) |
| [reddit-alpha-beta-users.md](reddit-alpha-beta-users.md) | Reddit strategy for finding alpha/beta users |
| [backlink-opportunities.md](backlink-opportunities.md) | 13 directories + 6 dev blogs + media pitch targets |
| [COMPETITORS.md#markerio-markerio](COMPETITORS.md) | Marker.io ($39/mo) + **Feedbucket** (agency feedback tool) + Markup.io (design, adjacent) — прямые конкуренты SimpleReview. Marker.io: контент-паттерн (template hubs, utility tripwire) в COMPETITORS.md |
| [advertising-channels.md](advertising-channels.md) | Полная карта рекламы: каталоги, ad networks, newsletters, стратегия по бюджету |
| [backlinks/](backlinks/) | Raw SEMrush backlink exports (CodeRabbit 4.6K, Qodo 6K domains); `submission-targets-from-competitor-backlinks.csv` — каталоги из бэклинков конкурентов |
| [topic-research-20260414.xlsx](topic-research-20260414.xlsx) | SEMrush Topic Research — 108 content ideas with volumes, questions, backlinks |
| [google-2026-content-strategy.md](google-2026-content-strategy.md) | **NEW** Google March 2026 правила: что банят (scaled abuse), что поднимают (Information Gain). Наша стратегия. |
| [bug-cluster-research.md](bug-cluster-research.md) | **NEW** 30 багов из SO + GitHub, классифицированы по SimpleReview fit и Noxon expertise. Roadmap на 5-10 статей. |
| [animated-banner-guide.md](animated-banner-guide.md) | Инструкция по созданию анимированных баннеров (cursor→highlight→popup→spinner→ready-to-upload fix sidebar) для статей блога и лендингов. Включает формат voiceover JSON (зашитые субтитры для диктора). |
| [marketplace-cover-banners.md](marketplace-cover-banners.md) | HTML-варианты и правила обложек для маркетплейсов/Kwork: `Проблема -> Работа -> Фикс`, CMS-логотипы, пути `/root/kwork/cover-html/*.html` и `/root/kwork/covers/*.png`. |
| [meta-cms-creatives-2026-05-05.md](meta-cms-creatives-2026-05-05.md) | Meta Ads creative pack for 22 CMS hubs + Discourse: landing URLs with UTM, primary text, headlines, descriptions, and visual templates. |

### Workflow: написание SEO-статьи для блога

1. **Исследование ключевых слов** → `/demand-research <тема>` — вытаскивает Wordstat, Google Suggest, People Also Ask
2. Если есть Semrush CSV/gist — парсить все группы (high-vol, mid-vol, platform-specific) и покрыть каждую группу в статье
3. **Маппинг ключей в секции:**
   - High-volume → title, H1, первые 100 слов, meta description, meta keywords
   - Platform/tool-specific → отдельный H2/H3 для каждой платформы (WordPress, Shopify, Webflow…)
   - PAA-вопросы → FAQ-раздел (+ FAQ-schema в JSON-LD)
   - Long-tail → естественно по тексту
4. **Баннер** — каждая статья должна иметь анимированный `.cap-banner` с `cap-voiceover` JSON внутри (инструкция в `animated-banner-guide.md`)
5. **CTA** — минимум 2: один сразу после баннера (ext-callout), один в конце статьи (`.cta-block`)
6. **Meta tags** — `<meta name="keywords">` + `<meta name="description">` + OG-теги
7. **⛔ Не палить SEO** на видимой странице — никаких "N mo. searches", "KD X", "targeted keyword" в копи. Эти метрики только в коммитах + `docs/keywords/libs/*.md`. Подробности ниже в [Cluster writing playbook](#cluster-writing-playbook).

### Cluster writing playbook (lib hubs + cluster articles)

Применяется когда мы пишем по либе из 38-lib pain-points список (`docs/keywords/libs/_pain-points.md`). Pillar+cluster pattern: 1 hub `/<lib>/` + 5 cluster articles `/<lib>/<slug>/`.

#### Структура

| Тип страницы | Путь | Стиль | Содержит |
|---|---|---|---|
| **Hub** | `/<lib>/index.html` | Landing-page как `onout.org/` (а не handbook-style) | Hero + банер + TL;DR + **honest disclaimer callout** + practical guides grid (БЕЗ SEO-цифр) + оригинальный материал хаба (бенчмарки, decision matrix) + production checklist + FAQ + footer |
| **Cluster article** | `/<lib>/<slug>/index.html` | Article-style (~600-1000 строк HTML) | TL;DR + research-backed разделы + **first-hand артефакт** (рабочий конфиг/код/бенчмарк/CVE PoC) + debug-таблица или decision-matrix + FAQ + cross-link на 4 sibling-статьи + back to hub |

#### Hub — обязательные элементы

1. **Hero** — strong promise (что юзер получит), 2 CTA (главный → most-pain guide; secondary → SimpleReview)
2. **Анимированный SimpleReview баннер** в hero — мокап админки этой либы на фоне, курсор анимируется на кнопку **Fix It** в sidebar
3. **TL;DR card** (5 буллетов что есть в хабе)
4. **Honest disclaimer callout** ([тон как у `simple-review/index.html`](../simple-review/index.html)) — кто мы, чем НЕ являемся (не аффилированы с компанией-разработчиком), приглашение фиксить ошибки на GitHub. Ставится сразу после TL;DR.
5. **Practical guides grid** (5 cluster cards + 1 SimpleReview card) — без SEO-метрик, только title + plain description
6. **Оригинальный материал хаба** — то, ради чего форум-юзеры останутся: hardware benchmark table, decision matrix self-host vs cloud, app.yml mental model, production checklist
7. **FAQ** + FAQPage JSON-LD
8. **Author byline** (Vibers org) в `Article` JSON-LD + видимая ссылка в footer

#### Cluster article — обязательные элементы

1. **Inline animated banner** — мокап на фоне строго по теме статьи (URL bar = relevant admin URL, highlighted element = relevant feature, sidebar comment = topic-specific), курсор → **Fix It button**. Каждая статья = уникальный мокап, не одинаковый template.
2. **TL;DR card** (3-5 буллетов)
3. **Real research** — WebFetch на оф. доки, GitHub source, meta-форумы. Цитировать конкретные имена методов/файлов.
4. **First-hand артефакт** — обязательно. Без рабочего кода / конфига / бенчмарка / debug-table статья не публикуется.
5. **Cross-link block** — 4 sibling-статьи + back to hub
6. **FAQ** (5-7 Q&A) + FAQPage JSON-LD
7. **Article JSON-LD** с author bylines

#### ⛔ Что НЕ палить на user-facing страницах

- "N mo. searches" / "KD X" / любые метрики поискового объёма
- "Targeted keyword:" / "SEO score:" / "Vol/KD"
- "We wrote this to rank for X"
- AI-template phrasing: "In this comprehensive guide", "Without further ado", "Buckle up", "Let's dive in"
- Дубль одной и той же структуры через все 5 статей (это паттерн scaled-content abuse, см. [google-2026-content-strategy.md](google-2026-content-strategy.md))

Внутренние трекинги (search vol, KD, target keyword) живут только в:
- Commit messages
- `docs/keywords/libs/<slug>.md` per-lib backlogs
- `docs/keywords/libs/_summary.md`, `_pain-points.md`
- GitHub issue threads

#### Источник трафика — профильные форумы

Hub-страница = landing для трафика с meta.discourse.org / r/selfhosted / HN / профильных форумов. Эта аудитория мгновенно палит SEO-bait. Поэтому:
- Honest disclaimer ОБЯЗАТЕЛЬНО (форумные читатели агрессивно проверяют "кто это и зачем")
- Текст в первом лице ("we tested", "we measured") с реальными артефактами (бенчи, конфиги, скриншоты)
- Author byline видимый
- Hub-страница это handbook FOR self-hosters, написанный self-hosters'ами — не SaaS-мaркетинг

#### Cluster execution flow

1. Создать папки `/root/vibers/<lib>/{slug1,slug2,slug3,slug4,slug5}/`
2. Hub писать самому (по референсу `/root/vibers/discourse/index.html`)
3. 5 cluster articles запустить параллельно через Agents (каждый агент пишет 1 статью с полным research через WebFetch)
4. После всех 5 — обновить nginx (regex `^/(...|<lib>)(/|$)` в `/etc/nginx/sites-available/onout.org`)
5. Live-тест 6 URL → 200 OK
6. Commit + push с "How to test" в теле, comment на issue #69 с прогрессом

Reference cluster: `/root/vibers/discourse/` (1 hub + 5 articles, написан 2026-05-01).
| [marker-io-keyword-insights.md](marker-io-keyword-insights.md) | **NEW** Анализ marker.io 4431 KW: топ-кластеры, "free" intent, чего НЕ копировать. |
| [WIKI.md#seo-intelligence](WIKI.md#seo-intelligence-april-2026) | Google March 2026 Core Update итоги + Claude SEO Prompts methodology |

### Marketplace Cover Banners

Для Kwork и похожих маркетплейсов использовать сохраненный HTML-паттерн из [marketplace-cover-banners.md](marketplace-cover-banners.md).

Текущий удачный формат:
- `660x440` PNG, без бокового кропа в карточке Kwork.
- CMS-логотип и название видны сразу.
- Четкий посыл: `Проблема -> Работа -> Фикс`.
- Визуальный стиль похож на SimpleReview: браузерная карточка, белый фон, оранжевый CTA, минимум декоративного шума.

Исходники HTML хранятся в `/root/kwork/cover-html/*.html`, финальные PNG — в `/root/kwork/covers/*.png`.

### Directory Submission Targets (из бэклинков конкурентов, 2026-04-18)

Полный список: `backlinks/submission-targets-from-competitor-backlinks.csv`

**Каталоги для сабмишена Vibers/SimpleReview** (DS ≥ 15, не конкуренты):

| DS | Domain | Тип | Приоритет |
|----|--------|-----|-----------|
| 58 | webcatalog.io | App catalog | HIGH |
| 41 | softwareworld.co | SaaS directory | HIGH |
| 36 | saashub.com | SaaS directory | HIGH |
| 30 | glama.ai | AI tools directory | HIGH |
| 28 | subscribed.fyi | SaaS discovery | HIGH |
| 26 | huntscreens.com | Product gallery | MED |
| 16 | digtize.com | Software directory | MED |
| 15 | wpm.so | SaaS directory | MED |
| 5 | rightfeature.com | Product directory | LOW |
| 6 | whatarethebest.com | Software comparison | LOW |

**Площадки для контента** (статьи/упоминания):

| DS | Domain | Формат |
|----|--------|--------|
| 85 | substack.com | Newsletter guest post |
| 66 | dev.to | Technical article |
| 44 | indiehackers.com | Founder story post |

**Конкуренты из этого же списка** (мониторить, не сабмитить):

| DS | Domain | Чем занимается |
|----|--------|---------------|
| 40 | bugherd.com | Visual feedback (agencias) |
| 36 | filestage.io | Design/file review |
| 31 | atarim.io | Visual feedback for WordPress |
| 29 | webvizio.com | Web annotation tool |
| 22 | bugsmash.io | Bug reporting widget |
| 19 | pageproofer.com | Page proofing tool |
| 44 | featurebase.app | Feature request board |

### Content Strategy (rebuilt 2026-04-18 after Google March 2026 analysis)

**Главное правило:** см. [google-2026-content-strategy.md](google-2026-content-strategy.md). Не делать кластерный спам — Google режет scaled content abuse. Каждая статья = original data + first-hand expertise + Information Gain.

**Стратегия — bug-cluster:** owning 3 узких ниш где у нас demonstrable expertise (см. [bug-cluster-research.md](bug-cluster-research.md)):

1. **WordPress/WooCommerce visual + checkout bugs** — Noxon NFTsy plugin moat
2. **React state/effect bugs в AI-coded apps** — MultiCurrencyWallet (540⭐) expertise
3. **Web3 wallet/DEX UX bugs** — unifactory, MCW, definance expertise

Каждая статья: 1 конкретный баг + интерактивный live-баннер с демкой бага + flow "fix uploaded to site" + реальная отсылка к коду из Noxon-репо.

**Опубликовано в bug-cluster (2026-04-18):**
- [x] `/blog/react-usestate-not-updating/` — vol ~929k SO views, KD high. С live-баннером (broken counter → SimpleReview → fixed counter)

**Опубликовано в alternative-кластере (2026-04-18):**
- [x] `/blog/markerio-alternative/` — KD 1-3, "free alternative" intent
- [x] `/blog/bugherd-alternative/` — KD 2
- [x] `/blog/usersnap-alternative/` — KD 4
- [x] `/blog/bug-report-template/` — vol 720, KD 33 (Marker.io top blog page)

**Backlog (next, по приоритету ROI):**
- [ ] React useEffect missing dependency (vol ~1.25M SO views) — pattern 2 in bug-cluster
- [ ] React useEffect runs twice / StrictMode (598k views) — wallet connect example
- [ ] React Hydration failed (687k views)
- [ ] WooCommerce add to cart not working — A-tier visual demo
- [ ] WordPress white screen of death — common WP nightmare
- [ ] MetaMask connect wallet does nothing — Web3 cluster opener

**Существующие, нужно усилить (Information Gain refresh — каждые 60-90 дней):**
- [ ] Все статьи: добавить original data — реальные PR-кейсы, time-to-fix, конкретные diffs
- [ ] Все статьи: добавить E-E-A-T author bio с github.com/noxonsu, MCW 540⭐
- [ ] `code-review-as-a-service`, `claude-code-review` — обновить с реальными бенчмарками

**ANTI-roadmap (НЕ делать — выйдем за core expertise):**
- ❌ UAT software/template hub (147k vol суммарно, но не наша ниша)
- ❌ Voice of customer template, design review software, tree testing — adjacent но не наше
- ❌ Programmatic SEO `/review/{tool}-code` — выглядит как scaled abuse в глазах Google March 2026

**People Also Ask (для FAQ-секций):**
- "What is the best free website for code reviews?"
- "How to review pull requests as a software engineer?"
- "How often should I be reviewing pull requests?"
- "How Can You Streamline the Code Review Process?"
- "What does a detailed code review look like?"

### SEO Intelligence (April 2026)

**Google March 2026 Core Update — итоги (Alex Groberman, @alexgroberman, 2026-04-14)**
Источник: https://x.com/i/status/2044080004842303818

Ключевые данные:
- Обновление длилось 12 дней (27 марта — 8 апреля 2026), одно из самых волатильных в истории Google
- 55%+ отслеживаемых доменов получили измеримые изменения в ранжировании
- 71% affiliate-сайтов пострадали (тонкие сравнения, шаблонные обзоры, рерайт)
- Сайты с оригинальными данными/исследованиями получили +22% видимости (анализ 600K+ страниц, JetDigitalPro)
- Типичное падение проигравших: 20-35%, у сильнейших страниц — более 50%
- Information Gain теперь прямой ранжирующий фактор: страницы, не добавляющие ничего нового к существующим результатам, проигрывают
- Topical Authority: сайт на 10 несвязанных тем оценивается хуже, чем сайт на 2 темы с глубиной
- Пример: HubSpot потерял ~80% органического блог-трафика (14.8M → 2.8M) после расширения в нерелевантные темы
- Победители: gov/institutional домены, сайты с экспертной атрибуцией, first-hand experience, third-party citations

Что это значит для Vibers:
- Наш контент уже на правильном пути (узкая ниша code review, экспертный опыт)
- Нужно усилить: оригинальные данные в статьях (benchmarks из реальных ревью, статистика багов)
- Прунинг: не расширяться за пределы code review / vibe coding / AI quality
- Экспертная атрибуция: добавлять авторов, их опыт, ссылки на профили

**10 SEO-промптов для Claude Cowork (Charles Floate, @Charles_SEO, 2026-04-14)**
Источник: https://x.com/i/status/2044010207458853314

Методология SEO через Claude Projects + Skills:
1. Prompt Zero — Business Context (загрузить в Project instructions, 30-45 мин на заполнение)
2. SERP Consensus Analyzer — анализ формата, DR, ссылочных профилей, entity-сигналов топа
3. Competitor Content Consensus Mapper — структурный анализ контента конкурентов (нужен Firecrawl MCP)
4. OnPage NLP & Entity Audit — entity relationships, topical completeness, information gain
5. Money Page Writer — CRO-оптимизация посадочных с учётом SEO-сигналов
6. Supporting Content Researcher — кластеры поддерживающего контента + internal linking
7. Supporting Content Writer — драфты на 80-90% готовности (нужен human editor!)
8. Brand Entity Stack — аудит brand entity signals (Wikipedia, Wikidata, Knowledge Graph)
9. Link Profile Analyzer — сегментация ссылок по tier/quality/anchor (лучше с Ahrefs MCP)
10. Link Bait Researcher — реверс-инжиниринг контента с 50+ referring domains в нише
11. SEO Dashboard Builder — кастомный дашборд как Claude Artifact
12. Self-Audit QA Gate — финальный QA перед публикацией

Ключевые инсайты для нас:
- Подход "Claude Project per business" — мы уже так работаем
- Skills для повторяющихся задач — у нас есть seo-content-writer, можно усилить по его схеме
- SERP Consensus перед написанием контента — внедрить в наш workflow
- Entity Audit — проверить наши статьи на entity coverage
- QA Gate как финальный шаг — добавить в наш seo-content-writer skill

**TODO (из инсайтов выше):**
- [ ] Добавить оригинальные данные в существующие статьи: реальная статистика багов из наших ревью, benchmarks time-to-fix, примеры найденных уязвимостей
- [ ] Внедрить SERP Consensus Analysis перед написанием новых статей (анализ топ-10 перед созданием контента)
- [ ] Добавить экспертную атрибуцию: авторы статей с именами, должностями, ссылками на профили
- [x] Entity Audit существующих статей — проверить entity coverage vs конкуренты (done 2026-04-15, see docs/entity-audit-2026-04-15.md)
- [ ] Добавить QA Gate в seo-content-writer skill (финальная проверка перед публикацией)
- [ ] Создать proprietary research piece: "50 Real Bugs AI Missed" на основе данных из реальных ревью
- [ ] Проверить topical focus: не расширяемся ли за пределы code review / vibe coding / AI quality

### Existing Blog Articles

| Slug | Target Keyword | Cluster |
|------|---------------|---------|
| `react-usestate-not-updating` | react usestate not updating | **Bug-cluster (NEW 2026-04-18, live banner)** |
| `bug-report-template` | bug report template | Template (NEW 2026-04-18) |
| `markerio-alternative` | marker.io alternative / free | Alternative (NEW 2026-04-18) |
| `bugherd-alternative` | bugherd alternative | Alternative (NEW 2026-04-18) |
| `usersnap-alternative` | usersnap alternatives | Alternative (NEW 2026-04-18) |
| `markerio-vs-vibers` | marker.io vs vibers | Comparison |
| `coderabbit-alternative-human-review` | coderabbit alternative | Alternative |
| `coderabbit-vs-human-review` | coderabbit vs human review | Comparison |
| `code-review-as-a-service` | code review as a service | Landing |
| `best-ai-code-review-tools` | best ai code review tools | Listicle |
| `claude-code-review` | claude code review | Landing |
| `best-chrome-extensions-ai-code-review` | best chrome extensions for ai code review | Listicle |
| `ai-code-review-bots-miss-bugs` | ai code review bots miss bugs | Hot take |
| `human-in-the-loop-code-review-teams` | human in the loop code review | Landing |
| `ai-generated-code-security-vulnerabilities` | ai generated code security vulnerabilities | Security |
| `review-cursor-generated-code` | review cursor generated code | Landing |
| `how-to-test-ai-generated-code` | how to test ai generated code | Guide |
| `ai-writes-code-who-verifies` | ai writes code who verifies | Hot take |
| `review-vibe-coded-app-before-launch` | review vibe coded app before launch | Landing |
| `vibe-coded-app-production-ready` | vibe coded app production ready | Landing |
| `vibe-coding-mistakes-production` | vibe coding mistakes production | Listicle |
| `vibe-coding-security-risks` | vibe coding security risks | Security |
| `claude-ai-performance-issues` | claude ai performance issues | Issue guide |

## Multilingual CMS Articles

CMS marketplace hubs use split domains by language. English pages are canonical on `https://onout.org/[cms]/`; Russian pages are canonical on `https://habab.ru/[cms]/` and are served by habab from `/root/vibers/[cms]/index.ru.html`.

### CMS coverage index (2026-05-05)

Source of truth for **currently shipped CMS hubs** is code, not memory:

- `scripts/generate-onout-sitemap.py` → `CMS_SLUGS` controls clean `/[cms]/` routes included in `generated/onout-sitemap.xml`.
- `scripts/lint-cms-hubs.py` → `CMS_HUBS` controls SEO/i18n/banner validation for hub pages.
- `README.md` → public project-level summary table.
- This wiki section → operational checklist for forum links, content planning, and future CMS phases.

Live indexed CMS hubs (35):

| Phase | CMS / platform | Slug | Public URL | RU sibling |
|-------|----------------|------|------------|------------|
| 1 | WordPress | `wordpress` | https://onout.org/wordpress/ | — |
| 1 | 1C-Bitrix | `bitrix` | https://onout.org/bitrix/ | https://habab.ru/bitrix/ |
| 1 | Magento / Adobe Commerce | `magento` | https://onout.org/magento/ | — |
| 1 | Joomla | `joomla` | https://onout.org/joomla/ | — |
| 1 | PrestaShop | `prestashop` | https://onout.org/prestashop/ | — |
| 1 | CS-Cart | `cs-cart` | https://onout.org/cs-cart/ | — |
| 1 | Webasyst / Shop-Script | `webasyst` | https://onout.org/webasyst/ | https://habab.ru/webasyst/ |
| 1 | OpenCart | `opencart` | https://onout.org/opencart/ | — |
| 1 | Shopware | `shopware` | https://onout.org/shopware/ | — |
| 1 | Drupal | `drupal` | https://onout.org/drupal/ | — |
| 1.5 | WooCommerce | `woocommerce` | https://onout.org/woocommerce/ | — |
| 2 | MODX | `modx` | https://onout.org/modx/ | — |
| 2 | Strapi | `strapi` | https://onout.org/strapi/ | — |
| 2 | Directus | `directus` | https://onout.org/directus/ | — |
| 2 | Craft CMS | `craft-cms` | https://onout.org/craft-cms/ | — |
| 2 | Statamic | `statamic` | https://onout.org/statamic/ | — |
| 2 / 5 | Payload CMS | `payload-cms` | https://onout.org/payload-cms/ | — |
| 2 | Umbraco | `umbraco` | https://onout.org/umbraco/ | — |
| 2 | nopCommerce | `nopcommerce` | https://onout.org/nopcommerce/ | — |
| 2 | DNN | `dnn` | https://onout.org/dnn/ | — |
| 2 | Concrete CMS | `concrete-cms` | https://onout.org/concrete-cms/ | — |
| 2 | TYPO3 | `typo3` | https://onout.org/typo3/ | — |
| 1.5 | Open WebUI (LLM admin) | `open-webui` | https://onout.org/open-webui/ | — |
| 1.5 | Dify (LLM workflow) | `dify` | https://onout.org/dify/ | — |
| 1.5 | Cal.com (booking) | `cal-com` | https://onout.org/cal-com/ | — |
| 1.5 | PostHog (analytics) | `posthog` | https://onout.org/posthog/ | — |
| 1.5 | Ghost (CMS / blog) | `ghost` | https://onout.org/ghost/ | — |
| 1.5 | Hashnode (hosted blog API) | `hashnode` | https://onout.org/hashnode/ | — |
| 1.5 | Storyblok (SaaS visual editor) | `storyblok` | https://onout.org/storyblok/ | — |
| 1.5 | Contentstack (enterprise SaaS) | `contentstack` | https://onout.org/contentstack/ | — |
| 1.5 | Decap CMS (git-based) | `decap-cms` | https://onout.org/decap-cms/ | — |
| 1.5 | Hygraph (GraphQL SaaS, 7 regions) | `hygraph` | https://onout.org/hygraph/ | — |
| 1.5 | DatoCMS (visual SaaS) | `datocms` | https://onout.org/datocms/ | — |
| 1.5 | TinaCMS (git-based local) | `tinacms` | https://onout.org/tinacms/ | — |
| 1.5 | KeystoneJS (TypeScript+Prisma) | `keystonejs` | https://onout.org/keystonejs/ | — |

Separate platform cluster, not part of `CMS_SLUGS` yet:

| Platform | Disk path | Public URL | Notes |
|----------|-----------|------------|-------|
| Discourse | `/root/vibers/discourse/` | https://onout.org/discourse/ | 1 hub + 5 researched articles, reference cluster for self-hosted/software-platform pages. Add to sitemap/nginx intentionally if we want it treated like CMS hubs. |

Planned CMS/platform backlog from GitHub issue #66 (no `/root/vibers/<slug>/index.html` yet unless listed above):

| Phase | Group | Candidates |
|-------|-------|------------|
| 3 | Flat-file / Git-based CMS | Grav, Bludit, Kirby, Decap CMS, Keystatic, Publii, Front Matter CMS, JekyllPad, Pages CMS, Sitepins, GitCMS, StudioCMS. Pico is intentionally skipped because it is deprecated. |
| 4 | RU/CIS source-available CMS | UMI.CMS, NetCat, HostCMS, DataLife Engine (DLE), Amiro.CMS |
| 5 | Open-source headless CMS (self-hostable) | KeystoneJS, TinaCMS, Static CMS, Squidex, dotCMS, October CMS, Ghost, ApostropheCMS, Cosmic, Caisy, Crystallize, Decap CMS, Spinal, Vault CMS. Payload CMS, Strapi, Directus are already live. |
| 5a | SaaS headless CMS (commercial, traffic exists) | Contentful, Sanity, Hygraph (former GraphCMS), Storyblok, DatoCMS, Kontent.ai (former Kentico Kontent), Contentstack, Builder.io, Prismic, ButterCMS, microCMS, Flotiq, Prepr CMS, CloudCannon, Hashnode. |
| 5b | Enterprise headless CMS | Sitecore XM, Optimizely CMS (former Episerver), Adobe Experience Manager (AEM). Low self-host fit but search volume exists. |
| 5c | Static-site / git-flow CMS variants | Craft Cross CMS — note: this looks like a typo in the source list, treat as Craft CMS sibling and verify before pulling Semrush keys. |
| 6 | Python CMS | Wagtail, django CMS, Plone, Mezzanine |
| 7 | .NET CMS | Orchard Core, Piranha CMS. Umbraco is already live. |
| 8 | Java CMS / portals | OpenCms, Liferay Portal, Jahia |
| 9 | Ruby/Rails CMS | Refinery CMS, Comfortable Mexican Sofa, LocomotiveCMS |
| 10 | E-commerce frameworks | Sylius, Saleor |

When adding a new CMS hub, update all four places in the same task: `scripts/generate-onout-sitemap.py`, `scripts/lint-cms-hubs.py`, `README.md`, and this wiki's **CMS announcement links** table. Then run `timeout 30s scripts/generate-onout-sitemap.py` and `timeout 30s scripts/lint-cms-hubs.py`.

## 2026-05-07 deploy notes (Issue #69 closeout, Issue #70 in progress)

**4 first-hand articles + voiced banners shipped:**

| Lib | URL | Banner | Real artifact captured |
|-----|-----|--------|------------------------|
| Open WebUI | https://onout.org/open-webui/ | `banner_voiced.mp4` | `host.docker.internal` doesn't resolve on Linux Docker → silent `{"models":[]}` |
| Dify 1.14.0 | https://onout.org/dify/ | `banner_voiced.mp4` | `plugin_daemon` panic-loop without `--profile=postgresql` flag |
| Cal.com 6.16.1 | https://onout.org/cal-com/ | `banner_voiced.mp4` | Image doesn't run `prisma migrate deploy` on boot; needs undocumented `DATABASE_DIRECT_URL` |
| PostHog hobby | https://onout.org/posthog/ | `banner_voiced.mp4` | Compose pull fails on empty `REGISTRY_URL`; 19 GB images; "really need 8GB" warning |

**Approach:** rejected the pre-scheduled "4 hubs × 5 cluster articles via parallel agents" plan as scaled-content abuse per Google March 2026 spam policy (`developers.google.com/search/docs/essentials/spam-policies`, last updated 2026-04-13). Replaced with one honest first-hand article per lib — actually deploy on this VM, capture real broken state, document fix. Same rule going forward: **no first-hand artifact = don't ship the article.**

**Headless CMS Semrush research (Issue #70):**

- 33 CSVs in `docs/keywords/headless-cms-2026-05-07/` (broad-match, US, single-seed-per-CMS)
- Summary at `docs/keywords/headless-cms-2026-05-07/_summary.md` with tier rec
- **Tier 1 (≥1k brand kw):** Storyblok, Ghost, Contentstack, Hashnode, Decap CMS — viable for first-hand articles
- **Tier 2 (170–590):** Hygraph, DatoCMS, Sitecore XM, ButterCMS, TinaCMS, Kontent.ai, Prismic, Optimizely, KeystoneJS, ApostropheCMS — comparison-page material
- **Tier 3 (<170):** the rest — round-up only
- **Re-run queue:** `sanity` (timed out), `crystallize` / `contentful` / `builder.io` / `keystatic` / `vault-cms` (bare-name seeds pulled non-product noise — re-query with disambiguating terms)
- **Bogus entry:** "Craft Cross CMS" is not a real product (working list = 41, not 42)

**Banner recording params (memory):** Emulation viewport 800×460, ScreenCast maxWidth 800, ffmpeg crop `720:446:40:0`, 14.714 fps (412 frames / 28 s), TTS via OpenAI tts-1 voice=nova, 4 segments mixed via `adelay+amix`. Recorder script: `scripts/record-article-banner.js`.

## First-hand article writing playbook

Used for the 4 lib articles on 2026-05-07 + Ghost on the same day. Replaces the
"5-cluster-articles-per-hub by parallel agents" pattern that violates Google
2026 spam policy.

**Goal:** every article ships with at least one first-hand artifact — a real
config we ran, a benchmark we measured, a real screenshot of a real broken
state. **No first-hand artifact = don't ship the article.**

### The pattern

1. **Pick the lib + the angle.** One narrow angle per article (e.g. "default
   docker run on Linux fails because X"), not a comprehensive guide. The
   broken state IS the angle.

2. **Pull the official image.** `docker pull ghcr.io/<org>/<image>:tag`.
   Record the digest — `sha256:…` goes into the article footer for traceability.

3. **Run with the most-naive config a docs reader would copy.** Skip
   custom env vars, skip the install script. The friction the article is
   about lives in the gap between "what the README says works" and "what
   actually works".

4. **Capture the broken state to the disk.**
   - Container logs: `docker logs <name> 2>&1 > /root/vibers/<slug>/assets/_logs.txt`
     (only if useful as artifact — usually we just paste the relevant lines into the article)
   - Screenshots: use the chrome-screen daemon, NOT a fake mockup:
     ```bash
     CDP_PORT=9223 node /root/tools/chrome-daemon/screenshot-model.js \
       "http://172.17.0.1:<port>/<route>" \
       /root/vibers/<slug>/assets/01-<state>.jpg
     ```
     The container listens on the host's docker0 gateway IP (`172.17.0.1`) which
     chrome-screen sees from the same network. Use the running container's
     actual hostname/IP, not the bind port from `localhost` on the host.
   - Resource numbers: `docker stats --no-stream <name>` gives RSS / CPU /
     I/O. Take a snapshot at idle and one under load if relevant.

5. **Verify the image is real.** Read the JPG back via the Read tool — confirm
   the screenshot shows what we claim (correct admin panel, real error text,
   target element in the right place). Fake-looking mockups are caught here.

6. **Apply the fix, capture the recovered state.** Same pattern — `docker run`
   with corrected env, take a second screenshot of the working state. The
   article needs to demonstrate both halves of the broken→fixed transition.

7. **Stop the container and clean up the docker volume only after the article
   is committed.** Removing the volume too early loses the screenshots' source
   of truth if a reviewer asks "show me that error again". Confirm with user
   before destructive `docker rm -f` or `docker volume rm` — the harness will
   warn but the user-confirmation is the policy.

8. **Write the article.** Structure:
   - Honest disclaimer callout (who we are, who we're NOT affiliated with)
   - The exact `docker run` we used
   - The broken-state log (verbatim, in `<pre><code>`)
   - `.callout-broken` block with one-paragraph diagnosis
   - The fix in a `.callout-fix` block
   - `<figure>` with the real screenshot
   - Resource table with the numbers we measured
   - Quiet warnings worth knowing about
   - "Things we'd change in the README" — concrete, opinionated
   - Cross-links to adjacent articles + back to onout.org/ for SimpleReview

9. **Banner.** Animated CSS banner per `animated-banner` skill, with a mockup
   admin/UI that matches THIS article (not a template across many articles).
   Record via `scripts/record-article-banner.js`, TTS via OpenAI tts-1, embed
   YouTube iframe after upload. Banner is the demo of SimpleReview catching
   the same error the article describes.

### Why this beats parallel-agent cluster generation

- Each article has a real artifact a reviewer can verify.
- The friction is real — Google's helpful-content signal recognizes first-hand
  experience.
- Forum / HN / Reddit audiences (where these articles get linked) can
  immediately tell SEO-ghost-written prose from someone who actually ran the
  thing. Trust signal compounds.
- Slower per article (~1 hour vs ~5 minutes for template prose) but the
  per-article ROI is order-of-magnitude higher because of the rate it gets
  cited in tool comparisons and stack-overflow answers.

### Quick reference — chrome-screen daemon
- Port: `9223` (Xvfb-backed, real rendering — for screenshots)
- Port `9222` is the headless one — DO NOT use for screenshots, use for console/CDP tests
- Daemon stays in pm2, just point it at a new URL via `PUT /json/new?<encoded-url>`
- Script: `/root/tools/chrome-daemon/screenshot-model.js <url> <output.jpg>`

Rules for adding or editing multilingual articles:

- Keep canonical, `og:url`, BlogPosting `url`, and BlogPosting `mainEntityOfPage.@id` on the public canonical URL for that language.
- On EN pages, hreflang `en` and `x-default` point to onout. If RU exists, hreflang `ru` points to habab.
- On RU pages, hreflang `ru` points to habab, and `en`/`x-default` point to onout.
- Add every new RU CMS hub to `VIBERS_CMS_PAGES` in `/root/space2/hababru/src/backend/routes/main_routes.py`; do not rely on nginx to serve RU pages from onout.
- Regenerate `https://onout.org/sitemap.xml` with `timeout 30s scripts/generate-onout-sitemap.py`; nginx serves that file from `/root/vibers/generated/onout-sitemap.xml`.
- Validate before release with `timeout 30s scripts/lint-cms-hubs.py`; validate production with `timeout 30s scripts/lint-cms-hubs.py --live`.

## Product Evaluation

| Doc | Description |
|-----|-------------|
| [prototyping-criteria.md](prototyping-criteria.md) | Criteria for evaluating the product prototype |
| [evaluation-round-1.md](evaluation-round-1.md) | First evaluation round results |
| [evaluation-round-2.md](evaluation-round-2.md) | Second evaluation round results |
| [improvement-log.md](improvement-log.md) | Log of improvements made |
| [simple-review-usage-analysis/INSIGHTS.md](simple-review-usage-analysis/INSIGHTS.md) | **Opinion — not direction** (2026-04-18). Анализ 93 реальных Fix-It-ов (tamara/maria/julia, 8 дней) joined к .entire-сессиям Claude. Выводы: non-dev shipper = ICP, deployed fix (не PR) = deliverable, full-stack (JS+Python) = scope, issue-anchored Claude session = истинная природа продукта. **Гипотезы, не утверждённое направление.** |
| [../../../office-hours-designs/2026-04-18-simple-review-split-positioning-design.md](../../../office-hours-designs/2026-04-18-simple-review-split-positioning-design.md) | **Opinion — not direction.** /office-hours дизайн-док по split-positioning (`/simple-review/` team + `/simple-review/solo/`) и issue-anchoring feature. Premise review, 4 personas (QA, editor, solo non-dev, manager-client), assignment = ship issue-auto-link Phase 1 на claritycult. Не утверждено, ждёт решения. |

### SimpleReview usage analysis — raw data (2026-04-18)

**Статус: гипотезы/мнение, не решение.** Перед действием — второй клиент + разговор с Tamara.

- `/root/op.wpmix.net/prompt-logs/` — historical + live prompt persistence (JSONL per day)
- `/root/vibers/docs/simple-review-usage-analysis/` — INSIGHTS.md, joined-sessions.jsonl, outcomes.jsonl
- Surfaced persona mismatch (лендинг vs реальность), potentially killer feature (issue-auto-link), new ICP breadth (команды + solo + manager-client)

## Community

| Doc | Description |
|-----|-------------|
| [../CONTRIBUTING.md](../CONTRIBUTING.md) | Contribution guidelines (public) |
| [../SECURITY.md](../SECURITY.md) | Security policy (public) |
| [../.github/ISSUE_TEMPLATE/](../.github/ISSUE_TEMPLATE/) | Issue templates (bug, feature, review request) |

## Key Numbers

| Metric | Value | Source |
|--------|-------|--------|
| Target keyword (best) | "code review as a service" | KD=1, Vol=110 |
| Highest CPC keyword | "hire remote code review devs" | $73.97 |
| Main competitor | CodeRabbit | $24/user/mo, 15K+ customers |
| Our price | $15/hr | Free promo available |
| First client | MethasMP/Paycif (Thailand) | 2026-03-23 |

## Software Directories & Placement Ideas

Где ещё можно разместить Vibers для получения трафика, backlinks и лидов.

> **Готовые наборы ассетов для заливки** (разделены по продуктам):
> - **Vibers** (human-in-the-loop, GitHub App): [listing-assets.md](listing-assets.md)
> - **SimpleReview** (Chrome Extension, AI → site-ready fix): [simple-review-listing-assets.md](simple-review-listing-assets.md)
>
> Внутри каждого — pitch'и всех длин, скриншоты, FAQ, теги, UTM-инструкция.

### Общие каталоги SaaS/Software

| Платформа | URL | Приоритет | Примечание |
|-----------|-----|-----------|------------|
| Capterra | https://www.capterra.com/ | HIGH | Топ-1 по DR, платные отзывы, огромный трафик по "code review software" |
| G2 | https://www.g2.com/ | HIGH | B2B-аудитория, отзывы влияют на продажи |
| GetApp | https://www.getapp.com/ | MEDIUM | Сестра Capterra (тот же Gartner), дубль без усилий |
| Software Advice | https://www.softwareadvice.com/ | MEDIUM | Ещё одна Gartner-сеть, бесплатный листинг |
| TrustRadius | https://www.trustradius.com/ | MEDIUM | Больше для enterprise, хорошие backlinks |
| SourceForge | https://sourceforge.net/ | LOW | Старый DR 90, dev-аудитория, бесплатно |
| AlternativeTo | https://alternativeto.net/ | HIGH | Уже в issue #26 — размещение ведётся |
| SaaSHub | https://www.saashub.com/ | MEDIUM | Автоматически индексируется, можно claim |

### Launch-платформы (разовый буст)

| Платформа | URL | Приоритет | Примечание |
|-----------|-----|-----------|------------|
| Product Hunt | https://www.producthunt.com/ | HIGH | Разовый launch — потенциал сотни лидов за день |
| BetaList | https://betalist.com/ | MEDIUM | Pre-launch аудитория, waiting list |
| AppSumo | https://appsumo.com/ | LOW | Нужен разовый lifetime deal, работает для инструментов |
| Uneed | https://www.uneed.best/ | MEDIUM | Меньше PH, но проще попасть в топ |
| AI Product Launch | https://aiproductlaunch.vercel.app/ | LOW | Упомянут в чате (#6), быстрый сабмит |

### AI-инструменты каталоги

| Платформа | URL | Приоритет | Примечание |
|-----------|-----|-----------|------------|
| Futurepedia | https://www.futurepedia.io/ | HIGH | Крупнейший AI tools directory, DR 70+ |
| There's An AI For That | https://theresanaiforthat.com/ | HIGH | 10M+ посетителей/мес, хорошо индексируется |
| Toolify.ai | https://www.toolify.ai/ | MEDIUM | AI directory с SEO-трафиком |
| AI Tool Hunt | https://www.aitoolhunt.com/ | LOW | Небольшой, но бесплатный |
| PeerPush | https://peerpush.net/ | MEDIUM | Упомянут в чате (#6), discovery для AI-ассистентов |

### Dev-сообщества (не каталоги, но дают трафик)

| Платформа | URL | Приоритет | Примечание |
|-----------|-----|-----------|------------|
| GitHub Marketplace | https://github.com/marketplace | HIGH | Уже есть GitHub App — надо оформить листинг |
| Indie Hackers | https://www.indiehackers.com/ | MEDIUM | Пост о запуске + ссылка |
| Hacker News (Show HN) | https://news.ycombinator.com/ | HIGH | Разовый Show HN пост — аудитория именно dev-инструментов |

### Platform-specific forums for community placement (2026-04-30)

Задача: искать обсуждения конкретных платформ, где владельцы сайтов жалуются на баги, сломанные шаблоны, checkout, mobile layout, forms, custom code и AI/no-code сборки. Это не места для прямого спама "купите SimpleReview"; рабочий формат — полезный ответ, мини-разбор проблемы, раскрытие affiliation и ссылка только когда она реально помогает.

**Наш продукт — SimpleReview.** Главная страница onout.org/ — это лендинг SimpleReview ("Click any issue on your website. Get a code fix."). Chrome extension: кликаешь на проблему на сайте → получаешь code fix, который можно залить на сайт через Git, SFTP/SSH или обычный deploy-flow. Built-in AI mode, либо BYOK через Claude Code / Codex. Vibers (human-in-the-loop review через GitHub App) — отдельная вторичная линия, в форумных ответах НЕ упоминать, чтобы не размывать сообщение.

**Правила выбора ссылки в форумном ответе:**
- CMS-форум (WordPress, WooCommerce, OpenCart, PrestaShop, Joomla, Magento, Bitrix, MODX, Strapi, Directus, Drupal, Shopware, CS-Cart и т.п.) → CMS-специфичный лендинг: `https://onout.org/<cms>/` (например `/wordpress/`, `/woocommerce/`, `/opencart/`, `/prestashop/`, `/joomla/`, `/bitrix/`)
- Discourse / forum / self-hosting темы → Discourse cluster: `https://onout.org/discourse/` или deep article из `/discourse/.../`, если вопрос про SSO, email replies, migration, API, plugin development, production/self-hosting.
- Общий вебмастерский / SEO / hosting / web-dev форум (SitePoint, Habr, Namepros, webhostingdiscussion, lowendtalk, freecodecamp, HTMLForums и т.п.) → главная `https://onout.org/`
- SimpleReview-специфичный лендинг: `https://onout.org/simple-review/` (когда тема прямо про visual feedback / Marker.io alternatives)

#### CMS announcement links

Использовать эти URL как основной destination для форумных анонсов, marketplace profiles, подписи в профиле и мягких disclosure-ссылок. В анонсах вести на hub `/<cms>/`; deep article ссылать только когда тред реально про конкретный баг/кластер.

UTM-шаблон:
`?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement`

| CMS / platform | Announcement URL | UTM URL |
|----------------|------------------|---------|
| WordPress | https://onout.org/wordpress/ | `https://onout.org/wordpress/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| WooCommerce | https://onout.org/woocommerce/ | `https://onout.org/woocommerce/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| 1C-Bitrix | https://onout.org/bitrix/ | `https://onout.org/bitrix/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Magento / Adobe Commerce | https://onout.org/magento/ | `https://onout.org/magento/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Joomla | https://onout.org/joomla/ | `https://onout.org/joomla/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| PrestaShop | https://onout.org/prestashop/ | `https://onout.org/prestashop/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| CS-Cart | https://onout.org/cs-cart/ | `https://onout.org/cs-cart/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Webasyst / Shop-Script | https://onout.org/webasyst/ | `https://onout.org/webasyst/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| OpenCart | https://onout.org/opencart/ | `https://onout.org/opencart/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Shopware | https://onout.org/shopware/ | `https://onout.org/shopware/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Drupal | https://onout.org/drupal/ | `https://onout.org/drupal/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| MODX | https://onout.org/modx/ | `https://onout.org/modx/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Strapi | https://onout.org/strapi/ | `https://onout.org/strapi/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Directus | https://onout.org/directus/ | `https://onout.org/directus/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Craft CMS | https://onout.org/craft-cms/ | `https://onout.org/craft-cms/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Statamic | https://onout.org/statamic/ | `https://onout.org/statamic/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Payload CMS | https://onout.org/payload-cms/ | `https://onout.org/payload-cms/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Umbraco | https://onout.org/umbraco/ | `https://onout.org/umbraco/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| nopCommerce | https://onout.org/nopcommerce/ | `https://onout.org/nopcommerce/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| DNN | https://onout.org/dnn/ | `https://onout.org/dnn/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Concrete CMS | https://onout.org/concrete-cms/ | `https://onout.org/concrete-cms/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| TYPO3 | https://onout.org/typo3/ | `https://onout.org/typo3/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |
| Discourse | https://onout.org/discourse/ | `https://onout.org/discourse/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=cms_announcement` |

Источник из чата: приватная ChatGPT-ссылка `/c/69f30833-8508-8389-a94b-5ab7e00d468c` недоступна без аккаунта/публичного share URL (403). Ниже — сохранённая рабочая версия из открытых источников.

| Платформа | Куда идти | Приоритет | Что можно делать | Ограничения / риск |
|-----------|-----------|------------|------------------|--------------------|
| Shopify | https://community.shopify.com/ + гайд Shopify для app marketing: https://shopify.dev/docs/apps/launch/marketing | HIGH | Отвечать на темы про theme bugs, checkout UX, app conflicts, slow pages. Shopify прямо рекомендует создавать ценность в Community forums и предлагать app только если он решает проблему. | Не поднимать старые темы ради промо, не писать "contact me here" без полезного ответа. |
| Webflow | https://forum.webflow.com/ + guidelines: https://discourse.webflow.com/guidelines | HIGH для SimpleReview | Искать layout/design/CMS/mobile issues, давать конкретный CSS/структурный совет, затем мягко показывать SimpleReview как способ превратить visual bug в фикс для сайта. Можно отдельный Show & tell, если есть хороший кейс. | Guidelines прямо просят избегать advertising/spam и irrelevant comments. |
| Bubble | https://forum.bubble.io/ + guidelines: https://forum.bubble.io/guidelines | HIGH для no-code/AI-shippers | Отвечать на темы "my app broke", responsive issue, workflows/API bugs. Хороший угол: "no-code/AI app before launch sanity check". | Нужны полезные технические ответы, не чистый launch-пост. |
| Squarespace | https://forum.squarespace.com/ + guidelines: https://forum.squarespace.com/guidelines/ | MEDIUM | Отвечать на advanced customization, CSS, template, responsive bugs. Допустимо упоминать paid/service resource после бесплатной помощи и disclosure. | Forum просит lead with free help first, paid resources second; affiliation нужно указывать каждый раз. |
| Wix Studio | https://forum.wixstudio.com/ + code of conduct: https://www.wix.com/studio/community/code-of-conduct | MEDIUM/LOW | Только полезные ответы по site/editor issues, без прямой продажи. Лучше использовать как мониторинг болей и source для контента. | Code of Conduct говорит, что community не место для solicitation или commercial self-promotion. |
| WordPress.org | https://wordpress.org/support/forums/ + guidelines: https://wordpress.org/support/guidelines/ | MEDIUM для research, LOW для ссылок | Искать частые WP/WooCommerce баги для статей и кейсов; отвечать только полезно и без коммерческого pitch. | WordPress.org прямо запрещает advertising, paid help requests и promotion of services/plugins. |
| WooCommerce | https://woocommerce.com/community/ + https://wordpress.org/support/plugin/woocommerce/ | MEDIUM | Брать темы про checkout, cart, template overrides, plugin conflicts как идеи для статей и SimpleReview demos. | На официальных support-форумах действуют анти-рекламные правила WordPress; ссылки на сервис лучше не ставить. |
| Magento / Adobe Commerce | Magento forum sunset notice: https://community.magento.com/t5/News-Announcements/Magento-Community-Forum-Sunsetting-on-December-31-2025/m-p/572112 + community: https://developer.adobe.com/commerce/contributor/community/ + Magento StackExchange: https://magento.stackexchange.com/ | MEDIUM | Старый Magento forum закрыт 2025-12-31, идти в Slack/GitHub/StackExchange. Подход: технические ответы, кейсы по checkout/theme/module bugs. | StackExchange не любит overt self-promotion; если упоминаем Vibers/SimpleReview, раскрывать affiliation и делать это редко. |
| OpenCart | https://opencart.zendesk.com/hc/en-us/community/topics + OpenCart forum/marketplace rules example: https://opencartforum.com/en/faq/developers/rules/ | MEDIUM | Темы про extensions/theme checkout/layout bugs; лучше делать полезные ответы и отдельные статьи под OpenCart issues. | Для прямой рекламы нужны профильные разделы/marketplace; не дублировать рекламные сообщения. |
| PrestaShop | https://www.prestashop.com/forums/ | MEDIUM | Темы про theme/module/checkout bugs; готовить полезные ответы и затем отдельные SEO-страницы "fix PrestaShop issue". | Перед постингом проверять правила конкретного language-форума; Reddit r/prestashop имеет karma/account-age ограничения. |
| Drupal | https://www.drupal.org/forum + advertising policy: https://www.drupal.org/advertising | LOW/MEDIUM | Больше подходит для Vibers как review/debug service для custom Drupal work; можно отвечать на dev issues. | Рекламные возможности лучше через официальную Drupal advertising/sponsorship policy, не через support-spam. |
| Joomla | https://forum.joomla.org/ + forum rule note: https://community.joomla.org/blogs/community/small-modication-to-the-joomla-forum-rules.html | LOW/MEDIUM | Технические ответы по extensions/templates; контент-идеи для "Joomla site broken" pages. | Self-promotion и внешние ссылки на extensions ограничены; по extensions лучше ссылаться на JED, не на свой сайт. |
| Shopware | https://forum.shopware.com/ + community: https://developers.shopware.com/community/ | MEDIUM для EU ecommerce | Темы Shopware 6 layout/plugin/checkout issues, особенно English/German sections. | Перед постингом проверять актуальные forum guidelines; не использовать как рекламную доску. |
| CS-Cart | https://forum.cs-cart.com/ + guidelines: https://forum.cs-cart.com/guidelines | MEDIUM | Можно обсуждать CS-Cart/Multi-Vendor services/add-ons, dev issues, bug tracker. Хороший fit для ecommerce checkout/theme bug cases. | Guidelines запрещают нерелевантный spam; продукты для CS-Cart должны вести на marketplace.cs-cart.com, если это add-on/theme. |
| 1C-Bitrix | https://dev.1c-bitrix.ru/community/forums/index.php + rules: https://dev.1c-bitrix.ru/community/forums/rules/index.php | MEDIUM для RU | Темы про компоненты, шаблоны, интеграции, checkout/order flow; лучше как экспертные ответы и source для RU-статей. | Не делать массовую рекламу; соблюдать правила конкретного форума и не писать капсом/в стиле объявления. |

#### Как писать ответ в forum thread

1. Найти свежую тему с конкретной болью: broken checkout, mobile layout, form not submitting, plugin conflict, AI/no-code app regression.
2. Дать бесплатный diagnostic answer: 2-4 шага проверки, возможная причина, короткий код/настройка если очевидно.
3. Если ссылка уместна, раскрыть связь: "Disclosure: I work on SimpleReview." Затем одна ссылка с UTM (по правилу выбора лендинга выше).
4. Не писать одинаковые сообщения в разные темы. Для каждого форума вести 5-10 полезных ответов на 1 ссылку.

#### Шаблон мягкого упоминания (SimpleReview)

Для CMS-форума (подставить `<cms>`):

```
This looks like a frontend/regression issue rather than a platform-wide outage.
I would first check: [1] ..., [2] ..., [3] ...

Disclosure: I work on SimpleReview — a Chrome extension that turns visual bugs
into a site-ready code fix, not just a ticket. If a second pair of eyes would help
before launch, this is exactly the kind of issue we handle:
https://onout.org/<cms>/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=platform_forums
```

Для общего веб-форума:

```
https://onout.org/?utm_source=PLATFORM_FORUM&utm_medium=community&utm_campaign=platform_forums
```

### Статус размещений

| Платформа | Статус |
|-----------|--------|
| AlternativeTo | В процессе (issue #26) |
| GitHub Marketplace | Есть App, листинг не оформлен |
| Все остальные | Не начато |
