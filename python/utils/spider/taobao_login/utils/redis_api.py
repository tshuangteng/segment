import redis

from app.constant import REDIS_HOST, REDIS_PORT, REDIS_PASS


class DbRedis:
    __pool = None

    def __init__(self, redis_host, redis_port, redis_pass, db=1):
        conn_kwargs = {
            'host': redis_host,
            'port': redis_port,
            'password': redis_pass,
            'db': db
        }
        if not self.__pool:
            self.__class__.__pool = redis.ConnectionPool(**conn_kwargs)
        self.__conn = None
        self.__get_conn()

    def __get_conn(self):
        self.__conn = redis.Redis(connection_pool=self.__pool)

    # def get_old_value(self):
    #     self.__conn.

    def close(self):
        self.__conn.close()


def get_old_value(conn, date):
    res_b = conn.get(date) or b"'token': [], 'cookie':[]"
    res_str = str(res_b, encoding='utf8')
    res_dic = eval('{' + res_str + '}')
    return res_dic


def update_value(conn, date, new_dic):
    str_res = str(new_dic).replace('{', '').replace('}', '')
    conn.set(date, str_res)


if __name__ == '__main__':
    # redis_pool = DbRedis(REDIS_HOST, REDIS_PORT, REDIS_PASS)
    # redis_pool.close()

    from datetime import datetime

    # token = 'token demo'
    # cookie = 'cookie demo'
    today_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
    # set_value = f"'token': ['{token}'], 'cookie':['{cookie}']"

    r = redis.Redis(host='localhost', port=6366, db=1, password=REDIS_PASS)
    # res = r.set(today_str, set_value)

    old_dict = get_old_value(r, '2021-03-27')
    # print(old_dict)

    # old_dict['token'].append('token3')
    # old_dict['cookie'].append('cookie3')
    # update_value(r, today_str, old_dict)
    #
    # r.close()
