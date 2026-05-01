# Pain-point keywords — actionable article candidates

**Source:** 38 self-hosted lib CSVs (Semrush US, 2026-05-01).
**Method:** 5 parallel agents each loaded their group of CSVs into context and hand-picked
keywords representing real solvable problems — not the regex pass that produced
`_summary.md`. Output cross-checked against Google's 2026 scaled-content stance.

## Why this list exists

Google's March 2026 core update penalised sites running templated AI content at scale —
50–80% traffic drops, manual actions, full deindexing for the worst offenders. SpamBrain
is now tuned to flag patterns: identical structure across hundreds of pages, swap-template
variants ("X vs Y" for every X and Y), thin first-pass walkthroughs without first-hand data.

This list deliberately avoids:

- `<lib> vs <lib>` comparison templates (every X×Y pair = mass-produced)
- `<lib> alternatives` listicles
- `What is <lib>?` cornerstones unless paired with an original angle
- `How to install <lib>` guides (covered by official docs; templated)
- Branded navigational queries (logo, GitHub, careers, valuation, login)
- Pricing pages

It keeps:

- Specific runtime errors with traceable root causes
- Feature configurations that aren't in official docs
- Integration walkthroughs where the article must contain working code/screenshots
- Migration / backup / upgrade pain that requires hands-on validation
- CVE/security articles where the writer must run the exploit in a lab

Articles written from this list MUST contain at least one of: a screenshot of the broken
state, a real config snippet that was tested, a benchmark number from our own measurement,
or a CVE PoC reproduced in our lab. No first-hand artifact = don't ship the article.

---

## Cross-lib top 20 priority queue

Sorted by `volume × KD-friendliness × E-E-A-T potential`. These are the articles where
the metric and the originality bar both line up — write these first.

| # | Lib | Keyword | Vol | KD | Why now |
|---|-----|---------|----:|---:|---------|
| 1 | **Appsmith** | `appsmith api params` | 590 | 10 | Param-binding gotchas affect every Appsmith dev; KD 10 is rare for that volume |
| 2 | **Appsmith** | `appsmith button input` | 590 | 20 | onClick chains drop actions silently; we can ship a working pattern |
| 3 | **Discourse** | `discourse develop plugin` | 880 | 6 | Outstanding KD/vol, plugin API has changed three times — original walkthrough |
| 4 | **Dify** | `dify internal server error` | 480 | 0 | Generic 500 has 4-5 known root causes; perfect diagnostic-tree article |
| 5 | **Dify** | `dify how to handle request output from api` | 480 | 0 | Workflow API node parsing — real DSL YAML required |
| 6 | **Dify** | `dify-sandbox` (cluster) | 480 | 1 | Sandbox container fails silently — strace + seccomp content needed |
| 7 | **Open WebUI** | `open webui 500 internal error` | 260 | — | DB lock / sqlite migration tree; evergreen, easy to keep updated |
| 8 | **PostHog** | `posthog nextjs` | 260 | 0.10 | App Router instrumentation breaks SSR — every Next dev hits this |
| 9 | **Discourse** | `discourse api documentation` | 220 | 6 | API auth split + rate limits undocumented — working Python+curl client |
| 10 | **Cal.com** | `cal.com embed` | 220 | 0 | Iframe height + theming — real broken-state screenshots possible |
| 11 | **Budibase** | `how to connect supabase to budibase` | 210 | 14 | RLS + JWT pass-through — undersaturated, hands-on required |
| 12 | **Snipe-IT** | `snipe it api` (recipes) | 210 | 0.18 | "10 real Snipe API recipes" — most-searched dev resource |
| 13 | **Cal.com** | `cal.com api` | 160 | 0–0.42 | v2 REST + booking creation — concrete original code |
| 14 | **EspoCRM** | `espocrm lead scoring` | 180 | — | Espo has NO native scoring — workaround article for frustrated users |
| 15 | **ToolJet** | `how to connect supabase to tooljet` | 170 | 23 | Same Supabase pain as Budibase, distinct stack |
| 16 | **OpenProject** | `openproject docker` (cluster) | 300 | 31 | Production compose with backups + reverse proxy in one file |
| 17 | **Cal.com** | `migrate from calendly to cal.com` (cluster) | 140 | 0.25 | Buyer-intent migration — CSV mapping + redirect strategy |
| 18 | **EspoCRM** | `espocrm sales pipelines` | 110 | — | Multi-pipeline kanban; formula-field auto-stage, screenshots |
| 19 | **Open WebUI** | `open webui reset password` | 110 | 0.02 | sqlite/postgres bcrypt update — short, definitive, traffic magnet |
| 20 | **Langflow** | `langflow rag tutorial` | 90 | 0.12 | Full RAG flow with vector DB swap; concrete metrics |

**Snubbed but tempting (good signal, weaker fit):**
- `langflow vulnerability/cve-2025-3248` — 70 vol — high E-E-A-T, but security articles need a security-eng named author or you risk inaccuracy that hurts more than helps
- `redmine plugins` cluster — 510 vol — excellent volume, but list-format risks looking like scaled content unless we audit each plugin install on Redmine 5.x and 6.x and screenshot it
- `posthog reverse proxy` — 60 vol — adblock bypass, niche but high commercial intent
- `cal.com self hosted` cluster — 50 vol — solid but covered by official docs; need a reverse-proxy + email twist to differentiate

---

## Per-library breakdown

### Chat / Forum / Community

#### Rocket.Chat — 11 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `rocket chat push notifications not working` | 20 | — | Apple/Google push gateway breaks for self-hosted; needs custom build or workspace registration | Walkthrough of gateway architecture, screenshots of empty notification settings, exact `Push_enable` + `Push_gateway` config, error from `Push.serverNotifications.error`, FCM/APNS quota limits |
| `rocket chat reset admin password` | 20 | — | Admin lockout via Mongo CLI; official docs scattered | Real `mongosh` session, before/after `bcrypt.hashSync`, 2FA on admin, what changed in 6.x, why `meteor reset` is destructive |
| `rocket chat android app cannot connect` | 10 | — | Connection failure in official Android client — usually nginx/wss config or self-signed cert | Wireshark of failing handshake, exact nginx `proxy_set_header Upgrade`, `websocket_check.js` test, fingerprinting wss vs CSP vs TLS chain |
| `rocket chat websocket is disabled for this server` | 10 | — | Specific runtime error on iframe/embed setups | Reproduction in Apache/Nginx with wrong proxy headers, `Disable_Websocket` admin toggle, debug screenshot from `/api/info` |
| `rocket chat community edition limitations` | 40 | — | Real decision pain: CE quietly disables features at user-count thresholds | Concrete table from codebase: which features hit 50-seat soft cap, push quota, omnichannel agent limit, feature flags in `License.ts` |
| `rocket chat exploit` / `rce` / `vulnerability` | 60 | — | CVE/security audit pain | CVE table by version, how to check version, mitigations, when to upgrade vs patch |
| `rocket chat install ubuntu 22.04` | 30 | — | snap install broken on 22.04+; mongo 5/6 needs CPU AVX | snap failure trace, AVX check, Docker Compose alternative, benchmark snap vs Docker memory |
| `rocket chat reverse proxy` | 20 | — | nginx/Caddy/Traefik config for wss + uploads | Three working configs, upload size headers, X-Forwarded-Proto, HTTP/2 push gateway |
| `rocket chat ldap` / `active directory integration` | 30 | — | LDAP sync mismatches, search filters, group sync | Real `Group_Filter` examples, "test connection" screenshot, paged results, AD vs OpenLDAP |
| `rocket chat backup and restore` | 10 | — | Backups not transactional — file uploads, mongo, app data must coordinate | `snap restore`, GridFS vs S3 backup differences, `meteor` migration on restore |

**Top 3:** push notifications not working, reset admin password, community edition limitations.

