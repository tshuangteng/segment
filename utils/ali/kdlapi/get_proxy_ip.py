import requests
import random
from retrying import retry

from common.logger import logger

logger = logger('kdl', '__file__')


def retry_if_result_none(res):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return res is None


@retry(retry_on_result=retry_if_result_none, stop_max_attempt_number=3)
def get_request(url, headers, cookies):
    proxies = {
        'https': f'https://{k_username}:{k_password}@{random.choice(proxy_ip)}',
    }
    try:
        res = requests.get(url=url, headers=headers, proxies=proxies, cookies=cookies, verify=False)
        return res.json()
    except Exception as e:
        logger.info(f'error: {e}')
        return None


# get dps
order_id = '908684754735143'
k_username = '8825107090'
k_password = 'n789rjc3'
signature = '9jwu6csodxin3bnz6r6rlsjmk5yagcen'  # API Key
# proxy  # 113.120.61.166:22989,122.4.44.132:21808


get_dps = f'http://dps.kdlapi.com/api/getdps/?orderid={order_id}&num=1&pt=1&format=json&sep=2&f_et=1'
dps_res = requests.get(get_dps).json()
# {'msg': '', 'code': 0, 'data': {'count': 1, 'proxy_list': ['114.99.18.49:17858,173']}}

ip_info = str(dps_res['data']['proxy_list'][0]).split(',')
proxy = ip_info[0]
expire_time = ip_info[1]

logger.info(proxy)
logger.info(expire_time)
logger.info('--------------')

# check dps valid
check_dps_valid_api = f'https://dps.kdlapi.com/api/checkdpsvalid?orderid={order_id}&proxy={proxy}&signature={signature}'

# get dps valid time
get_dps_valid_time = f'https://dps.kdlapi.com/api/getdpsvalidtime?orderid={order_id}&proxy={proxy}&signature={signature}'

# get ip balance
sign_type = 'simple'
get_ip_balance = f'https://dps.kdlapi.com/api/getipbalance?orderid={order_id}&signature={signature}'

logger.info(requests.get(check_dps_valid_api).text)
logger.info(requests.get(get_dps_valid_time).text)
logger.info(requests.get(get_ip_balance).text)
