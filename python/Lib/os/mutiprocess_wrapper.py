from datetime import datetime
from multiprocessing import Pool
import time

def import_file(path, day_str, table, imported_file_list):
    pass


def run(path, table):
    entry_date = datetime.now().date()
    imported_file_list = []

    while 1:
        today = datetime.now().date()
        day_str = str(today).replace('-', '')

        if today != entry_date:
            import_file(path, day_str, table, imported_file_list)
            imported_file_list = []
            entry_date = today

        import_file(path, day_str, table, imported_file_list)
        time.sleep(20)


def multi_wrapper(args):
    return run(*args)


if __name__ == '__main__':
    logger = mylogger('real_time_import_csv')
    pool = Pool(3)

    # 需要导入的 文件地址 和 对应数据库中的表名
    path = ['/etl/dta', '/etl/dta', '/etl/dta']
    table = ['tb', 'th', 'tu']
    zip_args = list(zip(path, table))

    try:
        pool.map(multi_wrapper, zip_args)
        pool.close()
        pool.join()
    except Exception as e:
        logger.info(e)
