# Entity Audit Report — Vibers Blog (2026-04-15)

## Methodology

For each article's target keyword, we analyzed top-10 SERP results to identify entities (brands, tools, concepts, people, studies, frameworks, benchmarks) that Google expects to see on a page ranking for that query. We then compared against what our articles currently mention. Missing entities = entity gaps that hurt topical completeness.

---

## 1. `best-ai-code-review-tools` (KW: "best ai code review tools")

**Target entities found in SERP (top-ranking pages mention these):**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| CodeRabbit | Tool | YES | - |
| Qodo / PR-Agent | Tool | YES | - |
| Greptile | Tool | YES | - |
| CodeAnt AI | Tool | YES | - |
| GitHub Copilot Code Review | Tool | YES | - |
| Graphite | Tool | YES | - |
| Entelligence | Tool | YES | - |
| **SonarQube / SonarSource** | Tool | NO | GAP |
| **Snyk / DeepCode AI** | Tool | NO | GAP |
| **Cursor BugBot / Macroscope** | Tool | NO | GAP |
| **Bito** | Tool | NO | GAP |
| **Aikido** | Tool | NO | GAP |
| **Umaku** | Tool | NO | GAP |
| **Claude Code (as review tool)** | Tool | NO | GAP |
| **Martian Code Review Bench** | Benchmark | NO | GAP |
| **DORA 2025 Report** | Study | NO | GAP |
| Augment Code benchmark | Benchmark | Mentioned in other articles | Minor gap |
| **Semgrep** | Tool | NO | GAP |
| **Codacy** | Tool | NO | GAP |

**Recommendations:**
- ADD SonarQube as a mention (most mature open-source, 10K+ stars, enterprise staple)
- ADD Snyk/DeepCode AI as security-first option
- ADD Cursor BugBot/Macroscope (precision-first, BugBot Autofix feature)
- ADD Martian Code Review Bench as the independent benchmark reference
- ADD Bito ($15/user/mo) as budget option
- ADD Claude Code review feature (announced April 2026, 84% findings on large PRs)
- MENTION DORA 2025 Report stats in the intro

**Priority: HIGH** (listicle completeness directly impacts rankings)

---

## 2. `ai-code-review-bots-miss-bugs` (KW: "ai code review bots miss bugs")

**Entities in SERP vs our article:**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| CodeRabbit (46% accuracy) | Tool+Data | YES | - |
| Qodo (60.1% F1) | Tool+Data | YES | - |
| Augment Code benchmark | Study | YES | - |
| byteiota benchmark | Study | YES | - |
| **Martian Code Review Bench** | Benchmark | NO | GAP |
| **Context window limitations** | Concept | NO | GAP |
| **Large diff problem (>1000 lines)** | Concept | NO | GAP |
| **Same-model blind spots** | Concept | NO | GAP |
| **Noise/false positive fatigue** | Concept | Partially | Minor |
| **Precision vs recall tradeoff** | Concept | NO | GAP |
| **DORA 2025 Report** | Study | NO | GAP |
| **Cursor BugBot** | Tool | NO | GAP |
| GitHub Copilot Review (25%) | Tool+Data | YES | - |
| Claude Code (31% F-score) | Tool+Data | YES | - |
| Greptile (45%) | Tool+Data | YES | - |

**Recommendations:**
- ADD Martian Code Review Bench reference as the independent standard
- ADD section on context window limitations and large diff degradation
- ADD concept of same-model blind spots (AI reviewing its own code)
- ADD precision vs recall tradeoff discussion
- MENTION DORA 2025 Report

**Priority: MEDIUM** (article is already strong, these are incremental improvements)

---

## 3. `claude-code-review` (KW: "claude code review")

**Entities in SERP vs our article:**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| Anthropic | Company | YES (implied) | - |
| Claude Code CLI | Product | YES | - |
| CORS vulnerabilities | Vuln | YES | - |
| Rate limiting | Concept | YES | - |
| CodeRabbit report (1.7x defects) | Study | YES | - |
| **CVE-2025-59536 (Claude Code vuln)** | CVE | NO | GAP |
| **CVE-2026-21852** | CVE | NO | GAP |
| **Claude Code source leak (March 2026)** | Event | NO | GAP |
| **Claude Code Security (product)** | Product | NO | GAP |
| **Anthropic claude-code-security-review Action** | Tool | NO | GAP |
| **ISACA report on Claude security** | Study | NO | GAP |
| **CSIS analysis** | Study | NO | GAP |
| **Adversa AI (permission bypass)** | Research | NO | GAP |
| **StackHawk comparison** | Article | NO | Minor |
| **Claude Code Review feature (April 2026)** | Feature | NO | GAP |
| **84% finding rate on large PRs** | Data | NO | GAP |
| **IDEsaster (30+ CVEs across AI tools)** | Research | NO | GAP |