#### Discourse — 11 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `discourse develop plugin` | 880 | 6 | Plugin starter changed three times; Ember version migration painful | Working "hello world" plugin against latest Discourse: `plugin.rb` modifiers, `api.modifyClass` Ember pattern, `discourse-doctor` debug, before/after diff for Ember 5 |
| `discourse forum software` | 590 | 38 | Self-host evaluation: hardware/RAM/runtime | Benchmark: 1k user simulation on 2GB vs 4GB VPS, sidekiq queue depth, postgres index size by topic count |
| `discourse api` / `documentation` | 220 | 6 | Auth split between User-Api-Key and Api-Key; rate limits undocumented | Python + curl examples, rate-limit env var table, common 403 traps, pagination for `/posts.json` |
| `discourse hosting` / `cheap hosting` / `free hosting` | 150 | 5 | Cost decision — $100+/mo official vs hidden self-host costs | Honest cost breakdown: VPS + mailgun/postmark + S3/CDN at three traffic tiers; monthly bill screenshots |
| `discourse install` (cluster) | 100 | 12-14 | `discourse_docker` is fork-then-rebuild, surprises people | `app.yml` hooks walkthrough, why NOT `docker run discourse/discourse`, cert auto-renew gotchas, `./launcher rebuild` failures |
| `discourse reply by email` | 20 | — | Needs MX, SPF, DKIM, polling vs IMAP, custom mailbox | Working Mailgun + DNS records, decision matrix forwarded/poll/IMAP, log lines per failure mode |
| `discourse migration` | 30 | — | phpBB/vBulletin import is script-running ordeal | Import scripts location, phpBB import in Docker exec, fixing usernames with bad chars, post-migration sidekiq backlog |
| `discourse smtp` / `gmail smtp` | 40 | — | Gmail no longer accepts password auth | OAuth2/app-password split, Postmark vs Mailgun vs SES `app.yml` examples, `./launcher mailtest` tree |
| `discourse sso` / `sso provider` | 50 | — | DiscourseConnect renamed; signing flow non-obvious | Sequence diagram, working Flask/Express provider with HMAC, signature-mismatch errors, Discourse as IdP |
| `discourse spam` | 20 | — | Akismet default but bot-spam on signup rampant | Mitigation stack: Akismet thresholds, `must_approve_users`, `discourse-akismet` log, IP rate limit env vars |
| `discourse without docker` | 10 | — | Officially unsupported but people try (Hetzner, FreeBSD, ARM) | Honest list of what breaks, source-install steps, when to give up |

**Top 3:** `discourse develop plugin` (KD 6, vol 880), `discourse api documentation`, `discourse reply by email`.

#### Flarum — 4 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `flarum the requested resource was not found` | 20 | — | Runtime error after install — `.htaccess`/nginx rewrite, base URL, missing extension | Reproduce error, `RewriteBase` block, nginx `try_files` recipe, `flarum info` diagnostic, three causes mapped to fix |
| `flarum sso` | 20 | — | SSO needs third-party extension (FoF Passport / SSO) | Working OIDC/Keycloak config, claim mapping, redirect-loop debug |
| `flarum nginx` | 20 | — | Default nginx config leaves CSS/JS broken on certain extensions | Working nginx config with `try_files`, gzip, CSP that doesn't break Mithril, `client_max_body_size` |
| `flarum wordpress integration` | 10 | — | No first-party bridge — SSO + comment sync | flarum-wordpress-bridge or custom JWT bridge; one-direction sync reality |

**Top 3:** all three nginx/SSO/error keys.

#### NodeBB — 5 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `nodebb default credentials` | 20 | — | Security — admin discovers no default; wants to verify post-install | install-time admin creation flow, half-created admin row state, `./nodebb reset -a admin` |
| `nodebb upgrade` | 20 | — | Touches redis/mongo/postgres; plugins must be rebuilt | Step-by-step major-version upgrade, `./nodebb upgrade-plugins`, redis migrations, build-failure recovery |
| `nodebb sso` / `oauth` | 30 | — | OAuth requires plugin template config — JSON-in-textarea | Keycloak/Auth0/Google config JSONs, callback URL mismatch debug, email vs username on first login |
| `nodebb write api` / `rest api` | 40 | — | Two APIs (Read/Write) with different auth styles; tokens per-user | Working bearer-token examples, why uid in Write API matters, scripted topic-poster bot |
| `nodebb mysql` | 10 | — | NodeBB supports redis/mongo/postgres — people ask MySQL | Document unsupported state, postgres migration path, benchmark differences |

**Top 3:** upgrade, sso/oauth, write api.

#### Live Helper Chat — skip

CSV is dominated by SaaS support-page intent for other brands ("amazon live chat help",
"ea help live chat"). Real product keywords are navigational only. **No SEO articles
warranted from this dataset.**

---

### AI / LLM / Conversational

#### Dify — 12 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `dify internal server error` | 480 | 0 | Generic 500 — DB pool exhausted, plugin daemon crash, sandbox OOM | Reproduce 500 from each cause; docker logs lines, exact `.env` fix, healthcheck script |
| `dify how to handle request output from api` | 480 | 0 | Workflow API node returns raw JSON; users can't pipe to next node | HTTP node → Code node parsing → variable assignment; full DSL YAML + screenshots |
| `dify-sandbox` / `dify sandbox` | 480 | 1 | Sandbox container fails or blocks pip imports; minimal docs | Sandbox seccomp profile, allow-list custom python lib (pandas), troubleshoot PermissionDenied with strace |
| `dify 502 bad gateway` | 20 | 1 | nginx → api worker timeout on long LLM calls | api worker timeout + nginx `proxy_read_timeout` + gunicorn worker sizing |
| `dify ollama` | 210 | 1 | Adding Ollama — "connection refused" inside docker | `host.docker.internal` vs container network, `OLLAMA_HOST=0.0.0.0`, model context length, llama3 latency |
| `dify difference between agent and workflow` 中文 | 210 | 0 | Genuine architectural confusion | Side-by-side: same task as agent vs workflow, latency/cost numbers, when each fails |
| `dify rag workflow` | 40 | 0.64 | Building retrieval pipeline with reranker + chunking | End-to-end PDF → chunker settings → embedding → rerank → answer; retrieval@k metrics |
| `dify plugin daemon` | 40 | 0.50 | New plugin system; daemon crashes silently | Plugin daemon logs path, common crashes, build "hello world" plugin |
| `dify chat memory` | 30 | 0.14 | Memory across sessions broken | Memory window vs summary memory; config + sqlite query showing tracker contents |
| `dify 多租户` 中文 | 260 | 0 | Self-host wants per-org isolation; docs cloud-only | Workspace isolation: postgres schema per tenant, RBAC, tenant-aware API keys, full docker-compose |
| `dify 高可用部署` 中文 | 20 | 1 | Production HA — multi-replica with shared state | docker-compose with redis sentinel + postgres replica + s3 + LB api; stress test results |
| `dify 知识库优化` 中文 | 50 | 0.17 | Bad RAG quality — chunking, embeddings, rerank | Before/after retrieval scores; chunking params, embedding model swap (bge vs OpenAI), rerank impact |

**Top 3:** internal server error, dify-sandbox, rag workflow.

#### Flowise — 6 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `flowise ending nodes not found` | 20 | 1 | Specific build error — chatflow won't validate | Reproduce, node graph rules, screenshot of fixed flow |
| `flowise cannot find module turndown` | 10 | 0 | npm dep missing in custom-tool sandbox | node_modules issue in custom tool, install deps inside vm2 sandbox |
| `flowise cve` / `cve-2025-61913 flowise` | 40 | 1 | Unauthenticated RCE / SSRF in older versions | CVE chain, exploit reproducer in lab, patched version diff, hardening checklist |
| `flowise message stopped` | 10 | 1 | Streaming cut off mid-response | Inspect SSE stream, identify token-limit / proxy buffer / agent-loop break; nginx + agent fix |
| `flowise webhook` | 20 | 0.29 | Triggering chatflow from external webhook — auth/payload | n8n → Flowise webhook with HMAC, full curl + screenshot |
| `flowise web scraper` | 40 | 1 | Web scraper node fails on JS-heavy sites | Cheerio vs Playwright nodes, anti-bot blocks, scraping a real SPA |

**Top 3:** flowise cve, ending nodes not found, web scraper.

