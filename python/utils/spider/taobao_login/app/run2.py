import asyncio

import urllib3
from pyppeteer import launch, launcher

from utils.logger import logger
from app.constant import WIDTH, HEIGHT, HEADLESS, EXPRESS_DOMAIN_URL, POINT_DOMAIN_URL
from utils.chromium import intercept_request, get_cookies, set_user_agent

logger = logger(log_file_name='cookies_token', file_name=__name__)

# launcher.AUTOMATION_ARGS.remove('--enable-automation')
launcher.DEFAULT_ARGS.remove('--enable-automation')


async def get_cookies_token(username, password, stat_date):
    browser = await launch(headless=HEADLESS, slowMo=15, autoClose=False,
                           args=['--disable-infobars', '--disable-extensions', '--hide-scrollbars', '--mute-audio',
                                 '--no-sandbox', '--disable-gpu', '--disable-setuid-sandbox',
                                 '--disable-translate', '--safebrowsing-disable-auto-update',
                                 '--disable-bundled-ppapi-flash', '--window-size={},{}'.format(WIDTH, HEIGHT),
                                 ], dumpio=True)
    page = await browser.newPage()
    user_agent = set_user_agent()  # set chromium info
    await page.setUserAgent(user_agent)
    await page.setViewport({'width': WIDTH, 'height': HEIGHT})
    await page.goto(POINT_DOMAIN_URL)

    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

    ####
    # taobao_login fly.cainiao.com
    await asyncio.sleep(1)
    frames = page.frames
    user = await frames[2].querySelector('#fm-taobao_login-id')
    await user.type(username, {'delay': 100})
    await asyncio.sleep(2)
    passwd = await frames[2].querySelector('#fm-taobao_login-password')
    await passwd.type(password, {'delay': 100})
    await asyncio.sleep(2)
    log_in = await frames[2].querySelector('#taobao_login-form > div.fm-btn > button')
    await log_in.click({'delay': 50})
    await asyncio.sleep(3)

    # await page.reload({'delay': 50})
    # await asyncio.sleep(2)

    # page_content = await page.content()
    # with open('taobao_login.html', 'w', encoding='utf8') as wf:
    #     wf.write(page_content)

    ####
    # close web popup if exist
    mask = await page.evaluate('''document.getElementsByClassName('edpl-icon icon-edpl-close')''')
    while 1:
        try:
            await page.click(
                'body > div.edpl-wrap > div > div.edpl-mask > div > span',
                delay=200)
        except Exception as warning:
            logger.info(f'popup windows warning: {warning}')
            if warning:
                break
    await asyncio.sleep(2)
    await page.reload({'delay': 80})

    # ####
    # # move mouse cursor to left sidebar and click current select(express or point url)
    # await page.mouse.move(25, 150, steps=5)
    # try:
    #     await page.click(
    #         'body > div.edpl-wrap > div > div.edpl-nav > div:nth-child(2) > ul:nth-child(1) > ul:nth-child(3) > li > a',
    #         delay=200)
    #     await asyncio.sleep(2)
    #     await page.reload({'delay': 50})
    # except Exception as err:
    #     logger.warning(f'warning: {err}')
    #     pass

    ####
    # save cookies and token to redis
    cookies = await get_cookies(page)
    await asyncio.sleep(2)
    await page.setRequestInterception(True)
    page.on('request', lambda req: asyncio.ensure_future(
        intercept_request(req, cookies, stat_date)))

    try:
        await page.click('#J_SearchBtn', {'delay': 30})
    except Exception as e:
        logger.error(f'{e}')
        await page.close()
        await browser.close()
        return None

    await page.close()
    await browser.close()

    return True


if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    from datetime import datetime, timedelta
    from app.constant import ACCOUNT

    stat_date = str(datetime.today().date() - timedelta(days=1))
    username = ACCOUNT[5]['username']
    password = ACCOUNT[5]['password']

    login = asyncio.get_event_loop().run_until_complete(get_cookies_token(username, password, stat_date))
    if not login:
        print('failed')
    else:
        print('success')
