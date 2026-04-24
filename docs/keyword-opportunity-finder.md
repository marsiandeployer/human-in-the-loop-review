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

### Pass 2 — Action regex (положительный сигнал)

Каждый кей получает score = volume × intent_multiplier:

| Pattern | Multiplier | Пример |
|---------|-----------|--------|
| Точная цитата ошибки | 3.0 | `there has been a critical error...` |
| `how to (fix\|remove\|disable\|delete...) wordpress` | 2.5 | `how to remove date from wordpress url` |
| `(fix\|repair\|recover) wordpress` | 2.5 | `fix wordpress site` |
| `wordpress (X) not working\|broken\|error\|fails` | 2.5 | `wordpress images not loading` |
| `(disable\|remove\|hide\|stop) wordpress (X)` | 2.0 | `disable comments wordpress` |
| `(change\|update\|reset) wordpress (X)` | 1.5 | `change wordpress url` |
| `how to install\|setup\|configure (X) wordpress` | 1.0 | `how to install yoast` |
| Просто WP проблема без явного действия | 0.5 | `wordpress slow` |

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