#### Langflow — 9 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `langflow setup failed` | 40 | 0 | Desktop installer hangs / errors during init | Reproduce on clean mac/win, root cause (port 7860 busy, sqlite lock, python version), diagnostic steps |
| `langflow vulnerability` / `cve-2025-3248` | 70 | 0 | Real RCE in `/api/v1/validate/code` — actively exploited | CVE-2025-3248 analysis: vulnerable endpoint, PoC, patched version, hardening |
| `langflow timeout` | 20 | 0 | Long flows die at 60s default | Timeout layers (nginx, uvicorn, langchain agent loops), config snippets to extend each |
| `langflow workers` | 30 | 0.18 | Scaling — gunicorn workers vs flow concurrency | Benchmark single vs multi-worker on same flow, GIL impact, recommended sizing |
| `langflow mcp server` / `mcp integration` | 80 | 0.27 | Model Context Protocol setup; new + sparse docs | Step-by-step: expose Langflow flow as MCP server, consume from Claude Desktop, payload examples |
| `langflow rag tutorial` | 90 | 0.12 | RAG with Langflow components | Build complete RAG flow with screenshots, swap Pinecone/Chroma/Qdrant, retrieval metrics |
| `langflow loop component` / `loop example` | 50 | 0.28 | Loop node — easy infinite loop or wrong batching | Working loop with break condition, common mistakes, example use case |
| `langflow session id` | 30 | 0.57 | Session memory across messages — confusing | Explain session_id flow, custom store backends, debug persistence |
| `langflow ollama` / `with ollama` | 50 | 0.40 | Local LLM connection issues in Docker | host.docker.internal, OLLAMA_HOST, embedding vs chat model split, perf benchmarks |

**Top 3:** langflow vulnerability/cve, setup failed, mcp server.

#### Open WebUI — 14 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `open webui 500 internal error` | 260 | — | DB lock, sqlite migration, missing OPENAI key | Diagnostic tree by log line, fixes per branch with exact command/.env |
| `open webui reset password` | 110 | 0.02 | Lost admin pw, no reset UI | sqlite/postgres update on `auth` table with bcrypt hash; full SQL snippet |
| `failed to fetch models open webui` | 60 | — | Models list empty — Ollama URL wrong, OpenAI key missing | curl test from inside container, OLLAMA_BASE_URL examples, network namespace |
| `open webui cannot connect to ollama` | 20 | 1 | Same — concrete error string | Same fix walkthrough, title-aligned |
| `open webui ollama model not found` | 20 | — | Pulled model on host not visible in webui | Containers don't share Ollama models; OLLAMA_HOST mounting, `ollama pull` from inside |
| `open webui pipelines not detected` | 20 | 1 | Pipelines server up but UI shows nothing | URL + key config, port issue, debug logs |
| `open webui permission denied microphone` | 40 | 1 | HTTPS / browser permission requirement for STT | Secure context requirement, reverse-proxy + Let's Encrypt, mkcert for localhost |
| `open webui system prompt not working` | 20 | 1 | Per-model / per-chat system prompt ignored | Show precedence (model > chat > default), modelfile vs UI, real test |
| `open webui web search not working` | 40 | — | Search backend (searxng/duckduckgo) misconfigured | Each backend setup (SearXNG self-host, Tavily, Brave), API keys, logs |
| `open webui rag setup` / `tutorial` | 90 | 0.14 | RAG config — embedding model, chunking, hybrid search | Full RAG with concrete embed model swap (nomic vs bge vs openai), chunk param impact |
| `open webui pipelines` | 140 | 0.65 | Custom pipeline framework — sparse examples | Build working pipeline (logging filter, custom auth), full python file |
| `open webui slow` | 30 | 0.11 | Latency — embeddings, search, sqlite | Profile request lifecycle, identify slow stage, fix list (postgres, qdrant, model warmup) |
| `open webui pgvector` | 40 | 0.28 | Migrate from chroma to pgvector | Migration script, env vars, performance comparison |
| `open webui sso` | 20 | 0.66 | OAuth/OIDC integration | Working Authentik / Keycloak config, env vars, group mapping |

**Top 3:** 500 internal error, reset password, rag setup.

#### Typebot — 5 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `typebot whatsapp` / `com whatsapp` | 50 | 0.22 | Self-host with WA needs Evolution API or Meta Cloud | Deploy Evolution API, link to Typebot WA block, message flow + media |
| `typebot self hosted` / `docker compose` / `docker` | 60 | 1 | Self-host setup non-trivial — env vars, S3, encryption secret | Production compose with postgres, S3 (MinIO), auth provider, certbot |
| `typebot s3` | 10 | 0 | File upload requires S3-compatible storage | MinIO walkthrough, env vars, CORS/signed URLs |
| `typebot evolution api` | 10 | 0 | Pairing Typebot with Evolution API for WA | Real config, webhook routing, errors with screenshots |
| `typebot webhook` | 10 | 1 | Webhook block payload + auth | Webhook block config, Bearer auth, n8n receiving end |

**Top 3:** typebot self-hosted compose, whatsapp + evolution-api, s3.

#### Rasa — 4 pain keywords (skip-tier)

CSV dominated by Celestron telescopes, "tabula rasa", restaurants, Indonesian food, Russian
band. Rasa-the-chatbot organic search has collapsed since 2023. Pickable: `rasa nlu`,
`rasa whatsapp integration`, `rasa tracker store`, `rasa custom action`. **Honest call:
if forced to skip one library, it's Rasa.**

---

### CRM / Helpdesk / ERP / Marketing

#### EspoCRM — 6 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `espocrm sales pipelines` | 110 | — | Multi-pipeline kanban not obvious | Create 2nd pipeline, stage probabilities, formula auto-stage on amount, screenshots, gotchas with cross-pipeline reports |
| `espocrm lead scoring` | 180 | — | EspoCRM has NO built-in scoring | Honest "fake lead scoring with formula fields + workflows" with copy-paste formulas, integer field, segment-by-score, demo |
| `espocrm whatsapp integration` | 30 | 0.11 | Espo doesn't ship native WhatsApp | Build Twilio/Evolution API → Espo via webhook+formula; code & flow recordings of inbound WA → lead |
| `espocrm formula` | 20 | 1 | Formula syntax is its own DSL; sparse docs | "10 EspoCRM formula recipes": entity\\_setAttribute, ifThen, datetime math, screenshots |
| `espocrm reset admin password` | 10 | 1 | Lockout panic; recovery via CLI/DB | `php reset-password.php`, MySQL UPDATE alt, 2FA reset, terminal output |
| `espocrm cron` | 10 | 1 | Cron misconfig = workflows die silently | Where cron logs, expected interval, systemd timer, `tail -f` of job pickup |

**Top 3:** lead scoring workaround, sales pipelines, formula recipes.

#### SuiteCRM — 10 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `suitecrm workflow customizations` | 40 | 1 | Workflow limitations + Process Definitions BPMN curve | Lead nurture with delay+condition+email; Logic Hook fallback when workflow can't |
| `suitecrm logic hooks` | 20 | 1 | PHP hooks confuse non-Sugar devs; afterSave/beforeSave timing bugs | Logic hooks survival guide — `logic_hooks.php` examples, infinite-loop trap, recompile, debug log |
| `suitecrm dashboard customizations` | 30 | 1 | Custom dashlets need Sugar Studio + PHP | Build custom dashlet end-to-end, SuiteCRM 8 vue3 vs SuiteCRM 7 |
| `suitecrm upgrade from 7 to 8` | 30 | 1 | Major architecture change (Symfony+Vue) | Real upgrade log: customisations that break, theme migration, CLI commands, rollback |
| `suitecrm customer portal` / `client portal` | 60 | 0.48 | Portal not free in core | Joomla portal vs SuiteCRM 8 Public area vs custom Symfony route |
| `suitecrm custom module` | 20 | 1 | Module Builder vs Studio decision | Build "Properties" module: relationships, list view, ACL roles |
| `suitecrm cron` | 20 | 1 | Scheduler stops silently | `php cron.php` execution, schedulers table, "Last successful run" debug |
| `suitecrm api v8` / `rest api` | 40 | 0.29 | OAuth2 setup quirks | OAuth2 keys generation, curl examples for create/update lead, 401 causes |
| `suitecrm permissions` | 20 | 1 | Role+Security Group matrix confusing | 3-team org with overlapping access, role/SG combo screenshots |
| `suitecrm chatwoot integration` | 30 | — | No off-the-shelf connector | Webhook from Chatwoot conversation → SuiteCRM Lead via REST v8; n8n flow |

