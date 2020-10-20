import redis
from datetime import datetime

from common.constant import REDIS_HOST, REDIS_PORT, REDIS_PASS
from common.constant import TB_GROUP, STREAM_FIELD, STREAM_KEY, ITEM_GROUP


class DbRedis:
    __pool = None

    def __init__(self, redis_host, redis_port, redis_pass, db=0):
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

    def insert_field(self, value, key=STREAM_KEY, field=STREAM_FIELD):
        self.__conn.xadd(key, {field: value})

    def single_read_value(self, key, field, ids=0, count=1, block=None):
        read_res = self.__conn.xread(streams={key: ids}, count=count, block=block)
        ack_id = read_res[0][1][0][0].decode('utf8')
        value = read_res[0][1][0][1].get(field.encode()).decode('utf8')
        return {'ack_id': ack_id, 'value': value}

    def group_read_value(self, consumer, group, key, field, count=1, block=None):
        read_res = self.__conn.xreadgroup(group, consumer, {key: '>'}, count=count, block=block)
        if read_res:
            ack_id = read_res[0][1][0][0].decode('utf8')
            value = read_res[0][1][0][1].get(field.encode()).decode('utf8')
            return {'ack_id': ack_id, 'value': value}

    def pending(self, key, min_len, max_len, group, count=1, consumer=None):
        self.__conn.xpending_range(key=key, groupname=group, min=min_len, max=max_len, count=count, consumername=consumer)

    def ack(self, key, group, ack_id=None):
        count = self.__conn.xack(key, group, ack_id)
        return count

    def create_group(self, key, group, mkstream=True):
        # mkstream: automatically create the stream
        count = self.__conn.xgroup_create(key, group, id=0, mkstream=mkstream)
        return count

    # def pending_length(self, key=STREAM_KEY, group=GROUP):
    #     pending_res = self.__conn.xpending(key, group)
    #     return pending_res['pending']
    #
    # def pending_range(self, name=STREAM_KEY, groupname=GROUP, ):
    #     res_list = self.__conn.xpending_range(name, groupname, min, max, count, consumername=consumername)
    #     all_ack_id = [ack_id['message_id'].decode('utf8') for ack_id in res_list]
    #     return all_ack_id

    def pending_id_lit(self, key, group, min='-', max='+', consumername=None):
        count = self.__conn.xpending(key, group)['pending']
        res_list = self.__conn.xpending_range(key, group, min, max, count=count, consumername=consumername)
        pending_id_list = [ack_id['message_id'].decode('utf8') for ack_id in res_list]
        return pending_id_list

    def close(self):
        self.__conn.close()


# def get_tb_pending_list(taobao_pool):
#     res = taobao_pool.pending_id_lit(key=TB_STREAM_KEY, group=TB_GROUP)
#     print(len(res))

if __name__ == '__main__':
    redis_pool = DbRedis(REDIS_HOST, REDIS_PORT, REDIS_PASS)

    # # 预备redis stream key字段名
    # value = '610858129452'
    # redis_pool.insert_field(value, key=STREAM_KEY, field=STREAM_FIELD)

    # # 创建redis stream消费组
    # import time
    # time.sleep(2)
    # redis_pool.create_group(key=STREAM_KEY, group=ITEM_GROUP)
    # redis_pool.create_group(key=STREAM_KEY, group=TB_GROUP)

    # 消费队列中pending的数据
    # taobao_res = redis_pool.pending_id_lit(key=STREAM_KEY, group=TB_GROUP)
    # print(len(taobao_res))
    #
    # items_res = redis_pool.pending_id_lit(key=STREAM_KEY, group=ITEM_GROUP)
    # print(len(items_res))

    # for ack in res:
    #     n = pool.ack(ack_id=ack)
    #     print(n)
    #     # break

    # for ack_id in res:
    #     res_dic = pool.single_read_value(ids=ack_id)
    #     print(res_dic)
    #     break
    redis_pool.close()
