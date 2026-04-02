# TICK.md — vibers.onout.org

Проверить трафик и найти инсайты по источникам, поведению, аномалиям.

## 1. Nginx логи — рефереры и источники

```bash
TODAY=$(date +%d/%b/%Y)
LOG=/var/log/nginx/vibers_onout_org.access.log

echo "=== Всего запросов сегодня ==="
grep "$TODAY" $LOG | wc -l

echo ""
echo "=== UTM источники ==="
grep "$TODAY" $LOG | grep -oP 'utm_source=[^&" ]+' | sort | uniq -c | sort -rn

echo ""
echo "=== Рефереры (внешние) ==="
grep "$TODAY" $LOG | awk '{print $11}' | sed 's/"//g' | \
  grep -v '^-$' | grep -v 'vibers.onout.org' | \
  sort | uniq -c | sort -rn | head -20

echo ""
echo "=== Топ URL ==="
grep "$TODAY" $LOG | awk '{print $7}' | sed 's/?.*//' | \
  sort | uniq -c | sort -rn | head -15

echo ""
echo "=== Боты ==="
grep "$TODAY" $LOG | grep -iE 'bot|crawl|spider|awario|semrush|ahrefs|bytespider' | wc -l | xargs -I{} echo "Боты: {}"
grep "$TODAY" $LOG | grep -v -iE 'bot|crawl|spider|awario|semrush|ahrefs|bytespider' | wc -l | xargs -I{} echo "Люди: {}"

echo ""
echo "=== POST /review (кто шлёт ревью) ==="
grep "$TODAY" $LOG | grep '"POST /review' | awk '{print $1, $9, $12}' | sed 's/"//g'
```

## 2. Cloudflare Analytics — страны и браузеры

```python
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import urllib.request, json, os

# source ~/space2/.env нужен для CLOUDFLARE_API_TOKEN
TOKEN = os.popen("source ~/space2/.env && echo $CLOUDFLARE_API_TOKEN").read().strip()
ONOUT_ZONE = "684689e499faaf171a42228dacf29720"
TODAY = __import__('datetime').date.today().isoformat()

payload = json.dumps({
    "query": f'{{ viewer {{ zones(filter: {{zoneTag: "{ONOUT_ZONE}"}}) {{ httpRequestsAdaptiveGroups(filter: {{date: "{TODAY}", requestSource: "eyeball"}}, limit: 100, orderBy: [count_DESC]) {{ count dimensions {{ clientCountryName clientRequestHTTPHost userAgentBrowser }} }} }} }} }}'
}).encode()
# ... см. предыдущие запросы в истории чата
```

Или через bash:
```bash
source ~/space2/.env
ONOUT_ZONE="684689e499faaf171a42228dacf29720"
TODAY=$(date -u +%Y-%m-%d)

curl -s "https://api.cloudflare.com/client/v4/graphql" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"{ viewer { zones(filter: {zoneTag: \\\"$ONOUT_ZONE\\\"}) { httpRequestsAdaptiveGroups(filter: {date: \\\"$TODAY\\\", requestSource: \\\"eyeball\\\"}, limit: 100, orderBy: [count_DESC]) { count dimensions { clientCountryName clientRequestHTTPHost userAgentBrowser } } } } }\"}" \
  | python3 -c "
import sys,json
from collections import defaultdict
d=json.load(sys.stdin)
if d.get('errors'): print('Error:', d['errors'][0]['message']); exit()
rows = d['data']['viewer']['zones'][0].get('httpRequestsAdaptiveGroups', [])
vibers = [r for r in rows if 'vibers' in (r['dimensions'].get('clientRequestHTTPHost') or '')]
total = sum(r['count'] for r in vibers)
print(f'=== vibers.onout.org — {total} запросов ===')
by_country = defaultdict(int)
by_browser = defaultdict(int)
for r in vibers:
    by_country[r['dimensions'].get('clientCountryName','?')] += r['count']
    by_browser[r['dimensions'].get('userAgentBrowser','?')] += r['count']
print()
print('Страны:')
[print(f'  {k:30} {v}') for k,v in sorted(by_country.items(), key=lambda x:-x[1])]
print()
print('Браузеры:')
[print(f'  {k:30} {v}') for k,v in sorted(by_browser.items(), key=lambda x:-x[1])]
"
```

## 3. Google Analytics — посещаемость (накапливается с 02.04.2026)

```bash
python3 - << 'EOF'
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import urllib.request, json

creds = service_account.Credentials.from_service_account_file(
    '/root/mycity2_key.json',
    scopes=['https://www.googleapis.com/auth/analytics.readonly']
)
creds.refresh(Request())
token = creds.token

payload = json.dumps({
    "dateRanges": [{"startDate": "7daysAgo", "endDate": "today"}],
    "metrics": [
        {"name": "sessions"},
        {"name": "activeUsers"},
        {"name": "screenPageViews"},
        {"name": "bounceRate"},
        {"name": "averageSessionDuration"}
    ],
    "dimensions": [{"name": "sessionDefaultChannelGroup"}],
    "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]
}).encode()

req = urllib.request.Request(
    'https://analyticsdata.googleapis.com/v1beta/properties/531011981:runReport',
    data=payload,
    headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
)
with urllib.request.urlopen(req) as resp:
    data = json.load(resp)

print("=== GA4 — каналы за 7 дней ===")
for row in data.get('rows', []):
    ch = row['dimensionValues'][0]['value']
    v = row['metricValues']
    print(f"  {ch:30} sessions={v[0]['value']:>5}  users={v[1]['value']:>5}  bounce={float(v[3]['value'])*100:.0f}%  avg={float(v[4]['value']):.0f}s")
EOF
```

## 4. Что искать (инсайты)

- **Reddit трафик** — есть `utm_source=reddit`? Значит наш пост/комментарий работает
- **SKILL.md запросы** — сколько раз скачали `/SKILL.md`? Это потенциальные установки
- **`/review` POST** — реальные ревью-запросы или только наш GitHub Action (Cloudflare IP)?
- **Новые страны** — появились незнакомые страны? Откуда пришли?
- **Боты-кравлеры** (Semrush, Ahrefs, Awario) — если активны, значит сайт индексируется конкурентами
- **Аномалии** — резкий рост/падение трафика, 404 на странных путях (сканеры), повторные IP

## 5. Исторические логи (за прошлые дни)

```bash
# Вчерашний день
YESTERDAY=$(date -d "yesterday" +%d/%b/%Y 2>/dev/null || date -v-1d +%d/%b/%Y)
grep "$YESTERDAY" /var/log/nginx/vibers_onout_org.access.log | wc -l

# Недельная динамика
for i in 0 1 2 3 4 5 6; do
  DAY=$(date -d "$i days ago" +%d/%b/%Y 2>/dev/null || date -v-${i}d +%d/%b/%Y)
  COUNT=$(grep "$DAY" /var/log/nginx/vibers_onout_org.access.log 2>/dev/null | wc -l)
  echo "$DAY: $COUNT запросов"
done

# Архивные логи (gzip)
zgrep "utm_source=reddit" /var/log/nginx/vibers_onout_org.access.log.*.gz 2>/dev/null | wc -l | xargs -I{} echo "Reddit переходов всего (архив): {}"
```
