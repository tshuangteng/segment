from datetime import datetime


# 文件同步 传参数执行sh文件 入库
def duplicate_date(date_tuple):
    from_date = date_tuple[0]
    to_date = date_tuple[1]

    from_table = 'addr_real'
    to_table = 'addr_real'

    # 复制一台psql表数据到另外一台psql
    duplicate_sql = 'psql -d develop -h localhost -U gpadmin -p 5432 -c "copy {from_table}_1_prt_pn_{from_date} to STDOUT csv" | psql -d suanfa -h 10.131.51.17 -U gpadmin -p 5432 -c "TRUNCATE TABLE {to_table}_1_prt_pn_{to_date}; copy {to_table}_1_prt_pn_{to_date} from STDIN csv"'.format(
        from_date=from_date, to_date=to_date, from_table=from_table, to_table=to_table)

    logger.info('--- Start --- {date} --- {duplicate_sql}'.format(date=datetime.now(), duplicate_sql=duplicate_sql))
    res = os.system(duplicate_sql)
    if res == 0:
        logger.info('--- DUP Success --- {date} --- {duplicate_sql} ---'.format(date=datetime.now(), duplicate_sql=duplicate_sql))
    else:
        logger.info('--- DUP Error --- {date} --- {duplicate_sql} ---'.format(date=datetime.now(), duplicate_sql=duplicate_sql))