**Top 3:** logic hooks survival, upgrade 7→8, OAuth2 API v8.

#### Chatwoot — 8 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `chatwoot api rate limit 60 requests per minute` | 40 | 0.55 | Concrete production limit causing 429s | Reproduce 429, retry-after header, bulk-message via queue, n8n loop with sleep, Cloudflare caveat |
| `chatwoot sidekiq` | 30 | 0.28 | Background workers stuck/queue grows | "Why my Chatwoot is slow" — Sidekiq dashboard, retry queue, dead jobs, restart flow |
| `chatwoot webhooks` | 20 | 1 | Payload structure undocumented for niche events | Catalog every webhook event with real JSON, signature verification |
| `chatwoot evolution api` / `whatsapp` | 40 | 1 | WhatsApp via Evolution API is de-facto self-host route | End-to-end Evolution + Chatwoot compose, QR pairing, debug "session disconnected" |
| `chatwoot custom attributes` | 20 | 1 | Define + display + filter | Custom attributes that work — define, set via API, surface in sidebar, filter inbox |
| `chatwoot dialogflow` / `chatbot` | 40 | 1 | Native bot builder limited | Wire Dialogflow ES → Chatwoot agent_bot via API, fallback to human, transcript |
| `chatwoot email configuration` | 20 | 1 | SMTP/IMAP for email channel + outgoing notifications | Inbound IMAP + Postmark for outbound, env vars, debug log |
| `chatwoot send message api` | 10 | 1 | API to inject outbound msg | Curl example, conversation_id discovery, attachment upload |

**Top 3:** rate-limit workaround, Sidekiq diagnostics, Evolution-API+WhatsApp.

#### Zammad — 10 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `zammad customer satisfaction survey feature` | 40 | 0 | Native CSAT limited; users want NPS-style | CSAT via trigger → email with rating link → webhook back creates ticket note |
| `zammad webhook` | 20 | 1 | Outbound webhook payload + signing | Trigger → webhook setup, payload anatomy, secret signing, Slack relay |
| `zammad nginx config` | 40 | 1 | Reverse proxy SSE/websocket gotchas | nginx vhost with websocket upgrade, large file upload, Let's Encrypt, `/ws` route |
| `zammad ldap` / `oauth` | 40 | 1 | Auth integrations break silently | LDAP (AD) sync filter, group→role mapping; OAuth M365 step-by-step |
| `zammad microsoft 365` / `teams integration` | 40 | 1 | M365 mail channel + Graph API auth | M365 channel with Graph (basic-auth deprecated), Azure app registration screenshots |
| `zammad time accounting` | 40 | 1 | Internal-billing reporting | Enable Time Accounting per group, CSV report, per-agent bill |
| `zammad elasticsearch` | 20 | 1 | ES rebuild after migration; OOM on small VPS | Reindex command, `searchindex.rebuild`, ES memory tuning |
| `zammad knowledge base` | 20 | 1 | Multi-locale KB published to public | Create KB, locales, public site, SEO sitemap, theming |
| `zammad custom fields` | 10 | 1 | Object attributes & migration timing | Add ticket attribute, run migration, "migration pending" banner gotcha |
| `zammad sla` | 10 | 0 | SLA setup with business hours, escalation triggers | Real SLA with 2 priorities, business calendar, escalation email, dashboard |

**Top 3:** CSAT survey workaround, nginx config, M365 Graph email channel.

#### FreeScout — 4 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `freescout chatgpt` / `ai` | 50 | 0.33 | ChatGPT module exists but practical use unclear | AI Drafts module + custom prompt; 5 prompts that produce decent first drafts |
| `freescout whatsapp` | 20 | 1 | WhatsApp module + Evolution API config | Connect via WhatsApp module + Evolution; demo inbound→ticket; vs Chatwoot |
| `freescout import` / `data transfer` | 30 | 1 | Migrating from Help Scout / Zendesk | Free Migration module + CSV; row mapping, encoding errors |
| `freescout module` | 50 | 0.52 | Confusion on which modules are free | Curated free-modules list, "minimal viable FreeScout" recipe |

**Top 3:** ChatGPT/AI drafts in practice, WhatsApp via Evolution, Help Scout migration.

#### Mautic — 11 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `mautic system requirements php version` | 140 | — | PHP 8.x compatibility shifts per Mautic 5.x | Tested matrix Mautic 5.x × PHP 8.1/8.2/8.3, missing-extension errors, opcache + memory tuning |
| `mautic not sending emails` / `campaign not sending` | 40 | 1 | Cron + spool + queue diagnosis | "Mautic emails stuck" debug — queue mode, `mautic:emails:send`, dead message log, SMTP test |
| `mautic cron jobs` | 40 | 1 | Multiple required crons; ordering matters | Authoritative cron table with frequencies + ordering + log paths; systemd timer alt |
| `mautic smtp` / `multiple smtp` | 40 | 1 | One SMTP per instance is limiting | Patch with PostMark/Mailgun routing per segment, monitor bounce |
| `mautic webhooks` | 40 | 1 | Outgoing webhook payload + auth | Webhook spec, retry behaviour, n8n endpoint validating signature |
| `mautic custom fields` | 20 | 1 | Field types + tracking pixel inheritance | Add custom field, segment filter, email merge tag, select vs lookup gotchas |
| `mautic dynamic content` | 20 | 1 | Variant logic underdocumented | "show content X if segment Y" with screenshots and HTML output |
| `mautic tracking pixel` | 40 | 1 | Cookie consent + cross-domain tracking | Tracking JS, GDPR consent gate, "contact not identified" bug fix |
| `mautic import contacts` | 20 | 1 | CSV mapping & dedupe | Real import: CSV format, do_not_contact, segment assignment, undo |
| `mautic api` / `rest api` | 60 | 1 | OAuth1/2 confusion + endpoints scattered | Working PHP+curl client, create-contact + add-to-segment recipe |
| `mautic stages` | 20 | 1 | Stages vs segments vs lifecycle | Decision matrix: stages (lifecycle) vs segments (filters), CRM funnel |

**Top 3:** "not sending emails" diagnosis, PHP requirements matrix, cron jobs canonical.

#### ERPNext — 14 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `erpnext multi-company support` | 110 | — | Inter-company setup + consolidated reports | Parent + 2 subsidiaries, COA inheritance, inter-company invoices, consolidated trial balance |
| `erpnext chart of accounts root types` / `importer` | 90 | — | COA structure mistakes break GL forever | Root types explained, Group vs Ledger, CSV importer pitfalls, fix wrong-root migration |
| `erpnext company setup fields` / `path` | 110 | — | Initial company wizard fields unclear | Walkthrough every Company doctype field with implications |
| `erpnext item tax template` | 30 | — | Tax template + item tax + COA confusion | "Wrong tax on invoice" by tracing template→item→COA mapping, IN GST + US sales examples |
| `erpnext create item programmatically frappe.get_doc` | 30 | — | Scripted creation via Server Script / API | Working `frappe.get_doc({...}).insert()` with validations, attachments, UOMs |
| `erpnext item doctype fields list` | 50 | — | Field reference for integrations | Full Item field list with type, mandatory, default, integration notes |
| `erpnext task doctype status options` | 30 | — | Custom workflow on Task | Add custom status via Workflow doctype, transitions, role-based |
| `erpnext report builder documentation` | 40 | 1 | Query-Report vs Script-Report | Build both flavors of "Sales by Customer Group" with code |
| `erpnext payment entry` | 20 | 1 | Allocation, exchange diff, mid-cycle reversal | Real reconciliation: 2 invoices + partial payment + currency diff |
| `erpnext woocommerce integration` | 40 | 1 | Connector quirks (stock sync, customer mapping) | Tested with WC 8.x: setup, sync failure, manual reconcile |
| `erpnext custom doctype` | 20 | 1 | When custom doctype vs custom field | Build "Property" doctype linking to Customer, list view, print format |
| `erpnext restore backup` | 40 | 1 | bench restore mistakes destroy data | `bench --site X restore`, files+private restore, encrypted-backup quirks |
| `erpnext payment gateway` / `stripe integration` | 40 | 1 | Stripe webhook setup + reconcile | End-to-end Stripe Payments + Webhook to Payment Entry mapping |

