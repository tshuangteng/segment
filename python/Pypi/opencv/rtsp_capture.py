import os
import cv2
from pathlib import Path
import concurrent.futures
from datetime import datetime, timedelta

from logger import my_logger, PROJECT_PATH

current_file_path = os.path.abspath(__file__)

logger = my_logger('screen_shot')

sxt = [
    'rtsp://admin:xxx@219.136.186.58:1556/cam/realmonitor?channel=8&subtype=0',
    'rtsp://admin:xxx@219.136.186.58:1556/cam/realmonitor?channel=14&subtype=0',
]

# 从rtsp摄像头地址视频截图
def capture_img(rtsp_url, name, str_time):
    """
    :param rtsp_url: 摄像头视频地址,rtsp协议
    :return:
    """
    logger.info(f'获取 {rtsp_url} 截图')
    try:
        cap = cv2.VideoCapture(rtsp_url)
    except Exception as error:
        logger.info(f'cv2的VideoCapture方法报错: {error}')
        return None, None

    now_datetime = datetime.now()
    capture_time = now_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # now_datetime = datetime.now()
    if cap.isOpened():
        ret, frame = cap.read()
        date_format_path = Path(PROJECT_PATH, 'img', name)
        os.makedirs(date_format_path, exist_ok=True)

        # image_name = f'{now_datetime.strftime("%Y%m%d-%H%M%S")}.jpg'
        image_name = f'{str_time}.jpg'
        image_full_path = str(Path(date_format_path, image_name))
        cv2.imwrite(image_full_path, frame)
        return capture_time, True
    else:
        logger.info('截图获取出错，请检查摄像头视频地址是否正确！')
        return capture_time, None


if __name__ == '__main__':
    start_str_date = '2022_02_18_00_00_00'
    start_date = datetime.strptime(start_str_date, '%Y_%m_%d_%H_%M_%S')
    str_time_list = []
    str_time_list.append(start_date.strftime('%Y_%m_%d_%H_%M_%S'))
    while 1:
        date_time = start_date + timedelta(minutes=5)
        str_time = date_time.strftime('%Y_%m_%d_%H_%M_%S')
        if str_time == '2022_02_18_22_00_00':
            break
        str_time_list.append(str_time)
        start_date = date_time

    number = 1
    for rtsp in sxt:
        foo = 1
        for str_time in str_time_list:
            playback_rtsp = f'{rtsp.replace("realmonitor", "playback")}&starttime={str_time}'
            capture_img(playback_rtsp, f'sc{number}', str_time)
            logger.info(f'--- {number} --- {foo} ---')
            foo += 1
        number += 1

    # rtsp = 'rtsp://admin:biewenwo110@219.136.186.58:1556/cam/playback?channel=8&subtype=0&starttime=2022_02_18_00_00_00'
    # capture_img(rtsp)

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     future_to_detect = {executor.submit(capture_img, rtsp_url=rtsp): rtsp
    #                         for rtsp in get_url_list}
    #
    #     for future in concurrent.futures.as_completed(future_to_detect):
    #         result = future.result()
