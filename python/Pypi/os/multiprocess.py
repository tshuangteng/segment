from multiprocessing import Pool
from datetime import datetime, timedelta


def duplicate_date(date_tuple):
    pass


if __name__ == '__main__':

    pool = Pool(3)

    init_date_str = '20200531'
    init_date = datetime.strptime(init_date_str, '%Y%m%d').date()
    date_list = []

    number = 1
    while 1:
        next_date = init_date + timedelta(days=number)
        str_next_date = str(next_date).replace('-', '')

        # 该批次 导入的时间
        if str_next_date >= '20210101':
            date_list.append((number, str_next_date))
        number += 1

        # 该批次 导入的截止时间
        if str_next_date == '20210630':
            break

    try:
        pool.map(duplicate_date, date_list)
        pool.close()
        pool.join()
    except Exception as e:
        logger.info(e)