**Top 3:** multi-company + consolidated trial balance, COA root types, item tax template debug.

#### Frappe Framework — 7 pain keywords (drinks excluded)

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `frappe framework child table fieldname_remove event handler` | 80 | — | Specific event hook for client script | Working child-table client script with `fieldname_remove`/`_add`; full doctype.js |
| `frappe.db.get_value` / `set_value` / `bulk_insert` | 60 | — | Sparse API docs; signature variants confuse | Cheat-sheet: every signature, return values, when to use vs ORM, perf vs `get_doc` |
| `frappe whitelist` | 20 | 1 | Decorator gotchas (allow_guest, GET/POST) | "Why your method returns 403" — `@frappe.whitelist()` deep-dive, CSRF, file uploads |
| `frappe workflow` | 20 | 1 | Workflow doctype + transitions per role | Build "Leave Approval" workflow, transitions, custom states, action buttons |
| `frappe report builder` / `doctype` | 40 | 1 | Doctype design ripples everywhere | Field-types decision tree (Link vs Dynamic Link vs Table); schema example |
| `frappe background jobs` | 40 | 1 | RQ workers + queues + retries | Enqueue patterns, long jobs, RQ dashboard, recover stuck jobs |
| `frappe bench install app` / `bench commands` | 120 | — | bench CLI surface is huge | Annotated bench reference grouped by lifecycle (dev, deploy, ops) with real output |

**Top 3:** child-table fieldname_remove handler, `frappe.db.*` cheat-sheet, `frappe.whitelist()` deep-dive.

#### Snipe-IT — 10 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `snipe it intune integration` | 50 | 1 | Sync devices Intune → Snipe (no native) | PowerShell+Graph script: pulls Intune devices, creates/updates Snipe assets via API; full code |
| `snipe it azure ad sync` | 50 | 1 | User sync via SCIM / SAML JIT or scripted | Three approaches (LDAP, SAML JIT, scripted) with pros/cons + working PowerShell |
| `snipe it api` / `examples` | 210 | 0.18 | API documented but examples sparse | "10 real Snipe API recipes": bulk-checkout, custom field update, location move, license seat, audit |
| `snipe it custom fields` | 30 | 1 | Field set + encryption + format regex | Field set for laptops with encrypted serials, dropdown, conditional display |
| `snipe it saml` / `azure ad` / `sso` | 60 | 1 | SAML config errors with AAD claims | Working AAD SAML (claim mapping, signing cert renewal, 500-after-login fix) |
| `snipe it ssl setup` / `https` / `reverse proxy` | 80 | 1 | TRUSTED_PROXIES + nginx | nginx + Let's Encrypt vhost with proxy headers + .env values; debug "mixed content" |
| `snipe it smtp settings` | 20 | 1 | SMTP test fails silently; queue worker missing | Configure SMTP, queue worker via supervisor (mandatory), check logs |
| `snipe it restore backup` | 20 | 1 | tar restore + DB restore order | Backup file structure, restore order, upload-folder permission issue |
| `snipe it status labels` | 20 | 1 | Status label types cause weird filters | Decision matrix and rename procedure preserving history |

**Top 3:** Intune integration, Azure AD sync, 10-recipe API cookbook.

#### Invoice Ninja — 8 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `invoice ninja subscriptions` | 50 | 1 | Subscription product setup + recurring billing | Monthly+annual SaaS with trial via Subscriptions; webhooks for sub events |
| `invoice ninja recurring invoices` | 20 | 1 | Recurring vs subscription differ; auto-bill | Real recurring invoice with auto-bill, dunning emails, failed-card retry |
| `invoice ninja payment gateways` / `stripe` / `paypal` / `quickbooks` | 80 | 1 | Multi-gateway routing & QuickBooks 2-way sync | Stripe + PayPal config side-by-side; QB sync (one-way + caveats), error log |
| `invoice ninja docker` / `portainer` / `compose` | 110 | 0.14 | Compose vars (APP_KEY, DB) and storage volumes | docker-compose with traefik, persistent storage, upgrade `--storage:link` |
| `invoice ninja app key` | 20 | 1 | Wrong APP_KEY = invoices unreadable | Generate APP_KEY correctly, recover after rotation, encrypt/decrypt fields |
| `invoice ninja white label` / `remove logo` / `logo not showing` | 60 | 1 | License + asset paths confuse | License purchase + activate, branding settings, S3 vs local storage logo debug |
| `invoice ninja import csv` | 20 | 1 | Import field mapping & dupes | CSV columns, vendor vs client import, partial-import recovery |
| `invoice ninja email setup` | 20 | 1 | Postmark vs SMTP + bounce handling | Postmark+SES config; queue worker; "Send Test Email" failures |

**Top 3:** subscriptions + recurring billing, Docker/portainer compose with persistent storage, APP_KEY recovery.

---

### PM / Internal-tools

#### Redmine — 12 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `redmine plugins` (count/best/top cluster) | ~510 | low | Curated audited 2026 plugin shortlist needed (most lists dead/abandoned) | Crawl plugins.redmine.org, filter by last commit ≤12mo, group by feature (gantt, agile, time, SSO), screenshot install on Redmine 5.x, mark which break on Ruby 3.3 |
| `redmine gantt drag drop` | 50 | 19 | Native gantt is read-only; users want drag-drop dependencies | Compare 4 free gantt plugins (RedmineUP free, redmine_better_gantt_chart, ANKO, Easy Gantt OSS subset). Drag-drop screencap, dependency-edit limits, 5.x/6.x compat |
| `redmine resource management plugin` | 40 | 12 | Picking free vs paid resource/capacity plugin is hard | Lighten plugin vs redmine_workload vs RedmineUP Resources side-by-side, role-perm trap |
| `redmine email to ticket` / `email config` | 60 | low | IMAP polling silently breaks — users blame SMTP | Configure imap polling cron in Bitnami vs Docker Redmine, fix "encoding=utf-8" gotcha, debug Action Mailer |
| `redmine custom fields` | 20 | low | CF + permissions per role + REST API exposure undocumented | Create text/list/user-typed CFs, restrict per role/tracker, expose via REST `?include=custom_fields`, jq examples |
| `redmine workflow` | 20 | low | Status transition matrix per role/tracker is a nightmare | "Workflow → Status transitions" matrix walkthrough, real bug→fix→QA→close flow, per-tracker copy trick |
| `redmine recurring tasks` | 20 | low | No native; users hack with plugins or cron | Test 3 plugins (recurring_tasks, scheduled_issues, redmine_scheduled_tasks) on 5.1, plus plain cron+REST script |
| `redmine to jira migration` cluster | 80 | low | Real export/import pain — attachment paths, CF mapping, watcher loss | Two articles: Redmine→Jira via JCMA + CF mapping table, attachment chunking; full-server migration: pg_dump, files/, secret_token, plugin reinstall |
| `redmine database migration` / `postgresql` | 40 | low | MySQL→Postgres is most-asked migration | pgloader script with schema gotchas (encoding, journals.notes TEXT, attachments.disk_filename), benchmark before/after |
| `redmine nginx` / `apache` / `reverse proxy` | 60 | low | Subpath deployment + RELATIVE_URL_ROOT breaks plugins | Working nginx config for `/redmine` subpath, fix asset 404s, X-Forwarded-Proto chain for HTTPS-aware emails |
| `redmine ldap` / `sso` / `saml` / `ldap active directory` | 100 | low | LDAP "on-the-fly user creation" + group sync buggy with AD | AD bind, attribute mapping table, redmine_ldap_sync, "user invalid" error |
| `redmine view customize` / `view customize plugin` | 40 | low | view_customize plugin is the real way to add JS/HTML | 8 real snippets: hide field by role, auto-fill CF from URL, change tracker icon, inject confirm-dialog before close |
| `redmine themes` / `basecamp-persian theme` / `best theme` | 90 | low | Most themes broken on 5.x; 6.x has fewer working ones | 2026 audit: install + screenshot 8 themes on Redmine 5.1 and 6.0, list which break, fork & fix CSS for 6.x |

