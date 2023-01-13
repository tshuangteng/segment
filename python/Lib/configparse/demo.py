import configparser
import os

# 读取配置文件
try:
    # CONFIG_PATH = os.environ['CONFIG_PATH']
    CONFIG_PATH = ('./config.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8')
    wgc_code = config['wgc_info']['wgc_code']
    wgc_name = config['wgc_info']['wgc_name']
    origin_image = int(config['save_image']['origin_image'])
    no_read = int(config['save_image']['no_read'])
    fj_api = config['fj_api']['fj_api']
except Exception as e:
    print(f'read config error: {e}')
    no_read = 0
    origin_image = 0
    wgc_code = 0
    wgc_name = 0
    fj_api = ''
