import os
import shutil
import time
from datetime import datetime
import codecs
import pandas as pd
from pathlib import Path


# 修复源文件的乱码
def fixed_decode_error(new_csv_file):
    with codecs.open(csv_file_path, 'r', encoding='gbk', errors='ignore') as rf, codecs.open(new_csv_file, 'w', encoding='gbk') as wf:
        content = rf.readlines()
        i = 0
        for line in content:
            if i == 0:
                print(line)
            wf.writelines(line)
            i += 1


# # 对修复完乱码的文件重新切割
# save_path = r'C:\Users\ht\Desktop\waybill'
file_name = '贵州省 六盘水市 盘县'
province_path = '贵州省'
city_path = '六盘水市'


def split_csv_from_fixed(fixed_csv_file):
    rows = pd.read_csv(fixed_csv_file, index_col=False, chunksize=5000, low_memory=False, encoding='gbk')
    # rows = pd.read_csv(csv_file_path, index_col=False, chunksize=500000, error_bad_lines=True, low_memory=False, encoding='gbk')

    for i, chuck in enumerate(rows):
        # mkdir_file_name = Path(save_path + '/', str(province_path) + '/' + str(city_path))
        # if i == 0:
        #     Path.mkdir(mkdir_file_name, parents=True, exist_ok=True)
        # chuck.to_csv(os.path.join(save_path, str(province_path), str(city_path), f'{file_name}{i + 1}.csv'), index=False, encoding='gbk')
        chuck.to_csv(f'{file_name}{i + 1}.csv', index=False, encoding='gbk')
        print(f'文件{csv_file_path}完成第【{i + 1}】次切割。')


if __name__ == '__main__':
    # csv_file_path是有乱码的源文件
    csv_file_path = r'21/贵州省 六盘水市 盘县.csv'
    new_csv = r'./fixed.csv'

    fixed_decode_error(new_csv)
    split_csv_from_fixed(new_csv)
