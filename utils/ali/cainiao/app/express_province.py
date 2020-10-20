# coding utf8

import asyncio
import time
import concurrent.futures
import requests
import urllib3
from pyppeteer import launcher
from datetime import datetime, timedelta

from common.logger import logger
from common.constant import ACCOUNT
from common.cainiao_fly_login import get_cookies_token
from utils.chromium import generate_headers
from express.express_utils.express_data_format import express_data_write, generate_express_province_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

FILE_NAME = 'express_province'
logger = logger(app_name=FILE_NAME, file_name=__name__)

launcher.AUTOMATION_ARGS.remove('--enable-automation', )

if __name__ == '__main__':
    start_time = time.time()
    stat_date = datetime.today().date() - timedelta(days=1)
    compare_date = stat_date - timedelta(days=1)

    username = ACCOUNT[1]['username']
    password = ACCOUNT[1]['password']

    user_agent, referer, token, cookies = '', '', '', ''

    while not token:
        user_agent, referer, token, cookies = asyncio.get_event_loop().run_until_complete(
            get_cookies_token(username, password, FILE_NAME, stat_date))

    headers = generate_headers(user_agent, referer)
    all_url = generate_express_province_url(token, compare_date, stat_date)
    logger.info(f'url total number: {len(all_url)}')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(requests.get, url, headers=headers, cookies=cookies, verify=False): url for
                         url in all_url}
        finish = 1
        for future in concurrent.futures.as_completed(future_to_url):
            api_url = future_to_url[future]
            try:
                response_content = future.result().json()
            except Exception as error:
                logger.error(f'{error}')
                logger.info(f'get {api_url} no data!')
                break
            express_data_write(response_content, api_url, stat_date, FILE_NAME)
            logger.info(f'complete: {finish}')
            finish += 1

    logger.info(f'use time: {time.time() - start_time} seconds')
