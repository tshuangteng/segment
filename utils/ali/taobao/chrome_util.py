import random
import asyncio
from retrying import retry

from _log.mylog import my_logger
from spider.constant import IP_ACCOUNT

logger = my_logger(__name__)


# 不加载css和img等资源
async def intercept_request(req):
    if req.resourceType in ["image", "media", "eventsource", "websocket", "stylesheet", "font"]:
        await req.abort()
    else:
        # res = {
        #     "method": req.method,
        #     "url": req.url,
        #     "data": "" if req.postData == None else req.postData,
        #     "res": "" if req.response == None else req.response
        # }
        # logger.info(f'intercept_request-->{res}')
        await req.continue_()


async def intercept_response(res):
    resource_type = res.request.resourceType
    if resource_type in ['xhr']:
        resp = await res.json()
        # logger.info(f'intercept_response-->{resp}')


# 判断函数的返回结果为None时返回True
def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None


async def page_close(browser):
    for _page in await browser.pages():
        await _page.close()
    await browser.close()


# 滑动滑块的操作
@retry(retry_on_result=retry_if_result_none, stop_max_attempt_number=8)
async def mouse_slider(page=None):
    """
    :param page:
    :return:  (flag, page)-->(成功的标志，网页)
    """
    await asyncio.sleep(1)

    # 尽量模拟人工滑动的速度
    try:
        # 淘宝滑块框300*30，滑块40*30，需要滑动的距离是260*30
        stage1 = 200
        stage2 = 75
        btn_position = await page.evaluate('''
               () =>{
                return {
                 x: document.querySelector('#nc_1_n1z').getBoundingClientRect().x,
                 y: document.querySelector('#nc_1_n1z').getBoundingClientRect().y,
                 width: document.querySelector('#nc_1_n1z').getBoundingClientRect().width,
                 height: document.querySelector('#nc_1_n1z').getBoundingClientRect().height
                 }}
                ''')
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

    except Exception:
        pass

    # 滑动之后，可能需要刷新之后重新滑动滑块
    # fresh = ''
    try:
        fresh = await page.Jeval('.errloading', 'node => node.textContent')
        if fresh:
            logger.info(f'需要刷新后重新滑动： {fresh}')
            await page.hover('a[href="javascript:noCaptcha.reset(1)"]')
            await page.mouse.down()
            await page.mouse.up()
            await asyncio.sleep(2)
    except Exception:
        pass

    # 最后返回的提示信息
    finally:
        slider_info = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
        if slider_info != '验证通过':
            return None, None
        else:
            return 1, page


# 搜索页面的滑块
async def search_page_slide(page):
    await asyncio.sleep(2)
    try:
        close_button = await page.evaluate('''document.getElementById("sufei-dialog-close").innerText''')
        logger.info(f'搜索页面的滑块是否有关闭按键：{"存在" if close_button else "不存在"}')
        # if close_button == '关闭':
        if close_button:
            await page.click('#sufei-dialog-close')
            slider = False
        else:
            slider = await page.Jeval('#nocaptcha', 'node => node.style')

        if slider:
            flag, page = await mouse_slider(page=page)
            logger.info(f'搜索页面滑动滑块之后的标志---> {flag}')
        await asyncio.sleep(1)
    except Exception:
        pass
    finally:
        await asyncio.sleep(2)
        logger.info(f'搜索页面滑动完滑块或点击关闭之后，店铺页面：{page}')
        return page


#  登录页面滑块及失败的检测
async def login_slide(browser, page):
    try:
        slider = await page.Jeval('#nocaptcha', 'node => node.style')
    except Exception:
        slider = ''
        pass

    if slider:
        flag, page = await mouse_slider(page=page)
        logger.info(f'登录页面滑动滑块之后的标志---> {flag}')

    # await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')
    # await page.evaluate('''document.getElementById("#login-form > div.fm-btn > button").click()''')
    await page.click('#login-form > div.fm-btn > button')
    await asyncio.sleep(5)
    logger.info('=================================')
    return page
    # # 账号信息出错时的判断
    # global login_error
    # try:
    #     # login_error = await page.Jeval('.error', 'node => node.textContent')
    #     login_error = await page.evaluate('''document.getElementsByClassName('error')[3].innerText''')
    #     logger.info(f'账号信息的报错是---> {login_error}')
    #     await asyncio.sleep(0.5)
    #     return None
    # except Exception:
    #     await asyncio.sleep(0.5)
    #     return page


async def get_cookie(page):
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = f"{cookie.get('name')}={cookie.get('value')}"
        cookies += str_cookie
    return cookies


def set_user_agent():
    user_agents = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    ]
    user_agent = random.choice(user_agents)
    return user_agent


def set_proxy_ip():
    ip_info = []
    for _, v in IP_ACCOUNT.items():
        ip_info.append(v)
    ip_info = random.choice(ip_info)
    return ip_info['ip'], ip_info['username'], ip_info['password']


if __name__ == '__main__':
    pass
