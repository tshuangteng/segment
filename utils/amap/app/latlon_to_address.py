import codecs

import pandas as pd
import numpy as np
from random import randint
import urllib3

from common.logger import logger
from app.constant import KEY
from utils.amap import lat_lon_decimal, get_request_api, lonlat_to_location, api_usability
from utils.text import excel_to_txt, text_to_excel

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
log = logger(app_name='app', file_name=__name__)

origin_file = 'latlon.xlsx'
# save_file = 'save_lonlat.xlsx'
URL = 'https://restapi.amap.com/v3/geocode/regeo?'
#
# key = 'a1616c46d97c4161fdf506b9f1c43163'
#

df = pd.read_excel(origin_file, engine='openpyxl')
df_rows = df.shape[0]

excel_to_txt(excel_file='latlon.xlsx', text_file='latlon_tmp.txt')


def text_line_append(txt_file, save_file, index, rows_info):
    with codecs.open(txt_file, 'r', 'utf-8') as f, open(save_file, 'a', encoding='utf8') as fw:
        data = f.readlines()[index + 1]
        line = data + '    ' + rows_info
        fin = line.replace('\n', '')
        fw.write(fin + '\n')
        log.info(f'成功写入第{index}行，文件：{save_file}')


for index in range(df_rows + 1):
    if index == 14000:
        key = KEY[3]
    elif index == 28000:
        key = KEY[4]
    else:
        key = KEY[2]

    if index == 0:
        rows_info = '地址1    地址2'
    else:
        express_service_point = df.loc[[index - 1], ['经纬度1']]
        lonlat1 = np.array(express_service_point).tolist()[0][0]

        express_service_point = df.loc[[index - 1], ['经纬度2']]
        lonlat2 = np.array(express_service_point).tolist()[0][0]

        lonlat = lat_lon_decimal(lonlat1)
        lonlat2 = lat_lon_decimal(lonlat2)
        location1 = lonlat_to_location(url=URL, key=key, lonlat=lonlat)
        location2 = lonlat_to_location(url=URL, key=key, lonlat=lonlat2)
        rows_info = f'{location1}    {location2}'
    text_line_append(txt_file='latlon_tmp.txt', save_file='save2_latlon.txt', index=index, rows_info=rows_info)

text_to_excel('save2_latlon.txt', 'save2_latlon.xls')