**Recommendations:**
- ADD Claude Code's own CVEs (CVE-2025-59536, CVE-2026-21852) — shows we track actual vulnerabilities
- ADD Claude Code source leak incident as real-world example
- ADD Claude Code Review feature (April 2026) — Anthropic's own review solution
- ADD 84% finding rate stat from Anthropic's internal usage
- ADD Adversa AI's permission bypass disclosure
- MENTION IDEsaster research (24 assigned CVEs across AI coding tools)
- UPDATE dateModified when changes applied

**Priority: HIGH** (320 vol keyword, major new entities since article was published)

---

## 4. `code-review-as-a-service` (KW: "code review as a service")

**Entities in SERP vs our article:**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| CodeRabbit | Tool | YES | - |
| Qodo | Tool | YES | - |
| **Codementor** | Service | NO | GAP |
| **Redwerk** | Service | NO | GAP |
| **PullRequest.com** | Service | NO | GAP |
| **SonarQube Cloud** | Tool | NO | GAP |
| **Anthropic Code Review** | Product | NO | GAP |
| **"40% quality deficit"** | Data | NO | GAP |
| NCC Group / Trail of Bits / Bishop Fox | Companies | YES (mentioned) | - |
| **Codacy** | Tool | NO | GAP |

**Recommendations:**
- ADD Codementor as competing human review service (validates the market)
- ADD Redwerk as enterprise code audit service
- ADD PullRequest.com (most direct competitor, code review marketplace)
- MENTION the "40% quality deficit" projection for 2026
- ADD SonarQube Cloud as enterprise-grade alternative context
- ADD Anthropic's own Code Review product launch

**Priority: HIGH** (KD=1 keyword, adding competitors shows market awareness and boosts topical authority)

---

## 5. `coderabbit-alternative-human-review` (KW: "coderabbit alternative")

**Entities in SERP vs our article:**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| CodeRabbit | Tool | YES | - |
| Qodo | Tool | YES | - |
| cubic.dev | Tool | YES | - |
| Git AutoReview | Tool | YES | - |
| GitHub Copilot Review | Tool | YES | - |
| **Aikido** | Tool | NO | GAP |
| **Macroscope / Cursor BugBot** | Tool | NO | GAP |
| **Bito** ($15/user/mo) | Tool | NO | GAP |
| **SonarQube** | Tool | NO | GAP |
| **Graphite** | Tool | NO | GAP |
| **Snyk Code** | Tool | NO | GAP |
| **Claude Code** (as reviewer) | Tool | NO | GAP |
| **Martian benchmark** | Benchmark | NO | GAP |
| **CodeRabbit noise ranking** (last on precision for offline PRs) | Data | NO | GAP |
| Tembo.io | Source | YES | - |

**Recommendations:**
- ADD Aikido (top-ranking in "coderabbit alternatives" SERP)
- ADD BugBot/Macroscope (precision-first approach, BugBot Autofix)
- ADD Bito as budget alternative ($15/mo)
- ADD Graphite (stacked PRs + AI review)
- ADD Martian benchmark as independent reference
- ADD CodeRabbit's noise problem (ranked last on precision in Martian benchmark)

**Priority: HIGH** (direct competitor keyword, completeness matters for rankings)

---

## 6. `coderabbit-vs-human-review` (KW: "coderabbit vs human review")

**Entity coverage is strong.** Minor gaps:

| Entity | Gap? |
|--------|------|
| **Claude Code Review (April 2026)** | GAP |
| **Martian Code Review Bench** | Mentioned as benchmark | Minor |
| **Martin Fowler "on the loop" concept** | GAP |

**Priority: LOW** (article already well-entity-covered)

---

## 7. `ai-generated-code-security-vulnerabilities` (KW: "ai generated code security vulnerabilities")

**Entities in SERP vs our article:**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| Veracode (45% vuln rate) | Study | YES | - |
| Georgia Tech Vibe Security Radar | Research | YES | - |
| Wiz Research (2,038 vulns) | Study | YES | - |
| SusVibes benchmark | Study | YES | - |
| IDOR/SQLi/SSRF/XSS/Path Traversal | Vulns | YES | - |
| Slopsquatting | Attack | YES | - |
| **Checkmarx** | Tool | NO | GAP |
| **Moltbook breach (1.5M tokens)** | Incident | NO | GAP |
| **Escape.tech (58% critical vulns)** | Study | NO | GAP |
| **CVE-2025-53773 (Copilot RCE)** | CVE | NO | GAP |
| **CWE catalog references** | Standard | NO | GAP |
| **Cycode** | Tool | NO | Minor |
| **YC W25 cohort (25% = 95% AI code)** | Data | NO | GAP |
| **Java 72% failure rate** | Data | NO | GAP |
| **Log injection 88% failure** | Data | NO | GAP |
| **Lovable RLS disabled 70%** | Data | NO | GAP |

