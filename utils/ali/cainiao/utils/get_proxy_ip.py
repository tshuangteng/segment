import requests
import random
from retrying import retry

from common.logger import logger

logger = logger('kdl', '__file__')


class KDLProxy:
    def __init__(self):
        self.order_id = order_id
        self.k_username = k_username
        self.k_password = k_password
        self.api_key = signature

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
order_id = '958701378638797'
k_username = 'pythme'
k_password = '05xa114z'
signature = 'ceow1r6y9w7fho029k8qojqdmoq67ddk'  # API Key
# proxy  # 113.120.61.166:22989,122.4.44.132:21808

# f_et include expire time of ip
# get_dps = f'http://dps.kdlapi.com/api/getdps/?orderid={order_id}&num=1&pt=1&format=json&sep=2&f_et=1'
get_dps = f'http://dps.kdlapi.com/api/getdps/?orderid={order_id}&num=1&pt=1&format=json&sep=2'

# dps_res = requests.get(get_dps).json()
# ip_info = str(dps_res['data']['proxy_list'][0])
# proxy = ip_info[0]
# expire_time = ip_info[1]
# logger.info(ip_info)
# logger.info(proxy)
# logger.info(expire_time)
logger.info('--------------')

proxy = '114.99.16.172:20888'
# check dps valid
check_dps_valid_api = f'https://dps.kdlapi.com/api/checkdpsvalid?orderid={order_id}&proxy={proxy}&signature={signature}'

# get dps valid time
get_dps_valid_time = f'https://dps.kdlapi.com/api/getdpsvalidtime?orderid={order_id}&proxy={proxy}&signature={signature}'

# get ip balance
sign_type = 'simple'
get_ip_balance = f'https://dps.kdlapi.com/api/getipbalance?orderid={order_id}&signature={signature}'
balance_res = requests.get(get_ip_balance).json()
balance_number = balance_res['data']['balance']
# logger.info(requests.get(check_dps_valid_api).text)
# logger.info(requests.get(get_dps_valid_time).text)
logger.info(balance_number)


# 2020-04-15 15:05:57,118 - get_proxy_ip - INFO -<module> - 44 - 114.99.16.172:20888
# 2020-04-15 15:05:57,118 - get_proxy_ip - INFO -<module> - 45 - 82
# 2020-04-15 15:05:57,119 - get_proxy_ip - INFO -<module> - 46 - --------------
# 2020-04-15 15:05:57,292 - get_proxy_ip - INFO -<module> - 58 - {"msg": "", "code": 0, "data": {"114.99.16.172:20888": true}}
# 2020-04-15 15:05:57,476 - get_proxy_ip - INFO -<module> - 59 - {"msg": "", "code": 0, "data": {"114.99.16.172:20888": 82}}
# 2020-04-15 15:05:57,610 - get_proxy_ip - INFO -<module> - 60 - {"msg": "", "code": 0, "data": {"balance": 2000}}


def generate_proxy_ip(oid, ino):
    get_dps = f'http://dps.kdlapi.com/api/getdps/?orderid={oid}&num={ino}&pt=1&format=json&sep=2'
    dps_res = requests.get(get_dps).json()

    pil = dps_res['data']['proxy_list']
    logger.info(f'获取{ino}个IP， IP列表：{pil}')
    return pil[0]
