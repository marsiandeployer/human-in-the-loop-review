#!/usr/bin/env python3
"""Daily GA4 report for /vibers/* → Telegram."""
import os, sys, warnings
warnings.filterwarnings('ignore')

from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric,
    FilterExpression, Filter, FilterExpressionList, OrderBy,
)

SA_KEY = '/root/google_service_account.json'
PROP = 'properties/531011981'
DAYS = int(os.environ.get('GA_REPORT_DAYS', '1'))  # 1 = yesterday only

creds = service_account.Credentials.from_service_account_file(
    SA_KEY, scopes=['https://www.googleapis.com/auth/analytics.readonly'])
client = BetaAnalyticsDataClient(credentials=creds)

date_range = [DateRange(start_date=f'{DAYS}daysAgo', end_date='yesterday')]

vibers_filter = FilterExpression(filter=Filter(
    field_name='pagePath',
    string_filter=Filter.StringFilter(
        match_type=Filter.StringFilter.MatchType.BEGINS_WITH, value='/vibers')))


def query(dims, mets, dim_filter=None, order=None, limit=15):
    req = RunReportRequest(
        property=PROP, date_ranges=date_range,
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        limit=limit)
    if dim_filter: req.dimension_filter = dim_filter
    if order: req.order_bys = [OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order), desc=True)]
    return client.run_report(req)


def rows(resp):
    out = []
    for r in resp.rows:
        d = [v.value for v in r.dimension_values]
        m = [v.value for v in r.metric_values]
        out.append(d + m)
    return out


def fmt_table(header, data, widths=None):
    if not data: return '— нет данных'
    lines = []
    for row in data:
        parts = [str(v)[:w] for v, w in zip(row, widths)] if widths else [str(v) for v in row]
        lines.append(' · '.join(parts))
    return '\n'.join(lines)


# --- collect data ---
totals = rows(query(['pagePath'], ['sessions','activeUsers','screenPageViews'], vibers_filter, 'sessions', 1))
# aggregate across all /vibers pages manually
agg_req = RunReportRequest(property=PROP, date_ranges=date_range,
    dimensions=[], metrics=[Metric(name='sessions'), Metric(name='activeUsers'),
        Metric(name='screenPageViews'), Metric(name='engagedSessions')],
    dimension_filter=vibers_filter)
agg = client.run_report(agg_req)
total_sessions = total_users = total_pv = total_engaged = '0'
if agg.rows:
    total_sessions, total_users, total_pv, total_engaged = [v.value for v in agg.rows[0].metric_values]

# leads total + by label
leads_filter = FilterExpression(and_group=FilterExpressionList(expressions=[
    FilterExpression(filter=Filter(field_name='pagePath',
        string_filter=Filter.StringFilter(match_type='BEGINS_WITH', value='/vibers'))),
    FilterExpression(filter=Filter(field_name='eventName',
        string_filter=Filter.StringFilter(value='generate_lead'))),
]))

leads_agg = client.run_report(RunReportRequest(property=PROP, date_ranges=date_range,
    metrics=[Metric(name='eventCount')], dimension_filter=leads_filter))
total_leads = leads_agg.rows[0].metric_values[0].value if leads_agg.rows else '0'

# Try event_label breakdown (custom dim, may be empty first day)
try:
    labels = rows(query(['customEvent:event_label'], ['eventCount'], leads_filter, 'eventCount', 10))
except Exception:
    labels = []

# channels
channels = rows(query(['sessionDefaultChannelGroup','sessionSource'], ['sessions'],
    vibers_filter, 'sessions', 10))

# top landings
landings = rows(query(['landingPage'], ['sessions','engagedSessions'],
    vibers_filter, 'sessions', 8))

# clicks (link destinations)
click_filter = FilterExpression(and_group=FilterExpressionList(expressions=[
    FilterExpression(filter=Filter(field_name='pagePath',
        string_filter=Filter.StringFilter(match_type='BEGINS_WITH', value='/vibers'))),
    FilterExpression(filter=Filter(field_name='eventName',
        string_filter=Filter.StringFilter(value='click'))),
]))
clicks = rows(query(['linkUrl'], ['eventCount'], click_filter, 'eventCount', 8))

# --- format message (plain text) ---
period = 'за вчера' if DAYS == 1 else f'за {DAYS} дней'
lines = [f'📊 Vibers GA4 — {period}', '']
lines.append(f'👥 Users: {total_users}  |  Sessions: {total_sessions}  |  Pageviews: {total_pv}  |  Engaged: {total_engaged}')
lines.append(f'🎯 Leads: {total_leads}')
lines.append('')

if labels:
    lines.append('Leads by action:')
    for label, cnt in labels:
        name = label or '(unset)'
        lines.append(f'  · {name} — {cnt}')
    lines.append('')

if channels:
    lines.append('Каналы:')
    for ch, src, s in channels:
        lines.append(f'  · {ch} / {src} — {s}')
    lines.append('')

if landings:
    lines.append('Top landings:')
    for lp, s, eng in landings:
        lp = lp[:50]
        lines.append(f'  · {lp} — {s} ({eng} engaged)')
    lines.append('')

if clicks:
    lines.append('Клики на внешние ссылки:')
    for url, cnt in clicks:
        short = url.replace('https://','').replace('http://','')[:55]
        lines.append(f'  · {short} — {cnt}')

text = '\n'.join(lines)

# --- send ---
TELEGRAM_API_ID = int(os.environ.get('TELEGRAM_API_ID', '0'))
TELEGRAM_API_HASH = os.environ.get('TELEGRAM_API_HASH', '')
TELEGRAM_SESSION = os.environ.get('TELEGRAM_SESSION_STRING', '')
TELEGRAM_CHAT_ID = int(os.environ.get('VIBERS_REPORT_CHAT_ID', '-5100588378'))

if not (TELEGRAM_API_HASH and TELEGRAM_SESSION):
    print(text)
    print('\n[TELEGRAM credentials missing — printed only]', file=sys.stderr)
    sys.exit(0)

import asyncio
from hydrogram import Client

async def send():
    app = Client('vibers_ga_report', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH,
                 session_string=TELEGRAM_SESSION, in_memory=True)
    async with app:
        # Populate peer cache — needed for channel IDs not yet seen
        try:
            async for _ in app.get_dialogs(): break
        except Exception:
            pass
        await app.send_message(TELEGRAM_CHAT_ID, text)

asyncio.run(send())
print(f'Sent to {TELEGRAM_CHAT_ID}')