**Recommendations:**
- ADD Moltbook breach as real-world incident (launched Jan 28 2026, exposed 1.5M API tokens in 3 days)
- ADD CVE-2025-53773 (Copilot prompt injection RCE, CVSS 9.6)
- ADD Checkmarx as reference (major player in AI code security research)
- ADD Escape.tech stat (58% of scanned AI apps had critical vulns)
- ADD YC W25 cohort data (25% of startups = 95% AI-generated code)
- ADD Java-specific failure rate (72%) and log injection (88%)
- ADD Lovable RLS disabled stat (70% of apps)
- ADD CWE catalog references (CWE-862, CWE-798, CWE-89, CWE-79, CWE-200)

**Priority: HIGH** (security article benefits greatly from more CVEs, breach examples, and specific data points)

---

## 8. `human-in-the-loop-code-review-teams` (KW: "human in the loop code review")

**Entities in SERP vs our article:**

| Entity | Type | Our Article | Gap? |
|--------|------|-------------|------|
| DORA 2025 Report | Study | YES | - |
| Gartner (90% HITL by 2026) | Forecast | YES | - |
| EU AI Act | Regulation | YES | - |
| Parseur | Source | YES | - |
| devtoolsacademy | Source | YES | - |
| **Martin Fowler "on the loop" concept** | Concept | NO | GAP |
| **Zapier HITL patterns** | Framework | NO | GAP |
| **MindStudio** | Tool | NO | Minor |
| **Sobonix HITL for coding agents** | Article | NO | Minor |
| **AlignX AI workflow patterns** | Framework | NO | Minor |
| **"700+ AI bills in US 2024"** | Data | NO | GAP |
| **Decision fatigue / rubber-stamping risk** | Concept | NO | GAP |
| **Human "on the loop" vs "in the loop"** | Concept | NO | GAP |

**Recommendations:**
- ADD Martin Fowler's "on the loop" concept — authoritative entity, differentiates from standard HITL
- ADD decision fatigue / rubber-stamping risk as scaling challenge
- ADD "700+ AI bills" regulatory pressure data point
- ADD "on the loop" vs "in the loop" distinction

**Priority: MEDIUM** (article already strong, these add depth)

---

## Summary: Highest-Impact Entity Fixes

### Must-Fix (HIGH priority):

1. **`best-ai-code-review-tools`** — Add SonarQube, Snyk, BugBot/Macroscope, Bito, Claude Code, Martian benchmark
2. **`claude-code-review`** — Add Claude Code CVEs, source leak, April 2026 review feature, Adversa AI
3. **`code-review-as-a-service`** — Add Codementor, PullRequest.com, Redwerk, 40% quality deficit data
4. **`coderabbit-alternative-human-review`** — Add Aikido, BugBot, Bito, Graphite, Martian benchmark
5. **`ai-generated-code-security-vulnerabilities`** — Add Moltbook breach, Copilot RCE CVE, Checkmarx, Escape.tech, YC data

### Should-Fix (MEDIUM priority):

6. **`ai-code-review-bots-miss-bugs`** — Add Martian benchmark, context window limits, same-model blind spots
7. **`human-in-the-loop-code-review-teams`** — Add Martin Fowler "on the loop", decision fatigue
8. **`coderabbit-vs-human-review`** — Add Claude Code Review April 2026 feature

### Lower Priority (remaining articles not audited in depth):
- `review-cursor-generated-code`
- `how-to-test-ai-generated-code`
- `ai-writes-code-who-verifies`
- `review-vibe-coded-app-before-launch`
- `vibe-coded-app-production-ready`
- `vibe-coding-mistakes-production`
- `vibe-coding-security-risks`
- `claude-ai-performance-issues`

These can be audited in a follow-up session.

---

## Cross-Article Entity Gaps (appearing across multiple articles)

These entities should be added across the blog, not just to one article:

| Entity | Currently Missing In | Action |
|--------|---------------------|--------|
| **Martian Code Review Bench** | All articles | Add as the independent benchmark standard |
| **SonarQube** | best-tools, coderabbit-alt, code-review-service | Mention as enterprise staple |
| **Claude Code Review (April 2026)** | All articles | Add as Anthropic's own solution |
| **Snyk / DeepCode AI** | best-tools, coderabbit-alt | Add as security-first option |
| **Martin Fowler** | human-in-the-loop | Add as authoritative voice |
| **Moltbook breach** | security-vulns, vibe-coding-risks | Add as real-world incident |
| **YC W25 cohort data** | multiple vibe-coding articles | Add as market data |
