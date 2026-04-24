# Keyword Opportunity Finder — Methodology

Систематический поиск ключей, по которым стоит писать SEO-статьи в стиле наших WordPress how-to (как `disable-comments-wordpress`, `critical-error-on-this-website`).

## Что считается «нашим» ключом

Статья работает, если все 5 признаков совпали:

1. **Intent = Informational** — пользователь ищет решение, не сравнение/покупку.
2. **KD ≤ 25** — можем ранжироваться быстро без бэклинков.
3. **Volume ≥ 100/мес** — стоит писать (комбинация из мелких ключей в одном кластере тоже ок).
4. **Actionable phrasing** — есть глагол-действие или фраза-ошибка:
   - `how to (fix|remove|disable|change|delete|hide|stop|turn off|reset|update|migrate)`
   - `(fix|error|broken|not working|crashed|won't|can't|stuck|slow)`
   - `(remove|disable|fix) wordpress (.*)`
   - точные сообщения об ошибке (`there has been a critical error`, `error establishing database connection`)
5. **Стек совпадает** — WordPress / WooCommerce / тема / плагин (мы умеем чинить это через SimpleReview).

## Что отбрасываем

- Top-of-funnel: `wordpress tutorial`, `what is wordpress`, `wordpress for beginners`.
- Commercial: `best wordpress`, `top 10`, `X vs Y`, `wordpress hosting`, `wordpress price`.
- News/Brand: `wordpress news`, `wordpress 6.5 release`.
- Pure listings: `wordpress themes free`, `plugin directory`.
- Generic single words без действия.

## Алгоритм (3 прохода)

### Pass 1 — Жёсткий фильтр

```python
filtered = [k for k in csv if
    k.intent == "Informational"
    and 1 <= k.kd <= 25
    and k.volume >= 100
]
```

### Pass 2 — Семантическая оценка через Haiku (parallel agents)

Regex-скоринг отбрасывает релевантные ключи из-за нестандартных формулировок и не понимает интент. Вместо этого — параллельная оценка через `haiku` нейронку.

**Идея:** каждому ключу LLM-агент с описанием продукта SimpleReview ставит балл 0–3:
- **3** = SimpleReview напрямую решает в один клик (понятный элемент → PR с фиксом)
- **2** = Помогает с контекстом (debug.log, multi-file)
- **1** = Tangential — статья может упомянуть SimpleReview как опцию
- **0** = Не релевантно (туториалы, hosting, comparisons, news)

**Реализация:**
1. `extract_candidates.py` — Pass 1 фильтр (Informational, KD ≤25, vol ≥100), сортировка по volume → JSON
2. Разбиваем на 10 батчей по ~107 ключей (`/tmp/kw_batch_N.txt`, TSV)
3. Спавним 10 параллельных Agent-ов с `model: haiku`. Каждый получает self-contained prompt:
   - Описание продукта SimpleReview
   - Шкала 0–3
   - Read `/tmp/kw_batch_N.txt`, write `/tmp/kw_verdict_N.json` (массив `{kw, vol, kd, score, angle}`)
   - Angle ≤15 слов: как именно SimpleReview решит
4. `aggregate-keyword-verdicts.py` — собирает все verdicts, фильтрует score≥2, кластеризует, дедупит против `covered-keywords.txt`, ранжирует по `vol × max_score / sqrt(kd)`

**Стоимость:** 1065 ключей × Haiku ≈ $0.05–0.10, время ~1 минута (10 параллельно).

**Результат пилота (1065 ключей):** 158 кластеров со score≥2; распределение 0=598 / 1=242 / 2=158 / 3=53. Качество отбора — заметно лучше regex (ловит non-standard phrasings типа "wordpress 6.9 broke my site", "wordpress emergency help").

### Pass 3 — Кластеризация (избегаем дублей)

Группируем близкие ключи в один кластер по корневому термину:
- `disable comments wordpress`, `wordpress disable comments`, `turn off comments wordpress` → 1 кластер «disable comments»
- Берём суммарный объём кластера и пишем **одну** статью, целясь на основной кей.

### Pass 4 — Исключаем уже покрытые

Ведём список `covered.txt` с slug'ами уже написанных статей. Перед публикацией результата — фильтруем кластеры, у которых корень совпал с уже покрытым.

## Выходной формат

Топ-20 кластеров отсортированы по score, для каждого:
- Primary keyword (самый высокий объём в кластере)
- Total cluster volume
- Min KD
- Variants (3-5 топовых вариантов)
- Suggested article slug

## Скрипт

`scripts/find-keyword-opportunities.py` — реализует все 4 прохода, читает CSV из `docs/keywords/`, выводит markdown-отчёт.

## Что обновлять

- **covered.txt** — после публикации каждой статьи добавляй slug + primary keyword.
- **CSV из Semrush** — обновлять раз в квартал (объёмы меняются).
- **Action patterns** — если находишь хороший кей, который не сматчился — добавляй паттерн.
