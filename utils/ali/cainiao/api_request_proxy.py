import random
import requests
from retrying import retry

from common.logger import logger

logger = logger('proxy_get', '__file__')

api_url = 'http://dps.kdlapi.com/api/getdps/?orderid=928650304233890&num=1000&pt=1&format=json&sep=1'
# proxy_ip = requests.get(api_url).json()['data']['proxy_list']
k_username = 'csh2008333'
k_password = 'elhrt79q'


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
