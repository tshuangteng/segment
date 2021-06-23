# coding utf8

import time
import asyncio
import urllib3
import concurrent.futures
from functools import partial
from pyppeteer import launcher
from datetime import datetime, timedelta

from common.logger import logger
from common.constant import ACCOUNT
from common.api_request import get_request
from utils.chromium import generate_headers
from common.cainiao_fly_login import get_cookies_token
from express.express_utils.express_data_format import generate_express_city_url, express_data_write

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

FILE_NAME = 'express_city'
logger = logger(app_name=FILE_NAME, file_name=__name__)

launcher.AUTOMATION_ARGS.remove('--enable-automation', )

if __name__ == '__main__':
    start_time = time.time()
    stat_date = datetime.today().date() - timedelta(days=1)
    compare_date = stat_date - timedelta(days=1)

    username = ACCOUNT[0]['username']
    password = ACCOUNT[0]['password']

    user_agent, referer, token, fly_cookies = '', '', '', ''

    while not token:
        user_agent, referer, token, fly_cookies = asyncio.get_event_loop().run_until_complete(
            get_cookies_token(username, password, FILE_NAME, stat_date))

    fly_headers = generate_headers(user_agent, referer)
    all_url = generate_express_city_url(token, compare_date, stat_date)
    logger.info(f'url total number: {len(all_url)}')

    get_func = partial(get_request, headers=fly_headers, cookies=fly_cookies)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        finish = 1
        for fly_url, res_json in zip(all_url, executor.map(get_func, all_url, chunksize=100)):
            if not res_json:
                logger.info(f'failed: {fly_url}')
                finish += 1
                continue
            if '&address=&' in fly_url:
                express_data_write(res_json, fly_url, stat_date, FILE_NAME, flag=True)
            else:
                express_data_write(res_json, fly_url, stat_date, FILE_NAME)
            logger.info(f'completed: {finish}')
            finish += 1
    logger.info(f'use time: {time.time() - start_time} seconds')
