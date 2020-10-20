import requests
import random
import time
from retrying import retry

from common.logger import logger

logger = logger('api_request', '__file__')


def retry_if_result_none(res):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return res is {}


@retry(retry_on_result=retry_if_result_none, stop_max_attempt_number=3)
def get_request(url, headers, cookies, sleep=None):
    try:
        res = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
        return res.json()
    except Exception as error:
        logger.info(f'error: {error}')
        logger.info(f'get {url} no data!')
        if sleep:
            time.sleep(random.randint(2, 3))
        return {}
