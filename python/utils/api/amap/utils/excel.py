import pandas as pd
from pathlib import Path

from common.logger import logger

log = logger(app_name='app', file_name=__name__)


def generate_excel_file(file_name):
    """
    :param file_name: 绝对路径 full path
    :return:
    """
    file_path = Path(file_name)
    if Path.exists(file_path) and Path.is_file(file_path):
        log.info(f'Excel输出文件: {file_name}, 已存在。')
    else:
        Path.touch(file_path)
        # 设置Excel文件的默认header
        df = pd.DataFrame(columns=['网点', '代收点', '距离', '驾驶距离', '驾驶时长', '骑行距离', '骑行时长', '步行距离', '步行时长'])
        df.to_excel(file_name, sheet_name='Sheet1', index=False, header=True, encoding='utf8')
        log.info(f'Excel输出文件：{file_name}, 已创建。')
    df = pd.DataFrame(pd.read_excel(file_name))
    df_rows_cols = df.shape
    log.info(f'Excel file: row, col --> {df_rows_cols}')
    df_rows = df.shape[0]
    return df_rows


def init_excel(file_name):
    distance, driving_dis, driving_dur, bicycling_dis, bicycling_dur, walking_dis, walking_dur = '距离', '驾驶距离', '驾驶时长', '骑行距离', '骑行时长', '步行距离', '步行时长'
    cols_info = [distance, driving_dis, driving_dur, bicycling_dis, bicycling_dur, walking_dis, walking_dur]

    origin_df = pd.read_excel(file_name)
    if '距离' in origin_df.columns:
        log.info(f'文件存在。')
        pass
    else:
        df = pd.concat([origin_df, pd.DataFrame(columns=cols_info)])
        df.to_excel(file_name, sheet_name='Sheet1', index=False, header=True)
        log.info(f'文件新增columns成功。')


def append_row(file_name, rows_info):
    distance, driving_dis, driving_dur, bicycling_dis, bicycling_dur, walking_dis, walking_dur = '距离', '驾驶距离', '驾驶时长', '骑行距离', '骑行时长', '步行距离', '步行时长'

    origin_df = pd.read_excel(file_name)
    row_num, column_num = origin_df.shape

    df = pd.DataFrame(origin_df)
    row = {distance: rows_info[0], driving_dis: rows_info[1], driving_dur: rows_info[2], bicycling_dis: rows_info[3],
           bicycling_dur: rows_info[4], walking_dis: rows_info[5], walking_dur: rows_info[6]}
    for i in range(row_num):
        end_df = df.append(row, ignore_index=True)
        end_df.to_excel(file_name, sheet_name='Sheet1', index=False, header=True)
