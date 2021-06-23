import shutil
import pandas as pd
import zipfile
import os
import time
from pathlib import Path

from common.logger import logger

app_name = os.path.basename(__file__).split('.')[0]
logger = logger(app_name)

current_path = Path.cwd()
de_tmp_path = '../tmp'
origin = r'C:\Users\ht\docs\地址清洗全国数据-运单数据'
save_path = r'C:\Users\ht\Desktop\waybill'

start_time = time.time()
logger.info('开始地址清洗数据切割')

# 所有的zip文件
all_zip_file = [f for f in Path(origin).glob('*') if str(f).endswith('.zip')]
logger.info(f'共计{len(all_zip_file)}个压缩文件')

for i, name in enumerate(all_zip_file):
    logger.info(i + 1, name)

# """
# 逐个对zip文件进行操作
for zip_file in all_zip_file:
    # zip_file = all_zip_file[31] # 测试38.zip这个最大的压缩文件包。
    zip_file_obj = zipfile.ZipFile(zip_file)
    # 一个一个解压zip文件里的子文件
    zip_file_list = zip_file_obj.filelist
    logger.info(f'{zip_file}里面的文件有:')
    for file_info in zip_file_list:
        logger.info(f'{file_info}')

    logger.info(f'将要解压zip文件{zip_file}里的{len(zip_file_list)}个文件')
    file_number = 0

    for file_info in zip_file_list:
        try:
            extract_res = zip_file_obj.extract(member=file_info, path=de_tmp_path)
            logger.info(f'解压第{file_number + 1}个文件, 解压成功后,文件为: {extract_res}')
        except Exception as e:
            logger.info(f'——————解压错误：{e}——————')
            pass
        file_name = str(Path(extract_res).parts[1]).split('.')[0]
        file_name_list = file_name.split(' ')

        # 从文件名字中提取省市区。
        province_path = Path(file_name_list[0])
        city_path = Path(file_name_list[1])
        logger.info(f'文件名: 【{file_name}】,省目录名: <{province_path}> 城市目录名: <{city_path}>')

        # 解压后的文件绝对路径
        csv_file_path = os.path.join(str(current_path), extract_res)

        # 切割给定csv文件，之后的每个文件小于500000行。
        try:
            rows = pd.read_csv(csv_file_path, index_col=False, chunksize=500000, encoding='gbk', low_memory=False)
        except Exception as e:
            logger.info(f'——————空文件{e}——————')
            mkdir_file_name = Path(save_path + '/', str(province_path) + '/' + str(city_path))
            Path.mkdir(mkdir_file_name, parents=True, exist_ok=True)

            dst = os.path.join(save_path, str(province_path), str(city_path), f'{file_name}1.csv')
            shutil.copy(csv_file_path, dst)
            continue

        logger.info(f'文件{csv_file_path}读取成功， 开始切割文件。')
        try:
            for i, chuck in enumerate(rows):
                mkdir_file_name = Path(save_path + '/', str(province_path) + '/' + str(city_path))
                if i == 0:
                    Path.mkdir(mkdir_file_name, parents=True, exist_ok=True)
                    logger.info(f'目录{mkdir_file_name}， 创建成功')
                    chuck.to_csv(os.path.join(save_path, str(province_path), str(city_path), f'{file_name}{i + 1}.csv'),
                                 index=False, encoding='gbk')
                logger.info(f'文件{csv_file_path}完成第【{i + 1}】次切割。')
        except Exception as e:
            logger.info(f'第【{all_zip_file.index(zip_file)}】个压缩文件')
            logger.info(f'压缩文件里的第【{file_name_list.index(file_info)}】个csv文件')
            logger.info(f'\n所有的csv文件: {file_name_list}\n 当前csv文件: {file_name}')
            logger.info(f'——————error：{e}——————')
            continue
        # break
        will_del = os.path.join(str(current_path), extract_res)
        os.remove(will_del)
        file_number += 1
        logger.info(f'第【{file_number}】个文件{csv_file_path} 切割完成。。。\n——————【{will_del}】文件已删除——————\n')
        # break
    logger.info(f'第【{all_zip_file.index(zip_file)}】个压缩文件{zip_file}，全部切割完成。。。\n\n')
    # break

logger.info(f'花费时间{time.time() - start_time}s')
# """