**Top 3:** "Every Redmine plugin actually maintained in 2026 — audited install on 5.1 + 6.0", "Drag-drop Gantt without paying Easy: 4 plugins benchmarked", "MySQL→Postgres migration with pgloader: every schema gotcha".

#### OpenProject — 11 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `openproject docker` cluster (compose / hub / install / synology / windows) | ~300 | 31 | Official compose has volume-permission and pgdata-init pitfalls | 2026 production-grade compose: separated postgres, persistent attachments volume, smtp env, `OPENPROJECT_HTTPS=true` behind reverse proxy, healthcheck, backup volume |
| `openproject backup` | 30 | low | No native automated backup; pg_dump + attachments + secret_key need coordination | Bash + cron script: `op run backup`, plus disk_directory + uploaded_files volumes, restore drill on fresh container |
| `openproject ldap` / `active directory` / `saml` / `sso` | 70 | low | LDAP filter strings + Kerberos AD + SAML omniauth poorly documented | Connect to AD with sAMAccountName, filter by group DN, test login + LDIF; SAML with Keycloak metadata |
| `openproject smtp` / `email config` | 40 | low | `smtp_address` env vs configuration.yml mismatch; STARTTLS behind proxy fails | Working env-var snippet for Gmail/SES/Mailtrap, debug `op run console` mail test, fix DKIM From-header |
| `openproject webhooks` | 30 | low | Webhook plugin payload schema undocumented; HMAC examples missing | JSON payload shape per work-package event, Node.js receiver verifying signature, posts to Slack/Discord |
| `openproject gantt` cluster (export / burndown) | 80 | low | Export to PDF/PNG looks broken; baseline locked to enterprise | Community export workflow, print-CSS hack for clean PDFs, Python ical→matplotlib for free burndown |
| `openproject community plugins` / `gitlab plugin` | 60 | low | Community plugin install is harder than Redmine — needs Dockerfile rebuild | Walkthrough: extend official Docker image with `Gemfile.plugins`, rebuild, verify; list of 2026-working plugins |
| `openproject api` / `rest api` / `key` / `examples` | 60 | low | HAL+JSON unusual; people get confused with `_links` and filter syntax | Practical recipes: list WPs with filter, create with parent, attach file, time entries — curl + Python |
| `openproject jira integration` | 80 | low | No first-party Jira connector — sync is hand-rolled | One-way Jira→OpenProject sync via REST APIs (~150 lines Python), field mapping table, idempotent issue ID |
| `openproject nginx` / `reverse proxy` | 30 | low | Behind nginx with subpath + websockets + asset_host is fiddly | Production nginx vhost: TLS, websocket upgrade for ActionCable, subpath mount, X-Forwarded-* headers |
| `openproject recurring tasks` / `relations` / `status` | 40 | low | Recurring is enterprise-only | Cron + REST script that clones template work package weekly; `_links/parent` and status-transition gotchas |

**Top 3:** "Production OpenProject Docker Compose 2026: backups, SMTP, reverse proxy in one file", "OpenProject ↔ Jira one-way sync without enterprise", "Adding community plugins to OpenProject Docker without breaking upgrades".

#### Plane — skip

CSV dominated by aviation/optics/songs/biology. Only `plane io` (590, navigational only)
points to the tool. **No qualifying pain keywords.**

#### Taiga — 2 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `taiga docker` / `docker compose` / `image` / `install` | 130 | low | Official compose has 7 services + RabbitMQ; SSL behind proxy is known stumble | 2026 minimal-but-production compose: postgres + back + front + events + async + rabbit, env reference, reverse-proxy with websocket upgrade for events, fix X-Frame-Options iframe issue |
| `taiga github integration` / `jira` / `api` | 60 | low | GitHub commit/PR linking via webhook is finicky; Jira import is community-only | GitHub webhook with secret, payload→user-story mapping, `python-taiga` script to bulk-import Jira CSV |

**Top 2:** Taiga Docker Compose with events websocket fix, Taiga ↔ GitHub webhook commit-linking.

#### Appsmith — 7 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `appsmith api params` | 590 | 10 | Param-binding with `{{Input1.text}}` quoting + URL-encoding gotchas | Every param-binding pattern: query string, body, headers, dynamic JSON, JSObject params, escape rules for SQL injection in Postgres |
| `appsmith button input` | 590 | 20 | onClick → mutate state → call query → close modal cleanly | Pattern: onClick = storeValue → run query → show alert → closeModal; covers store value, multiple actions, closemodal double issue |
| `appsmith supabase` | 50 | low | RLS conflicts with service-role key; user identity passing | Supabase as Postgres datasource, JWT pass-through for RLS, real CRUD with auth context |
| `appsmith sso` | 20 | low | OIDC config for Keycloak/Google + group→role mapping in CE | OIDC setup in self-hosted CE, IdP groups to Appsmith roles, redirect_uri reverse-proxy fix |
| `appsmith embed` / `iframe` / `public app` | 60 | low | Embedding into parent CMS while keeping auth + sizing right | Embedded dashboard: SSO token forwarding, dynamic iframe height postMessage, X-Frame-Options |
| `appsmith on page load` | 10 | low | Queries on page load fire wrong order, duplicate, before user data ready | Execution order, await chains, "Run on page load" vs JSObject pattern, duplicate-fire on widget re-render |
| `appsmith helm chart` / `deploy` | 60 | low | Self-hosted on K8s — values.yaml for SMTP/MongoDB/Redis/PVs | Production helm: external Mongo, OIDC env vars, persistence, ingress; `APPSMITH_MAIL_*` envs not in chart README |

**Top 3:** API params (590 vol, KD 10), button onClick chains (590 vol), Supabase + RLS.

#### ToolJet — 7 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `how to connect supabase to tooljet` | 170 | 23 | Supabase is most-asked datasource; auth + RLS pass-through unclear | Supabase Postgres add, `apikey` header, JWT user-id forward via custom header, RLS-aware queries |
| `tooljet supabase integration` cluster | 70 | 15 | Connector vs raw Postgres trade-offs | Native Postgres vs Supabase REST compared |
| `tooljet rest api` / `datasource docs` | 20 | low | REST datasource auth headers + dynamic params + pagination | Pagination via `currentPage`, bearer-token refresh, OpenAPI import quirks |
| `tooljet docker` / `compose` / `install` | 70 | low | Standard compose splits pg_db + tooljet_db; env collisions | Production compose: external Postgres for both DBs, env table, traefik vs nginx, `TOOLJET_HOST=` URL trap |
| `tooljet sso` cluster | 10 | low | OIDC + SAML SP setup for Keycloak/Okta | Real OIDC + SAML configs for Keycloak, group→role mapping, redirect URI behind proxy |
| `tooljet workflow` | 10 | low | New workflows engine has poor docs around triggers + variables | "Row inserted in postgres → enrich via REST → notify Slack" flow; variable scoping, error branches |
| `tooljet custom component` | 10 | low | Building JS custom component is undocumented post v3 | Scaffolding React custom component, registering, props bridge, hot-reload |

**Top 3:** Supabase + RLS, production Docker Compose, OIDC SSO with Keycloak.

