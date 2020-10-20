from DBUtils.PooledDB import PooledDB
import MySQLdb
from MySQLdb import cursors
from common.constant import MYSQL_PASS, MYSQL_USER, MYSQL_DB, MYSQL_PORT, MYSQL_HOST, PRODUCT_INFO_TABLE


class DbManager(object):
    __pool = None

    def __init__(self, host, port, db_name, user_name, password):
        cmd = ["set names utf8mb4;"]
        conn_kwargs = {'host': host,
                       'port': port,
                       'db': db_name,
                       'user': user_name,
                       'passwd': password,
                       'charset': 'utf8mb4',
                       'cursorclass': cursors.DictCursor
                       }
        if not self.__pool:
            self.__class__.__pool = PooledDB(MySQLdb, mincached=5, maxcached=20, setsession=cmd, reset=True,
                                             **conn_kwargs)
        self._conn = None
        self._cursor = None
        self.__get_conn()

    def __get_conn(self):
        self._conn = self.__pool.connection()
        self._cursor = self._conn.cursor()

    def __execute(self, sql, param=()):
        count = self._cursor.execute(sql, param)
        return count

    def execute(self, sql, param=()):
        count = self.__execute(sql, param)
        return count

    def select_one(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._cursor.fetchone()
        # result = self.__dict_datetime_obj_to_str(result)
        return count, result

    def select_many(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._cursor.fetchall()
        """:type result:list"""
        # [self.__dict_datetime_obj_to_str(row_dict) for row_dict in result]
        return count, result

    def commit(self):
        self._conn.commit()

    def close(self):
        try:
            self._cursor.close()
            self._conn.close()
        except Exception as e:
            # logger.error(f'{e}')
            pass

    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.autocommit()
        else:
            self._conn.rollback()


if __name__ == "__main__":
    pool = DbManager(host=MYSQL_HOST, port=MYSQL_PORT, db_name=MYSQL_DB, user_name=MYSQL_USER, password=MYSQL_PASS)
    res = pool.select_many(f"select * from {PRODUCT_INFO_TABLE} where id < 3")
    # pool.commit()
    print(res)
    pool.close()
    pass
