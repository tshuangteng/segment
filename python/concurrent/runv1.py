import os

import cv2
import requests
import json
import re
import time
import timeout_decorator

from uuid import uuid4
from datetime import datetime
from pathlib import Path
import concurrent.futures

from common.constant import UNIFORM_ORIGIN_IMG, UNIFORM_API, FRONT_END_URL, FB_CODE, IMG_HOST, PROJECT_PATH
from common.mysql_manager import DbManager

from common.constant import MYSQL_PASS, MYSQL_USER, MYSQL_DB, MYSQL_PORT, MYSQL_HOST, ORIGIN_INFO_TABLE
from common.logger import my_logger

file_name = os.path.basename(__file__).split('.')[0]

logger = my_logger(file_name)


# 从rtsp摄像头地址视频截图
@timeout_decorator.timeout(8, use_signals=False)
def get_img_from_rtsp(video_url):
    """
    :param video_url:  摄像头视频地址,rtsp协议
    :return:
        check_time: 截图时间
        path_name: 截图文件存放地址,完整的绝对路径.
        url_suffix: 图片查看服务中,域名后需要拼接的地址内容.
    """
    logger.info(f'获取 {video_url} 截图')
    try:
        cap = cv2.VideoCapture(video_url)
        check_time = None
        if cap.isOpened():
            ret, frame = cap.read()
            now_datetime = datetime.now()
            check_time = now_datetime.strftime('%Y-%m-%d %H:%M:%S')
            img_directory = str(now_datetime.date().strftime('%Y%m%d'))
            img_date_path = str(Path(UNIFORM_ORIGIN_IMG, img_directory))
            os.makedirs(img_date_path, exist_ok=True)
            img_name = str(now_datetime.strftime('%Y%m%d-%H%M%S') + f'-{uuid4()}.jpg')
            # img_suffix_path = Path('img/img_origin', img_name)
            path_name = str(Path(img_date_path, img_name))
            cv2.imwrite(path_name, frame)
            # url_suffix = str(Path('worn', img_directory, img_name))

            img_date_suffix_path = path_name.split('img_origin/')[1]
            return check_time, img_date_suffix_path
        else:
            logger.info('截图获取出错，请检查摄像头视频地址是否正确！')
            return check_time, None

    except Exception as e:
        logger.info(f'cv2的VideoCapture方法报错: {e}')
        return None, None


def integration_detect_data(video_url, fb_code, aisle_name, standard_set):
    """
    :param video_url: 摄像头视频地址,rtsp协议
    :param fb_code: 分拨中心编码
    :param aisle_name:  摄像头通道名称
    :return:
    """

    try:
        three_res = get_img_from_rtsp(video_url)
    except Exception as e:
        three_res = None
        logger.error(f'{e}------请求摄像头地址 已超过设置的timeout')

    try:
        aisle_num = re.match(r'.*channel=(\d+)?.*', video_url).group(1)
    except Exception as e:
        aisle_num = 0
        logger.info(f'正则获取通道号: {e}')

    if not three_res:
        check_time, path_name = None, None
    else:
        check_time, path_name = three_res[0], three_res[1]

    if not path_name:
        res_json = {
            "frockData": [
                {
                    "fb_code": fb_code,
                    "aisle_name": aisle_name,
                    "check_time": check_time,
                    "aisle_num": aisle_num,
                    "illegal_num": 0,
                    "pictureUrl": None,
                    "is_valid": 0,  # 1 生效, 0 无效
                    "standard_set": 0
                }
            ]
        }
        return res_json

    # 修改img映射的目录名到拼接字符串中
    body = {'path_name': f'/usr/src/uniform/img/img_origin/{str(path_name)}'}

    # prd  请求uniform容器的api服务，需提前绑定uniform容器来直接映射为ip
    resp = requests.post(UNIFORM_API, data=json.dumps(body)).text

    response = json.loads(resp)
    total = response['data']['total']
    worn = response['data']['worn']
    no_wear = response['data']['no_wear']

    if total != worn:
        standard_set = standard_set
    else:
        standard_set = 0

    res_json = {
        "frockData": [
            {
                "fb_code": fb_code,
                "aisle_name": aisle_name,
                "check_time": check_time,
                "aisle_num": aisle_num,
                "illegal_num": no_wear,
                # pictureUrl 需要分拨服务器的外网ip加容器expose端口号.
                "pictureUrl": f'http://{IMG_HOST}/worn/{path_name}',
                "is_valid": 1,
                "standard_set": standard_set
            }
        ]
    }

    return res_json


def run_entry(fb_code, db_pool):
    columns = None
    try:
        # 首先从前端数据库表中获取几个字段
        _, columns = db_pool.select_many(f"select * from {ORIGIN_INFO_TABLE} where fb_code = {fb_code}")
    except Exception as e:
        logger.warning(f'连接数据库,查询分拨编码{fb_code}出错. {e}')
    db_pool.close()

    # 获取算法识别的结果,并整合数据.
    if columns:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_detect = {executor.submit(integration_detect_data, video_url=column['video_url'], aisle_name=column['aisle_name'], standard_set=column['standard_set'], fb_code=fb_code): column
                                for column in columns}
            for future in concurrent.futures.as_completed(future_to_detect):
                now = time.time()

                result = future.result()
                try:
                    final_response = requests.post(FRONT_END_URL, data=json.dumps(result), headers={'Content-Type': 'application/json;charset=UTF-8'})
                    logger.info(f'http status code: {final_response.status_code}')
                except Exception as e:
                    logger.warning(f'给前端传参,请求不通! \n {e}')
                logger.info(f'\n ========== 通道名 {future_to_detect[future]["aisle_name"]} 请求时间: {time.time() - now} ============\n{result}\n========================\n')

    else:
        logger.info(f'通过{fb_code}查询的数据库数据为空')


if __name__ == '__main__':
    db_pool = DbManager(host=MYSQL_HOST, port=MYSQL_PORT, db_name=MYSQL_DB, user_name=MYSQL_USER, password=MYSQL_PASS)
    run_entry(FB_CODE, db_pool=db_pool)
    # db_pool.close()
