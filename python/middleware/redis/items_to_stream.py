import os

from db.mysql_manager import DbManager
from db.redis_manager import DbRedis
from common.constant import MYSQL_PASS, MYSQL_USER, MYSQL_DB, MYSQL_PORT, MYSQL_HOST
from common.constant import REDIS_HOST, REDIS_PORT, REDIS_PASS, STREAM_KEY, TB_GROUP, ITEM_GROUP
from common.constant import PRODUCT_ITEM_TABLE
from common.logger import my_logger

file_name = os.path.basename(__file__).split('.')[0]
logger = my_logger(file_name)


def write_item_to_redis_stream(id_start, id_end, mysql_pool, redis_pool):
    select_command = f'SELECT id, item FROM `{PRODUCT_ITEM_TABLE}` WHERE id >= {id_start} and id < {id_end} ORDER BY id;'
    res_item_dict_tuple = ()
    try:
        exec_res = mysql_pool.select_many(select_command)
        res_item_dict_tuple = exec_res[1]
    except Exception as e:
        logger.warning(e)
    mysql_pool.close()

    # print(len(res_item_dict_tuple))
    if res_item_dict_tuple:
        flag = 1
        for item_dict in res_item_dict_tuple:
            try:
                redis_pool.insert_field(value=item_dict['item'])
                logger.info(f'{flag} 入队成功')
            except Exception as re:
                logger.warning(re)
            flag += 1
        logger.info('----------------------消息队列数据已生成----------------------')
        redis_pool.close()
    return True


if __name__ == '__main__':
    id_start_number = 17000000
    id_end_number = 25000000

    # insert 922828 term

    mysql_pool_conn = DbManager(host=MYSQL_HOST, port=MYSQL_PORT, db_name=MYSQL_DB, user_name=MYSQL_USER, password=MYSQL_PASS)
    redis_pool_conn = DbRedis(REDIS_HOST, REDIS_PORT, REDIS_PASS)

    ##
    # 转移item数据到消费列表
    write_item_to_redis_stream(id_start_number, id_end_number, mysql_pool_conn, redis_pool_conn)

    mysql_pool_conn.close()
    redis_pool_conn.close()
