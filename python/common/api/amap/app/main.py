import time
from random import randrange
import urllib3
import pandas as pd
import numpy as np

from app.constant import DISTANCE_API, DRIVING_API, WALKING_API, BICYCLING_API, KEY, EXCEL_FILE, NEW_EXCEL_FILE
# from app.constant import TXT_FILE, TMP_TXT_FILE
from common.logger import logger
from utils.excel import generate_excel_file, append_row, init_excel
from utils.amap import get_request_api, api_usability, lat_lon_decimal
from utils.text import excel_to_txt, text_line_append, text_to_excel

log = logger(app_name='app', file_name=__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# excel_file = new_excel_file = EXCEL_FILE
excel_file = 'latlon.xlsx'
# txt_file = TXT_FILE
txt_file = 'new.txt'

df = pd.read_excel(excel_file, engine='openpyxl')
# row_num, column_num = df.shape

df_rows = df.shape[0]
df_cols = df.shape[1]

for index in range(df_rows + 1):
    global key
    # 一个key最多使用30000次，本程序for一次4个请求。
    index_func_call_number = 30000 // 4 - 5
    split_number = df_rows // index_func_call_number

    if split_number == 0:
        key = KEY[0]
    else:
        for i in range(split_number):
            if index == 0:
                key = KEY[i]
                break
            elif index == (i + 1) * index_func_call_number:
                key = KEY[i + 1]
                break

    if index == 0:
        rows_info = ['网点', '代收点', '距离', '驾驶距离', '驾驶时长', '骑行距离', '骑行时长', '步行距离', '步行时长']
    else:
        # express_service_point = df.loc[[index-1], ['网点经纬度']]
        express_service_point1 = df.loc[[index - 1], ['经纬度1']]
        # express_collection_lat = df.loc[[index-1], ['经度']]
        # express_collection_lon = df.loc[[index-1], ['纬度']]
        express_service_point2 = df.loc[[index - 1], ['经纬度2']]

        org = np.array(express_service_point1).tolist()[0][0]
        origin = lat_lon_decimal(org)

        des = np.array(express_service_point2).tolist()[0][0]
        destination = lat_lon_decimal(des)

        # destination_lat = np.array(express_collection_lat).tolist()[0][0]
        # destination_lon = np.array(express_collection_lon).tolist()[0][0]
        # destination = f'{destination_lat},{destination_lon}'
        # destination = lat_lon_decimal(destination)
        log.info(f'获取第{index - 1}行数据，选择的key: {key}')

        distance = get_request_api(key=key, origin=origin, destination=destination, api_url=DISTANCE_API)[0]
        driving_res = get_request_api(key=key, origin=origin, destination=destination, api_url=DRIVING_API)
        driving_distance, driving_duration = driving_res[0], driving_res[1]

        bicycling_res = get_request_api(key=key, origin=origin, destination=destination, api_url=BICYCLING_API)
        bicycling_distance, bicycling_duration = bicycling_res[0], bicycling_res[1]

        walking_res = get_request_api(key=key, origin=origin, destination=destination, api_url=WALKING_API)
        walking_distance, walking_duration = walking_res[0], walking_res[1]

        rows_info = [distance, driving_distance, driving_duration, bicycling_distance,
                     bicycling_duration, walking_distance, walking_duration]

    text_line_append(txt_file=txt_file, save_file='save30000.txt', index=index, rows_info=rows_info)

# time.sleep(10)
# text_to_excel(text_file='save30000.txt', excel_file='save30000.xls')
