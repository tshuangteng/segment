from datetime import datetime
import time


def import_file():
    pass


def run(path, table):
    entry_date = datetime.now().date()
    imported_file_list = []

    while 1:
        today = datetime.now().date()
        day_str = str(today).replace('-', '')

        if today != entry_date:
            imported_file_list = []
            import_file(path, day_str, table, imported_file_list)
            entry_date = today

        import_file(path, day_str, table, imported_file_list)
        time.sleep(20)


if __name__ == '__main__':
    logger = mylogger('real_time_import')

    table = 'addr_real'
    path = '/addr/full/real'

    run(path, table)
