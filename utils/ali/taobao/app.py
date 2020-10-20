# encoding: gbk

import asyncio
import datetime
import os
import time

from pyppeteer import launch, launcher
from lxml import etree

from _log.mylog import my_logger
from utils.excel.read_data import find_active_sheet, r_sheet_shop_name
from spider.chrome_util import page_close, set_user_agent
from spider.chrome_util import login_slide
from spider.constant import XLSX_FILE_PATH, WIDTH, HEIGHT, SHOP_NAME_SET_PATH, ALI_ACCOUNT, DATA_PATH

launcher.AUTOMATION_ARGS.remove('--enable-automation', )
# launcher.AUTOMATION_ARGS.remove('--password-store=basic')
os.makedirs(os.path.join(DATA_PATH, 'shop_screenshot'), exist_ok=True)
os.makedirs(os.path.join(DATA_PATH, 'generate_file'), exist_ok=True)

logger = my_logger(__name__)


def xpath_parse(html_content, shop_name):
    # type(html_content) >>> str
    tree = etree.HTML(html_content)
    number_list = tree.xpath(
        '//div[@class="items" and not (contains(@id,"J_itemlistCont" ))]/div[contains(@data-category,"auctions")]')
    # >>> [<Element div at 0x1cbb6f06908>, <Element div at 0x1cbb7b50948>,...]
    product_number = len(number_list)

    # 通过xpath方法获取所需商品详情字段
    if product_number == 0:
        return {}
    index = 0
    s_name = ''.join(tree.xpath(
        f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div/div[@class="shop"]/a/span[2]/text()'))
    date = str(datetime.datetime.now()).split(' ')[0]
    shop_id = ''.join(tree.xpath(
        f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div/div[@class="shop"]/a/@data-userid'))
    shop_url = f'https://store.taobao.com/shop/view_shop.htm?user_number_id={shop_id}'

    global dict_date
    dict_date = {shop_name: {
        'shop_id': shop_id,
        'shop_url': shop_url,
        'shop_product': [],
    }, }

    for index in range(product_number):
        if s_name != shop_name:
            continue
        product_url = 'https:' + ''.join(tree.xpath(
            f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div[2]/a/@href'))
        product_desc_xpath = tree.xpath(
            f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div[2]/a/text()')
        product_desc = ''.join(product_desc_xpath).replace(' ', '').replace('\n', '').replace('\r', '')
        product_id = ''.join(tree.xpath(
            f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div[2]/a/@data-nid'))
        price = ''.join(tree.xpath(
            f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div/div/strong/text()'))
        deal_cnt = ''.join(tree.xpath(
            f'//div[@class="items" and not (contains(@id,"J_itemlistCont" )) ]/div[@data-index="{index}"]/div[contains(@class,"J_IconMoreNew")]/div/div[@class="deal-cnt"]/text()'))

        shop_product_json = {product_id: {
            'product_desc': product_desc,
            'product_url': product_url,
            'price': [{date: price}],
            'deal_cnt': [{date: deal_cnt}],
        }}

        dict_date[shop_name]['shop_product'].append(shop_product_json)

    logger.info(dict_date)
    return dict_date


# 登录TB获取搜索到的店铺页面
async def main(username, password, search_number=None, ip=None):
    browser = await launch(headless=True, slowMo=15, autoClose=False,
                           args=['--disable-infobars', '--mute-audio',
                                 '--no-sandbox', '--disable-gpu', '--disable-setuid-sandbox',
                                 '--disable-translate', '--safebrowsing-disable-auto-update',
                                 '--disable-bundled-ppapi-flash', f'--window-size={WIDTH},{HEIGHT}',
                                 ], dumpio=True)
    page = await browser.newPage()

    # 浏览器设置
    # await page.setJavaScriptEnabled(enabled=True)
    # await page.setRequestInterception(value=True)
    # page.on('request', intercept_request)
    # page.on('response', intercept_response)
    await page.setUserAgent(set_user_agent())
    await page.setViewport({'width': WIDTH, 'height': HEIGHT})
    # await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')


    await asyncio.sleep(1)

    # 淘宝网站的登录
    await page.type('#fm-login-id', username, {'delay': 30})
    await page.type('#fm-login-password', password, {'delay': 50})

    # # 登录页面滑块检测
    # await login_slide(browser, page)
    # if not page:
    #     await page_close(browser)
    #     return False
    # logger.info(f'\n====淘宝账号：{username}，登录成功后的页面实例====\n{page}\n========')
    await page.click('#login-form > div.fm-btn > button')
    await asyncio.sleep(3)
    res = await page.content()

    await page_close(browser)
    return res

    # # 检测维护的账号（伪登录成功）
    # await asyncio.sleep(0.5)
    # try:
    #     maintenance = await page.evaluate('''document.getElementsByClassName("maincenter")''')
    #     if maintenance:
    #         return False
    # except Exception:
    #     pass
    #
    # await asyncio.sleep(5)
    # # await asyncio.sleep(0.5)
    # # 获取要查询的店铺名字
    # global set_shop_name
    # shop_count = 0
    # while True:
    #     if not os.path.exists(SHOP_NAME_SET_PATH):
    #         sheets_list = find_active_sheet(filename=XLSX_FILE_PATH)
    #         set_shop_name = r_sheet_shop_name(sheets_list, filename=XLSX_FILE_PATH)
    #         try:
    #             set_shop_name.remove(None)
    #         except Exception:
    #             pass
    #         shop_name_list = list(set_shop_name)
    #         shop_name_txt = ','.join(str(e) for e in shop_name_list)
    #         open(SHOP_NAME_SET_PATH, 'a').close()
    #
    #         with open(SHOP_NAME_SET_PATH, 'w', encoding='utf8') as f:
    #             f.write(shop_name_txt)
    #         shop_name = set_shop_name.pop()
    #     else:
    #         with open(SHOP_NAME_SET_PATH, 'r', encoding='utf8') as f:
    #             set_shop_name = set(f.read().split(','))
    #         shop_name = set_shop_name.pop()
    #
    #     await asyncio.sleep(1)
    #     if shop_count == 0:
    #         try:
    #             await page.type('#tbSearchContent', shop_name, {'delay': 85})
    #             await asyncio.sleep(0.5)
    #             await page.click('.search-button')
    #             await asyncio.sleep(1)
    #             logger.info(f'正在搜索第{shop_count + 1}个店铺: {shop_name}')
    #         except Exception:
    #             await asyncio.sleep(0.5)
    #             await page_close(browser)
    #             return False
    #     else:
    #         try:
    #             await page.evaluate('document.getElementsByTagName("input")[0].value = ""')
    #             await asyncio.sleep(0.5)
    #             await page.type('#q', shop_name, {'delay': 85})
    #             await asyncio.sleep(0.5)
    #             await page.click('button.submit.icon-btn-search')
    #             await asyncio.sleep(1)
    #             search_bar = await page.evaluate(
    #                 '''document.getElementsByClassName('submit icon-btn-search')[1].innerText''')
    #             await asyncio.sleep(0.5)
    #             if not search_bar:
    #                 await page_close(browser)
    #                 return False
    #             logger.info(f'正在搜索第{shop_count + 1}个店铺: {shop_name}')
    #         except Exception:
    #             await asyncio.sleep(0.5)
    #             await page_close(browser)
    #             return False
    #     await asyncio.sleep(1)
    #     # 商品搜索结果页面滑块检测
    #     try:
    #         slider = await page.Jeval('#nocaptcha', 'node => node.style')
    #         await asyncio.sleep(0.5)
    #         if slider:
    #             return False
    #     except Exception:
    #         pass
    #     await asyncio.sleep(1)
    #
    #     # 店铺内容显示成功后
    #     if page:
    #         await page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    #         await page.evaluate('window.scrollTo({top:0, left:"document.body.scrollHeight", behavior: "smooth"})')
    #         # await page.evaluate('window.scrollBy(0, window.innerHeight)')
    #         await asyncio.sleep(0.5)
    #
    #         # now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    #         # screenshot_path = os.path.join(DATA_PATH, 'shop_screenshot')
    #         # success = await page.screenshot({'path': f'{screenshot_path}/{now_time}-{shop_name}.png'})
    #         # await asyncio.sleep(0.5)
    #
    #         # 保存获取到的商品信息
    #         page_text = await page.content()
    #         # logger.info(page_text)
    #         # pass
    #         dict_date = xpath_parse(html_content=page_text, shop_name=shop_name)
    #
    #         logger.info(f'\n========\n{dict_date}\n========')
    #
    #         # write_json(dict_date)
    #
    #         logger.info(f'第{shop_count + 1}个店铺：{shop_name},已经写入完毕！')
    #
    #         # 删除搜索过的店铺, 写入不成功的店铺
    #         if not dict_date:
    #             set_shop_name.add(shop_name)
    #         shop_name_list = list(set_shop_name)
    #         shop_name_txt = ','.join(str(e) for e in shop_name_list)
    #         if not os.path.exists(SHOP_NAME_SET_PATH):
    #             open(SHOP_NAME_SET_PATH, 'a').close()
    #         with open(SHOP_NAME_SET_PATH, 'w', encoding='utf8') as f:
    #             f.write(shop_name_txt)
    #
    #         if shop_count == search_number or not set_shop_name:
    #             await page_close(browser)
    #             return False
    #         shop_count += 1


def activate(account_no, search_number):
    search_number = search_number
    index = account_no
    loop = asyncio.get_event_loop()

    switch_account = loop.run_until_complete(
        main(username=ALI_ACCOUNT[index]['username'], password=ALI_ACCOUNT[index]['password'],
             search_number=search_number))

    return page_content

    while not switch_account:
        if index + 1 == len(ALI_ACCOUNT):
            index = 0
        else:
            index += 1
        username = ALI_ACCOUNT[index]['username']
        password = ALI_ACCOUNT[index]['password']
        switch_account = loop.run_until_complete(
            main(username=username, password=password, search_number=search_number))
        time.sleep(2)


if __name__ == '__main__':
    # page = activate(0, search_number=5)
    loop = asyncio.get_event_loop()

    page_content = loop.run_until_complete(
        main(username=ALI_ACCOUNT[0]['username'], password=ALI_ACCOUNT[0]['password'], ))

    with open('tb.html', 'w', encoding='utf8') as w:
        w.write(page_content)