#### Budibase — 6 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `how to connect supabase to budibase` | 210 | 14 | Supabase as Budibase datasource — #1 community question | Supabase Postgres, JWT pass-through, RLS-aware queries, screenshot of "data → external sources" config; schema-detection failure modes |
| `budibase api client id client secret subaccount connection` | 70 | 4 | OAuth2 datasource setup (client-credentials) poorly documented | REST datasource with OAuth2 client_credentials, refresh-token, scope/audience |
| `budibase custom components` | 30 | low | Plugin SDK build chain fragile post v3 | Scaffold via `budi plugin init`, build, upload to self-hosted, debug "schema not loading" |
| `budibase ldap` | 10 | low | LDAP config is enterprise — but env vars work in self-hosted with workaround | Actual env vars, AD bind, group→role sync via SCIM workaround |
| `budibase generate pdf` / `pdf` | 30 | low | No native PDF — users hack with print CSS or external service | "Screen → PDF" via Automation step + tiny puppeteer microservice; template approach |
| `budibase relationship` / `mysql` / `sqlite` | 50 | low | Many-to-many relationship UX in internal-DB mode is confusing | Internal-table M2M with junction table vs external Postgres FKs, query screen for both |

**Top 3:** Supabase + RLS, OAuth2 client_credentials, `budi plugin init` plugin build.

#### listmonk — 4 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `listmonk amazon ses` / `aws ses` | 30 | low | SES sending limits + IAM + SNS bounce/complaint not in docs | SES SMTP creds, SNS bounce webhook → Listmonk via 30-line proxy, IAM policy, sandbox-exit |
| `listmonk smtp` | 20 | low | "Email send failed" debugging across Sendgrid/Mailgun/Postal/relay | Real config samples per provider, TLS vs STARTTLS gotcha, "From address must be allowed sender" trap |
| `listmonk n8n` | 40 | low | No native n8n node; users want subscriber-add, campaign-trigger automations | n8n workflows hitting Listmonk REST: add subscriber on form submit, trigger transactional template; node-template JSON |
| `listmonk click tracking` | 10 | low | Click tracking + UTM + "tracking pixel disabled by Gmail" | Enable click + open tracking, inject UTM via templates, why opens unreliable in 2026 |

**Top 3:** Listmonk + SES with bounces/complaints, Listmonk + n8n playbook, "why your Listmonk opens look fake in 2026".

---

### Analytics / Ecommerce / Scheduling

#### PostHog — 12 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `posthog nextjs` | 260 | 0.10 | App Router vs Pages Router instrumentation differs; SSR/RSC tracking breaks | `instrumentation-client.ts` vs `app/providers.tsx`, screenshot of duplicate pageviews from RSC, fix with `capture_pageview: false` + manual capture in `usePathname` effect |
| `posthog identify not working` | 20 | 1 | Anonymous → identified user merge fails, sessions split | curl repro — events table before/after, `$anon_distinct_id` mismatch, fix order: identify BEFORE next capture, never re-identify in same session |
| `posthog reverse proxy` | 20 | 1 | Adblockers nuke `/i.posthog.com`; users want self-hosted ingest | nginx + Cloudflare Worker config, `api_host` rewrite, CORS preflight trace, capture-rate before/after on same site |
| `posthog cors` | 40 | 0.14 | Cross-origin failures when proxying | Actual `Access-Control-Allow-Origin` error in DevTools, three fixes (reverse proxy header, custom domain, `cross_subdomain_cookie`) |
| `posthog feature flags nextjs` | 30 | 0.28 | Server-side flag eval mismatches client; flicker on first render | Bootstrap with `getServerSideProps`/RSC, `bootstrap` config, flicker screenshot, cold-eval latency benchmark |
| `posthog server side tracking` | 20 | 1 | Node SDK queue + flush pitfalls | `posthog-node` with `await shutdown()` in serverless, lost-event repro on Vercel, fix with `flushAt: 1` for cron |
| `posthog cloudflare worker` | 30 | 1 | Edge proxy for ingestion w/o origin | Worker script, env-var routing for `/decide` vs `/e`, latency benchmark vs direct |
| `posthog gtm` / `google tag manager posthog` | 30 | 1 | Custom GTM template misfires, autocapture conflicts | Template install, dedup events when both autocapture + GTM fire, real network log |
| `posthog stripe integration` | 20 | 1 | Revenue events from Stripe webhooks not appearing on funnels | Stripe webhook → Node SDK relay, `$set` user props with MRR, working funnel screenshot |
| `posthog data warehouse` / `to bigquery` | 60 | 0.49 | Export raw events to BQ for cohorts beyond UI limits | BigQuery batch export, partitioning gotcha, sample SQL on `events` table |
| `posthog cookieless` / `consent` | 40 | 1 | EU consent mode with no cookies | `persistence: 'memory'`, `opt_out_capturing_by_default`, cookie list before/after, GDPR DPA snippet |
| `posthog multiple environments` | 30 | 0.33 | Dev/staging/prod project separation; leaked dev events | Multi-project token routing, `disable_session_recording` in dev, polluted prod dashboard screenshot |

**Top 3:** posthog nextjs, reverse proxy + cors combined (adblock bypass), identify not working.

#### Matomo — 13 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `matomo setcustomurl trackpageview spa` | 70 | 0.05 | SPA route changes don't fire pageviews | React Router/Next.js code: `setCustomUrl` + `setReferrerUrl` + `trackPageView` in route effect, screenshot of missing routes |
| `matomo enablecrossdomainlinking setdomains setcookiedomain` | 40 | 1 | Cross-subdomain visitor stitching breaks | Exact JS init order, cookie inspector before/after, common `setCookieDomain '.example.com'` typo |
| `matomo trackecommerceorder parameters` / `addecommerceitem` | 130 | 0.20 | E-com tracking JS args mismatched; revenue not recorded | Argument-by-argument walkthrough w/ types, common error: strings where floats expected, real Goals report |
| `matomo woocommerce` | 20 | 1 | WP plugin double-counts or misses orders | Plugin config, dedup with native WC hooks, before/after revenue table |
| `matomo nginx` / `nginx config` | 40 | 1 | Bot blocks, big POST limits, `matomo.php` cached | Working `nginx.conf` snippet, `client_max_body_size`, `fastcgi_read_timeout` for archive cron |
| `matomo cron` / `archive` | 40 | 1 | Reports lag because archive crons aren't running | systemd timer vs PHP cron, `core:archive` flags, log of stuck archive |
| `matomo docker compose` | 20 | 1 | Persistence + db-link breaks on restart | Working `compose.yaml` with named volumes, MariaDB tuning, "config.ini.php missing volume" bug |
| `matomo cookie consent` / `cookieless tracking` | 40 | 1 | DSGVO mode with vs without cookies | `_paq.push(['disableCookies'])`, IP anonymization, consent banner with `requireConsent`, report differences |
| `matomo gtm` / `tag manager vs google tag manager` | 40 | 1 | MTM vs GTM tradeoffs, importing GTM containers | Build a Click trigger in MTM, exact event payload, debugger screenshot |
| `matomo import google analytics` | 20 | 1 | GA4 → Matomo migration of historical data | GA4 BigQuery export → Matomo importer plugin, volume mismatch debug |
| `matomo funnels` | 20 | 1 | Premium funnels feature setup | Goal-based funnel without paid plugin via custom dimensions, query SQL fallback |
| `matomo nextjs` | 30 | 1 | App Router pageview wiring | `usePathname` + `useSearchParams` effect, hydration-safe init, double-fire repro |
| `matomo opt out` | 20 | 1 | Embedding compliant opt-out iframe | Iframe code, styling override, cookie clear verification |

**Top 3:** SPA pageview tracking (KD 0.05), e-commerce trackEcommerceOrder family, cron + archive ops.

#### Plausible Analytics — 5 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `plausible analytics docker` | 20 | — | Self-host setup with persistence + ClickHouse | Working `compose.yaml`, ClickHouse volume gotcha, `SECRET_KEY_BASE` and `BASE_URL` mistakes |
| `plausible analytics wordpress` | 20 | — | Plugin vs script-tag tradeoffs | Both methods side-by-side, custom event setup for WooCommerce purchase |
| `plausible analytics api` | 20 | — | Stats API auth + rate limits | Auth header, breakdown query example with curl, pagination |
| `plausible import google analytics` | 10 | — | Historical GA → Plausible | Built-in GA4 import flow, what does/doesn't transfer, report-gap screenshot |
| `plausible analytics real-time dashboard update interval` | 40 | — | Users confused by perceived lag | ClickHouse aggregation cadence, browser polling vs server, network tab inspection |

