import random
import re
import asyncio
import redis

from utils.logger import logger
from utils.redis_api import get_old_value, update_value
from app.constant import REDIS_HOST, REDIS_PORT, REDIS_PASS

logger = logger(log_file_name='chromium')


def set_user_agent():
    """choose one user-agent randomly for chromium"""
    user_agents = [
        # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4323.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4392.0 Safari/537.36",
    ]
    user_agent = random.choice(user_agents)
    return user_agent


def generate_headers(user_agent, referer):
    """mock browser generate correct Request Headers parameters"""
    headers = {
        "Host": "fly.cainiao.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '''"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"''',
        "Accept": "application/json, text/plain, */*; q=0.0.1",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4323.0 Safari/537.36",
        "User-Agent": user_agent,
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": referer,
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
    }

    return headers


def generate_headers_for_chain(user_agent, referer):
    headers = {
        # "authority": "fly.cainiao.com",
        # "method": "GET",
        # "path": '',
        # "scheme": 'https',

        "Host": "fly.cainiao.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"''',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4323.0 Safari/537.36",
        "User-Agent": user_agent,
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": referer,
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
    }

    return headers


async def get_cookies(page):
    """get cookies by pyppeteer"""
    cookies_list = await page.cookies()
    # cookies = {}
    # for cookie in cookies_list:
    #     name = cookie.get('name')
    #     value = cookie.get('value')
    #     cookies[name] = value
    cookies = ''
    for cookie in cookies_list:
        name = cookie.get('name')
        value = cookie.get('value')
        cookies += f'{name}={value};'

    return cookies[:-1]


async def intercept_request(req, cookies, stat_date):
    """use pyppeteer save token to local file"""
    # if req.resourceType in ["image", "media", "eventsource", "websocket", "stylesheet", "font"]:
    #     await req.abort()
    # else:
    # file_path = Path(f'{ct_file_path}/{stat_date}')
    # Path.mkdir(file_path, parents=True, exist_ok=True)
    # cookies_file = Path(f'{cookies_file_path}/data.py')
    req_url = req.url
    token = re.match(r'(.*tb_token_=)(\w+)(&.*)', req_url).group(2)
    ###
    # save cookies and token to redis
    # redis---> key:value    {'date': {'token':[], 'cookie':[]}  }
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1, password=REDIS_PASS)
    old_dict = get_old_value(r, stat_date)
    old_dict['token'].append(token)
    old_dict['cookie'].append(cookies)
    update_value(r, stat_date, old_dict)
    r.close()
    logger.info(f'---------save token to redis ------- {token} -------------')

    await req.continue_()


async def close_dialog(dialog):
    """close browser dialog windows"""
    logger(dialog.message)
    await dialog.dismiss()


async def intercept_response(res):
    resource_type = res.request.resourceType
    if resource_type in ['xhr']:
        resp = await res.json()
        logger.info(resp)


async def mouse_slider(page=None):
    await asyncio.sleep(3)
    try:
        await page.hover('#nc_1_n1z')
        # 鼠标按下按钮
        await page.mouse.down({'delay': 50})
        # 移动鼠标
        await page.mouse.move(1000, 0, {'steps': 30})
        # 松开鼠标
        await page.mouse.up({'delay': 50})
        await asyncio.sleep(2)
    except Exception as e:
        print(e)
        return None

    # else:
    #     await asyncio.sleep(3)
    #     # 获取元素内容
    #     ua = await page.evaluate('navigator.webdriver')
    #     print(ua)
    #     # await page.screenshot({'path': './headless-slide-result.png'})
    #     slider_again = await page.querySelectorEval('#nc_1__scale_text', 'node => node.textContent')
    #     if slider_again != '验证通过':
    #         return None
    #     else:
    #         # 截图
    #         await page.screenshot({'path': './headless-slide-result.png'})
    #         print('验证通过')
    #         return True
