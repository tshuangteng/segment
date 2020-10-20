import asyncio
from celery import Celery, platforms
# from pyapollos import ApolloClient

from api.parse_address import standard4classaddress, get_category

##
# apollo dev
# apollo_client = ApolloClient(app_id="b05-addr-api-redis", cluster='default', config_server_url="http://10.19.18.201:30225")

##
# apollo prd
# apollo_client = ApolloClient(app_id="pro-b05-addr-api", cluster='default', config_server_url="http://apollometa.com:30225")
# redis_url = apollo_client.get_value('redis_url', namespace='application')
# redis_pass = apollo_client.get_value('redis_pass', namespace='application')
# redis_port = apollo_client.get_value('redis_port', namespace='application')

##
# local VM prd
redis_pass = 'huangteng123'
redis_url = 'addr_redis'
redis_port = 6379

# redis_pass = 'MjExMGNh'
# redis_url = 'prod.rediscloud-slb-1.yundasys.com'
# redis_port = 30074

celery = Celery()
celery.conf.update(
    broker_url=f'redis://:{redis_pass}@{redis_url}:{redis_port}/0',
    result_backend=f'redis://:{redis_pass}@{redis_url}:{redis_port}/1',
    max_connections=98,
    timezone='Asia/Shanghai',
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',

)

platforms.C_FORCE_ROOT = True


async def generate_addr(data):
    input_data = data['msg']
    category = get_category(input_data)
    addr_list = standard4classaddress(input_data)

    return category, addr_list


@celery.task(name='api.tasks.parse_address')
def parse_address(data):
    res_json = {
        'errorCode': 0,
        'msg': 'success',
        'datas':
            {
                'province': '',
                'city': '',
                'county': '',
                'dtl_address': '',
                'category': ''
            }
    }
    res_list = asyncio.run(generate_addr(data))

    if res_list:
        res_json['datas']['province'] = res_list[1][0]
        res_json['datas']['city'] = res_list[1][1]
        res_json['datas']['county'] = res_list[1][2]
        res_json['datas']['dtl_address'] = ''.join(res_list[1][3:])
        res_json['datas']['category'] = res_list[0]

    return res_json
