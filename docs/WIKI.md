# Vibers Wiki

Internal knowledge base. For the public README see [../README.md](../README.md).

---

## Product

| Doc | Description |
|-----|-------------|
| [../SKILL.md](../SKILL.md) | AI Agent skill — client-facing quickstart (English) |
| [../REVIEW-RUNBOOK.md](../REVIEW-RUNBOOK.md) | Step-by-step review workflow for reviewers |
| [../CLAUDE.md](../CLAUDE.md) | Claude Code project instructions |
| [../vibecheck/index.html](../vibecheck/index.html) | **VibeCheck** — Chrome Extension "Website Feedback & Fix Tool". Click element → Fix It → real PR. Beta, free first fix. Landing at `/vibers/vibecheck/` |

### VibeCheck — Visual Feedback & Fix Chrome Extension

**Positioning:** "Website Feedback & Fix Tool" — отличие от конкурентов: не просто репортит баг, а чинит (PR).

**Direct competitors (visual feedback tools):**

| Tool | Pricing | Target | Key diff vs VibeCheck |
|------|---------|--------|----------------------|
| **Marker.io** | $39/mo+ | Agencies, QA teams | Reports only. Session replay, console logs, 20+ integrations. No fixes, no PR. |
| **BugHerd** | $50/mo+ (5 seats) | Web agencies, UAT | "Sticky notes on a webpage." Client-friendly Kanban, no login for clients. No code fixes. G2 4.8/5 |
| **Usersnap** | $39-249/mo | Product/SaaS teams, PM | Enterprise: AI sentiment, surveys, SDK, 50+ integrations. No code access. |
| **Feedbucket** | 14-day trial, paid | Agencies + clients | Reports only, no dev fixes. Widget (no extension). |
| **Userback** | Freemium + paid | Product teams, SaaS | NPS, surveys, session replay, roadmap. No code fixes. 20K+ teams. |

**Key message:** All of them → ticket. VibeCheck → PR. All paid, VibeCheck free (BYOK).

**Alternative-статьи (опубликованы 2026-04-18):** `/blog/markerio-alternative/`, `/blog/bugherd-alternative/`, `/blog/usersnap-alternative/`. Все таргетят low-KD KWs (KD 1-4) + "free X" intent.

→ Полный анализ + "alternative to" messaging: [COMPETITORS.md#visual-feedback-tools](COMPETITORS.md#visual-feedback-tools-vibecheck-специфичные-конкуренты)
→ Marker.io keyword intelligence (4431 KW): [marker-io-keyword-insights.md](marker-io-keyword-insights.md)

## Marketing & SEO

| Doc | Description |
|-----|-------------|
| [COMPETITORS.md](COMPETITORS.md) | 11 competitors — pricing, features, SEO strategies, keywords |
| [competitive-research/](competitive-research/) | Ad copy analysis (SonarSource, Google Ads) |
| [keywords/](keywords/) | SEMrush keyword exports (6 CSV files, 2026-04-14) |
| [reddit-alpha-beta-users.md](reddit-alpha-beta-users.md) | Reddit strategy for finding alpha/beta users |
| [backlink-opportunities.md](backlink-opportunities.md) | 13 directories + 6 dev blogs + media pitch targets |
| [COMPETITORS.md#markerio-markerio](COMPETITORS.md) | Marker.io ($39/mo) + **Feedbucket** (agency feedback tool) + Markup.io (design, adjacent) — прямые конкуренты VibeCheck. Marker.io: контент-паттерн (template hubs, utility tripwire) в COMPETITORS.md |
| [advertising-channels.md](advertising-channels.md) | Полная карта рекламы: каталоги, ad networks, newsletters, стратегия по бюджету |
| [backlinks/](backlinks/) | Raw SEMrush backlink exports (CodeRabbit 4.6K, Qodo 6K domains); `submission-targets-from-competitor-backlinks.csv` — каталоги из бэклинков конкурентов |
| [topic-research-20260414.xlsx](topic-research-20260414.xlsx) | SEMrush Topic Research — 108 content ideas with volumes, questions, backlinks |
| [google-2026-content-strategy.md](google-2026-content-strategy.md) | **NEW** Google March 2026 правила: что банят (scaled abuse), что поднимают (Information Gain). Наша стратегия. |
| [bug-cluster-research.md](bug-cluster-research.md) | **NEW** 30 багов из SO + GitHub, классифицированы по VibeCheck fit и Noxon expertise. Roadmap на 5-10 статей. |
| [marker-io-keyword-insights.md](marker-io-keyword-insights.md) | **NEW** Анализ marker.io 4431 KW: топ-кластеры, "free" intent, чего НЕ копировать. |
| [WIKI.md#seo-intelligence](WIKI.md#seo-intelligence-april-2026) | Google March 2026 Core Update итоги + Claude SEO Prompts methodology |

### Directory Submission Targets (из бэклинков конкурентов, 2026-04-18)

Полный список: `backlinks/submission-targets-from-competitor-backlinks.csv`

**Каталоги для сабмишена Vibers/VibeCheck** (DS ≥ 15, не конкуренты):

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

Каждая статья: 1 конкретный баг + интерактивный live-баннер с демкой бага + наш PR-fix flow + реальная отсылка к коду из Noxon-репо.

**Опубликовано в bug-cluster (2026-04-18):**
- [x] `/blog/react-usestate-not-updating/` — vol ~929k SO views, KD high. С live-баннером (broken counter → VibeCheck → fixed counter)

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

## Product Evaluation

| Doc | Description |
|-----|-------------|
| [prototyping-criteria.md](prototyping-criteria.md) | Criteria for evaluating the product prototype |
| [evaluation-round-1.md](evaluation-round-1.md) | First evaluation round results |
| [evaluation-round-2.md](evaluation-round-2.md) | Second evaluation round results |
| [improvement-log.md](improvement-log.md) | Log of improvements made |
| [vibecheck-usage-analysis/INSIGHTS.md](vibecheck-usage-analysis/INSIGHTS.md) | **Opinion — not direction** (2026-04-18). Анализ 93 реальных Fix-It-ов (tamara/maria/julia, 8 дней) joined к .entire-сессиям Claude. Выводы: non-dev shipper = ICP, deployed fix (не PR) = deliverable, full-stack (JS+Python) = scope, issue-anchored Claude session = истинная природа продукта. **Гипотезы, не утверждённое направление.** |
| [../../../office-hours-designs/2026-04-18-vibecheck-split-positioning-design.md](../../../office-hours-designs/2026-04-18-vibecheck-split-positioning-design.md) | **Opinion — not direction.** /office-hours дизайн-док по split-positioning (`/vibecheck/` team + `/vibecheck/solo/`) и issue-anchoring feature. Premise review, 4 personas (QA, editor, solo non-dev, manager-client), assignment = ship issue-auto-link Phase 1 на claritycult. Не утверждено, ждёт решения. |

### VibeCheck usage analysis — raw data (2026-04-18)

**Статус: гипотезы/мнение, не решение.** Перед действием — второй клиент + разговор с Tamara.

- `/root/op.wpmix.net/prompt-logs/` — historical + live prompt persistence (JSONL per day)
- `/root/vibers/docs/vibecheck-usage-analysis/` — INSIGHTS.md, joined-sessions.jsonl, outcomes.jsonl
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

### Статус размещений

| Платформа | Статус |
|-----------|--------|
| AlternativeTo | В процессе (issue #26) |
| GitHub Marketplace | Есть App, листинг не оформлен |
| Все остальные | Не начато |
