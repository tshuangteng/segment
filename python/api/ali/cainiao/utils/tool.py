# coding utf8

import codecs
import random
import re
from pathlib import Path
from datetime import datetime
from retrying import retry
import asyncio

from common.constant import TOKEN_PATH
from common.logger import logger

logger = logger(app_name='chromium', file_name=__name__)


def set_user_agent():
    """choose one user-agent randomly for chromium"""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4092.1 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4121.0 Safari/537.36',
    ]
    user_agent = random.choice(user_agents)
    return user_agent


def generate_headers(user_agent, referer):
    """mock browser generate correct Request Headers parameters"""
    headers = {
        'Host': 'fly.cainiao.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*; q=0.0.1',
        # 'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Dest': 'empty',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': user_agent,
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': referer,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    return headers


async def get_cookies(page):
    """get cookies by pyppeteer"""
    cookies_list = await page.cookies()
    cookies = {}
    for cookie in cookies_list:
        name = cookie.get('name')
        value = cookie.get('value')
        cookies[name] = value
    return cookies


async def intercept_request(req, random_index, name, stat_date):
    """use pyppeteer save token to local file"""
    # if req.resourceType in ['image', 'media', 'eventsource', 'websocket', 'stylesheet', 'font']:
    #     await req.abort()
    # else:
    file_path = Path(f'{TOKEN_PATH}/{stat_date}')
    # if not Path.exists(file_path):
    Path.mkdir(file_path, parents=True, exist_ok=True)
    token_file = Path(f'{file_path}/{name}.txt')
    req_url = req.url
    now = datetime.now().time()

    token = re.match(r'(.*tb_token_=)(\w+)(&.*)', req_url).group(2)
    with codecs.open(token_file, 'a', encoding='utf8') as wf:
        wf.write(f'{random_index} {token} {now}\n')
    logger.info(f'name: {name}, token: {token}, save succeeded.')
    await req.continue_()


def read_token(random_index, stat_date, name):
    """from local token file read corresponding token value"""
    token_file = Path(f'{TOKEN_PATH}/{stat_date}/{name}.txt')
    with codecs.open(token_file, 'r') as rf:
        data = rf.readlines()
        for token in data:
            if token.startswith(str(random_index)):
                token = token.split(' ')[1].replace('\n', '')
                return token


async def close_dialog(dialog):
    """close browser dialog windows"""
    logger(dialog.message)
    await dialog.dismiss()


async def intercept_response(res):
    resource_type = res.request.resourceType
    if resource_type in ['xhr']:
        resp = await res.json()
        logger.info(resp)


def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None


@retry(retry_on_result=retry_if_result_none, stop_max_attempt_number=3)
async def mouse_slider(page=None):
    await asyncio.sleep(1)

    try:
        stage1 = 200
        stage2 = 75
        btn_position = await page.evaluate("""
               () =>{
                return {
                 x: document.querySelector('#nc_1_n1z').getBoundingClientRect().x,
                 y: document.querySelector('#nc_1_n1z').getBoundingClientRect().y,
                 width: document.querySelector('#nc_1_n1z').getBoundingClientRect().width,
                 height: document.querySelector('#nc_1_n1z').getBoundingClientRect().height
                 }}
                """)
        x = btn_position['x'] + btn_position['width'] / 2 + 15
        y = btn_position['y'] + btn_position['height'] / 2 + 15
        await page.hover('#nc_1_n1z')
        await page.mouse.down()
        await page.mouse.move(x + stage1, y, {'steps': 30})
        await page.waitFor(150)
        await page.mouse.move(x + stage1 + stage2, y, {'steps': 4})
        await page.waitFor(1500)
        await page.mouse.up()
        await asyncio.sleep(2)

    except Exception as e:
        logger.error(f'{e}')
        pass

    try:
        fresh = await page.Jeval('.errloading', 'node => node.textContent')
        if fresh:
            logger.info(f'需要刷新后重新滑动： {fresh}')
            await page.hover('a[href="javascript:noCaptcha.reset(1)"]')
            await page.mouse.down()
            await page.mouse.up()
            await asyncio.sleep(2)
    except Exception as e:
        logger.error(f'{e}')
        pass

    finally:
        slider_info = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
        if slider_info != '验证通过':
            return None
        else:
            return page