**Top 3:** docker self-host, WP plugin vs script-tag, GA import. Plausible's keyword space is mostly branded/comparison — don't pad.

#### Medusa — 6 pain keywords (mythology/cartoons filtered)

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `medusa b2b starter` | 30 | 13.81 | B2B starter (companies, quote requests) on Medusa v2 | `medusa-starter-b2b` walkthrough, custom workflow for quote → order, admin B2B module screenshot |
| `medusa nextjs` | 30 | 0 | Next.js storefront wiring with publishable API key, region | Common 401 from missing `x-publishable-api-key`, region cookie persistence, network trace |
| `medusa docker compose` / `docker` | 60 | 0 | Postgres + Redis + worker container topology | Working v2 `compose.yaml`, separate `worker` mode service, healthcheck for workflows |
| `medusa stripe` / `payment stripe` | 30 | 0 | Stripe payment provider config in v2 (provider rewrite from v1) | Provider config snippet, webhook secret, "no provider configured" error repro |
| `medusa multi tenant` / `marketplace` / `multi vendor` | 60 | 0 | No native multi-vendor — community hacks | Architecture options: sales channels per vendor vs separate stack, working Sales Channels split, payouts model |
| `medusa js product csv import format columns` | 10 | 0 | CSV column spec for product import — undocumented edge cases | Full column reference w/ examples, `variant_option_1_value` gotcha, import error log |

**Top 3:** Next.js storefront (publishable key), Stripe v2 provider, B2B starter.

#### Saleor — 7 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `saleor webhooks` | 20 | 1 | Async vs sync webhooks, signature verification | Sync webhook for tax + shipping calc working code, signature verify with public key, dropped-webhook repro |
| `saleor stripe` | 20 | 1 | Stripe payment app config | Saleor App pattern w/ Stripe, PaymentIntent → transaction event mapping, succeeded transaction screenshot |
| `saleor nextjs` / `storefront` | 40 | 1 | React Storefront wiring with GraphQL codegen | Codegen config, channel/locale cookie, common `channel` arg missing GraphQL error |
| `saleor checkout` | 20 | 1 | Migrating from old checkout to new SDK | Storefront SDK checkout flow, `checkoutCreate` → `checkoutComplete`, `INSUFFICIENT_STOCK` handling |
| `saleor multi vendor` / `marketplace` | 40 | 1 | Saleor lacks native marketplace | Channels-per-vendor vs Apps-per-vendor architecture compared, payout model |
| `saleor plugins` / `apps` | 40 | 1 | Plugin (legacy) vs Apps (current) migration | Migration map, manifest example, dashboard install screenshot |
| `saleor graphql` / `graphql api` | 30 | 1 | Pagination + filtering quirks (Relay cursor) | Relay pagination pattern, `filter`/`where` mismatch, `__type` introspection debug |

**Top 3:** sync webhooks for tax/shipping, Stripe payment app, Next.js storefront.

#### Sylius — 5 pain keywords

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `sylius elasticsearch` | 10 | 1 | Search bundle setup + reindex | `sylius/search-plugin` config, mapping override for product attributes, reindex cron |
| `sylius docker` / `docker-compose` | 20 | 1 | Working dev stack PHP-FPM + MySQL + Node | Compose file, asset compilation issue, healthcheck |
| `sylius plugin` / `cms plugin` / `refund plugin` | 40 | 1 | Plugin scaffolding + DI extension on Symfony 6/7 | Plugin skeleton, service decoration to override `OrderProcessor`, common compiler-pass error |
| `sylius b2b` | 10 | 1 | Customer groups + price lists for B2B | Channels + customer-tier pricing, custom shipping rule per group |
| `sylius headless` | 10 | 1 | Using Sylius API Platform endpoints headlessly | API Platform routes inventory, JWT auth, Next.js storefront stub w/ real GraphQL/REST trace |

**Top 3:** sylius plugin DX (~40 combined), headless with API Platform, elasticsearch.

#### Vendure — 3 pain keywords (restaurants/industries filtered)

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `vendure storefront` | 20 | 1 | Wiring Angular/Remix/Next storefront with Shop API | GraphQL codegen for Shop API, channel + auth token cookie, `activeOrder` query trace |
| `vendure plugins` | 20 | 1 | Writing custom plugin (entity, service, GraphQL ext) | Plugin skeleton, `@VendurePlugin` decorator, custom field migration, missing `compatibility` error |
| `vendure marketplace` / `multi vendor` | 40 | 1 | Multi-vendor patterns (Channels but not full marketplace) | Channels-per-seller, payout split via custom plugin, comparison with off-the-shelf marketplace plugin |

**Top 3:** vendure plugins (DX core), marketplace patterns, storefront onboarding. Vendure's keyword space is small — invest proportionally.

#### Cal.com — 9 pain keywords (state benefits/credit-union filtered)

| Keyword | Vol | KD | Pain | Article angle |
|---------|----:|---:|------|---------------|
| `cal.com embed` / `embed cal com` | 220 | 0 | Embedding the booker on a marketing site, layout/CSS conflicts | Inline vs popup vs floating-button, CSS variable theming, broken iframe height + fix with `auto-resize` listener |
| `migrate from calendly to cal.com` (cluster) | 140 | 0.25 | Real migration: event types, redirects, integrations | Calendly CSV mapped to Cal.com event types, `/calendly/foo` → `/cal/foo` redirect strategy, integration carry-over |
| `cal.com webhooks` | 30 | 1 | Booking webhook payload + signature, retry semantics | Payload examples for `BOOKING_CREATED/CANCELLED/RESCHEDULED`, signature verify in Node, idempotency |
| `cal.com api` (cluster) | 160 | 0–0.42 | v2 REST API auth + booking creation | API key vs OAuth, create booking with availability check, common 422 from missing timezone |
| `n8n cal.com` / `integration` | 40 | 0 | Wiring Cal bookings into n8n automations | n8n workflow JSON: webhook → Slack → CRM, execution log screenshot |
| `cal.com stripe` | 20 | 1 | Paid bookings via Stripe app | App install, price config per event-type, refund flow on cancellation |
| `cal com self hosted` / `cal.com self hosted` | 40 | 1 | Self-host with calendar sync + email | Docker compose, `CALENDSO_ENCRYPTION_KEY`, Google calendar OAuth, SMTP, "no slots" bug from missing OAuth scopes |
| `cal.com docker compose` / `cal com docker` | 40 | 1 | Persistent compose file | Working compose with Postgres + email, healthcheck, schema migration on startup |
| `cal.com google calendar` (sync) | 40 | 1 | Google Calendar two-way sync, double-bookings | OAuth scope checklist, double-booking repro on token expiry, fix with refresh token storage |

**Top 3:** cal.com embed (220 vol KD 0), migrate from Calendly cluster, self-hosted + docker compose.

#### Cal.diy — skip

All keywords are about cal-king bed frames, calcium-magnesium, Cal Kestis cosplay, .50 cal
items. **No software intent. Don't write articles.**

---

## Notes for writers

1. **Write fewer, deeper articles.** Pick from cross-lib top 20 first. One article that
   ranks beats five that get manual-actioned.

2. **First-hand artifacts mandatory.** Every article needs at least one of: screenshot of
   broken state, real config snippet we ran, benchmark number we measured, CVE PoC
   reproduced in our lab.

3. **Don't reuse structure.** Identical templates across libs is exactly what SpamBrain
   flags. Vary headings, code-vs-prose ratio, conclusion structure.

4. **Author bylines.** Each article needs a named human author with a bio that ties to
   actual experience. Anonymous content with no editorial chain is high-risk in 2026.

5. **Skip these libs entirely:** Live Helper Chat, Plane, Cal.diy, Rasa (all collapsed
   organic search or noise-dominated CSVs).

6. **Skip-tier candidates if scope is tight:** Vendure, Sylius, Plausible Analytics,
   listmonk, Flarum, NodeBB — small total addressable volume, low ROI vs Tier 1 libs.
