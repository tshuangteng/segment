# coding utf8

import asyncio
import uuid
from pyppeteer import launch

from common.logger import logger
from common.constant import WIDTH, HEIGHT, EXPRESS_DOMAIN_URL
from utils.chromium import set_user_agent, intercept_request, read_token, get_cookies

logger = logger(app_name='cookies_token', file_name=__name__)


async def get_cookies_token(username, password, name, stat_date):
    browser = await launch(headless=True, slowMo=15, autoClose=False,
                           args=['--disable-infobars', '--disable-extensions', '--hide-scrollbars', '--mute-audio',
                                 '--no-sandbox', '--disable-gpu', '--disable-setuid-sandbox',
                                 '--disable-translate', '--safebrowsing-disable-auto-update',
                                 '--disable-bundled-ppapi-flash', '--window-size={},{}'.format(WIDTH, HEIGHT)
                                 ], dumpio=True)
    page = await browser.newPage()
    user_agent = set_user_agent()
    await page.setUserAgent(user_agent)
    await page.setViewport({'width': WIDTH, 'height': HEIGHT})
    await page.goto(EXPRESS_DOMAIN_URL)
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

    # taobao_login fly.cainiao.com
    await asyncio.sleep(1)
    frames = page.frames
    user = await frames[3].querySelector('#fm-taobao_login-id')
    await user.type(username, {'delay': 80})
    passwd = await frames[3].querySelector('#fm-taobao_login-password')
    await passwd.type(password, {'delay': 80})
    log_in = await frames[3].querySelector('#taobao_login-form > div.fm-btn > button')
    await log_in.click()
    await asyncio.sleep(4)
    await page.reload()
    await asyncio.sleep(3)

    # close web popup if exist
    # mask = await page.evaluate('''document.getElementsByClassName('edpl-icon icon-edpl-close')''')

    while 1:
        try:
            await page.click(
                'body > div.edpl-wrap > div > div.edpl-mask > div > span',
                delay=1200)
            await asyncio.sleep(1)
        except Exception as warning:
            error_flg = warning
            logger.info(f'warning: {warning}')
            if error_flg:
                break

    await page.reload()
    await asyncio.sleep(3)

    # move mouse cursor to left sidebar and click current select
    await page.mouse.move(25, 150, steps=5)
    try:
        await page.click(
            'body > div.edpl-wrap > div > div.edpl-nav > div:nth-child(2) > ul:nth-child(1) > ul:nth-child(3) > li > a',
            delay=1200)
        await asyncio.sleep(5)
    except Exception as error:
        logger.error(f'warning: {error}')
        pass

    # save token
    referer = page.url
    logger.info(f'referer: {referer}')
    random_index = uuid.uuid1()
    await asyncio.sleep(1)
    await page.setRequestInterception(True)
    page.on('request', lambda req: asyncio.ensure_future(
        intercept_request(req, random_index, name, stat_date)))
    try:
        await page.click('#J_SearchBtn')
    except Exception as e:
        logger.error(f'{e}')
        await page.close()
        await browser.close()
        return '', '', '', ''

    cookies = await get_cookies(page)
    logger.info(f'cookies: {cookies}')
    await page.close()

    # read token
    token = read_token(random_index, stat_date, name)
    if not token:
        await browser.close()
        return '', '', '', ''
    logger.info(f'token: {token}')

    await browser.close()
    return user_agent, referer, token, cookies


async def get_cookies_and_referer_for_link(username, password):
    browser = await launch(headless=True, slowMo=15, autoClose=False,
                           args=['--disable-infobars', '--disable-extensions', '--hide-scrollbars', '--mute-audio',
                                 '--no-sandbox', '--disable-gpu', '--disable-setuid-sandbox',
                                 '--disable-translate', '--safebrowsing-disable-auto-update',
                                 '--disable-bundled-ppapi-flash', f'--window-size={WIDTH},{HEIGHT}',
                                 ], dumpio=True)
    page = await browser.newPage()
    user_agent = set_user_agent()
    await page.setUserAgent(user_agent)
    await page.setViewport({'width': WIDTH, 'height': HEIGHT})
    await page.goto(EXPRESS_DOMAIN_URL)
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

    await asyncio.sleep(1)
    frames = page.frames
    user = await frames[3].querySelector('#fm-taobao_login-id')
    await user.type(username, {'delay': 80})
    passwd = await frames[3].querySelector('#fm-taobao_login-password')
    await passwd.type(password, {'delay': 80})
    log_in = await frames[3].querySelector('#taobao_login-form > div.fm-btn > button')
    await log_in.click()
    await asyncio.sleep(3)
    await page.reload()
    await asyncio.sleep(3)

    while 1:
        try:
            await page.click(
                'body > div.edpl-wrap > div > div.edpl-mask > div > span',
                delay=1200)
            await asyncio.sleep(1)
        except Exception as warning:
            error_flg = warning
            logger.info(f'warning: {warning}')
            if error_flg:
                break

    await page.reload()
    await asyncio.sleep(3)

    await page.mouse.move(25, 150, steps=5)
    # click branch overall href
    try:
        await page.click('body > div.edpl-wrap > div > div.edpl-nav > div:nth-child(2) > ul:nth-child(2) > ul > li > a',
                         delay=1800)
        await asyncio.sleep(4)
    except Exception as error:
        logger.info(f'{error}')
        return '', '', ''

    referer = page.url
    cookies = await get_cookies(page)
    logger.info(f'request cookies for link: {cookies}')
    await page.close()
    await browser.close()
    return user_agent, referer, cookies
