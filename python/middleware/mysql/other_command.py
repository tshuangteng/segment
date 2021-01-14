from datetime import datetime
from constant import *
from mysql_main import DbManager

input_date = '20200601'
select_datetime = str(datetime.strptime(input_date, '%Y%m%d'))
pool = DbManager(host=MYSQL_HOST, port=MYSQL_PORT, db_name=MYSQL_DB, user_name=MYSQL_USER, password=MYSQL_PASS)

query_str = f'select id from {TEST_TABLE} where unix_timestamp(create_time) > unix_timestamp("{select_datetime}") order by id asc limit 1'
pool.execute(query_str)
pool.close()
