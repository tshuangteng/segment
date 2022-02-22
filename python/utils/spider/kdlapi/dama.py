# #!/usr/bin/env python3
# from configparser import ConfigParser
# from splinter import Browser
# import time
# from bs4 import BeautifulSoup
# import base64
# import json
# import requests
# from PIL import Image
# import urllib
# import time
#
# browser = Browser(driver_name='chrome', headless=False, executable_path=r'C:\Users\ht\Desktop\chrome\chromedriver.exe')
# browser.visit('https://my.alipay.com/portal/i.htm?referer=https%3A%2F%2Fauth.alipay.com%2F')
# browser.find_by_xpath('//*[@id="J-loginMethod-tabs"]/li[2]').click()
# browser.find_by_xpath('//*[@id="J-input-user"]').fill('账号')
# browser.find_by_xpath('//*[@id="password_rsainput"]').fill('密码')
# browser.driver.save_screenshot('bdbutton.png')
#
# element = browser.driver.find_element_by_xpath('//*[@id="J-checkcode-img"]')  # 找到验证码图片
# print(element.location)  # 打印元素坐标
# print(element.size)  # 打印元素大小
# left = element.location['x']
# top = element.location['y']
# right = element.location['x'] + element.size['width']
# bottom = element.location['y'] + element.size['height']
# im = Image.open('bdbutton.png')
# im = im.crop((left, top, right, bottom))
# im.save('bdbutton.png')
#
#
# def base64_api(uname, pwd, img, typeid):
#     with open(img, 'rb') as f:
#         base64_data = base64.b64encode(f.read())
#         b64 = base64_data.decode()
#     data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#     result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         return result["message"]
#     # return ""
#
#
# result = base64_api(uname='kelvinlyw', pwd='liyunwen0506', img='bdbutton.png', typeid=3)
# print(result)
# browser.find_by_xpath('//*[@id="J-input-checkcode"]').fill(result)
# browser.find_by_xpath('//*[@id="J-login-btn"]').click()
# time.sleep(3)
