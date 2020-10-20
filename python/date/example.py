from datetime import datetime, timedelta

now = datetime.now().date()

# str to date format
date_str = '2020-10-19'
start_date = datetime.strptime(date_str, '%Y-%m-%d').date()

# day
stat_date = datetime.today().date() - timedelta(days=1)

# week date
last_week_start = now - timedelta(days=now.weekday() + 7)
last_week_end = now - timedelta(days=now.weekday() + 1)

last_last_week_start = now - timedelta(days=now.weekday() + 14)
last_last_week_end = now - timedelta(days=now.weekday() + 8)
week_stat_date = f'{last_week_start}_{last_week_end}'

# month date
last_month = (datetime(now.year, now.month, 1) - timedelta(days=1)).date()
last_last_month = (datetime(last_month.year, last_month.month, 1) - timedelta(days=1)).date()
month_stat_date = str(last_month)[:-3]
compare_date = str(last_last_month)[:-3]

