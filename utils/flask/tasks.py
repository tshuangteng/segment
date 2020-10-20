from celery import Celery, platforms
from api.parse_address import standard4classaddress
from pyapollos import ApolloClient

##
# apollo dev/uat
# apollo_client = ApolloClient(app_id="b05-addr-api-redis", cluster='default', config_server_url="http://10.19.18.201:30225")

##
# apollo prd
# apollo_client = ApolloClient(app_id="pro-b05-addr-api", cluster='default', config_server_url=" http://apollometa.com:30225")
# redis_url = apollo_client.get_value('redis_url', namespace='application')
# redis_pass = apollo_client.get_value('redis_pass', namespace='application')
# redis_port = apollo_client.get_value('redis_port', namespace='application')

##
# VM prd
redis_pass = 'huangteng123'
redis_url = 'addr_redis'
redis_port = 6379

celery = Celery()
celery.conf.update(
    broker_url=f'redis://:{redis_pass}@{redis_url}:{redis_port}/0',
    result_backend=f'redis://:{redis_pass}@{redis_url}:{redis_port}/1',
    timezone='Asia/Shanghai',
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)

platforms.C_FORCE_ROOT = True


@celery.task(name='api.tasks.parse_address')
def parse_address(data):
    input_data = data['msg']
    res_list = standard4classaddress(input_data)

    res_json = {
        'errorCode': 0,
        'msg': 'success',
        'datas':
            {
                'province': '',
                'city': '',
                'county': '',
                'dtl_address': ''
            }
    }

    if res_list:
        res_json['datas']['province'] = res_list[0]
        res_json['datas']['city'] = res_list[1]
        res_json['datas']['county'] = res_list[2]
        res_json['datas']['dtl_address'] = ''.join(res_list[3:])

    return res_json
