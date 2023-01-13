# import time
# import configparser
# import os
#
#
# while 1:
#     a_while_start = time.time()
#     # 读取配置文件
#     try:
#         # CONFIG_PATH = os.environ['CONFIG_PATH']
#         CONFIG_PATH = './conf/config.ini'
#         config = configparser.ConfigParser()
#         config.read(CONFIG_PATH, encoding='utf-8')
#         wgc_code = config['wgc_info']['wgc_code']
#         wgc_name = config['wgc_info']['wgc_name']
#         origin_image = int(config['save_image']['origin_image'])
#         print('origin-image', origin_image)
#         no_read = int(config['save_image']['no_read'])
#         print('no-read', no_read)
#         fj_api = config['fj_api']['fj_api']
#     except Exception as e:
#         print(f'read config error: {e}')
#         no_read = 0
#         origin_image = 0
#         wgc_code = 0
#         wgc_name = 0
#         fj_api = ''
#
#     if not no_read:
#         print(no_read)
#
#     time.sleep(5)
#

# pip install func_timeout -i https://pypi.doubanio.com/simple
from func_timeout import func_set_timeout, FunctionTimedOut
import time


@func_set_timeout(0.2)
def mytest():
    print("Start")
    for i in range(1, 10):
        print("%d seconds have passed" % i)
        time.sleep(1)


if __name__ == '__main__':
    now = time.time()

    try:
        mytest()
    except FunctionTimedOut as e:
        print('mytest2:::', e)
    print('finish test')

    print(time.time() - now)
