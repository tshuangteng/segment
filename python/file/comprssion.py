# from zipfile import ZipFile
import time
import zipfile
import os
from os.path import basename
from pathlib import Path
from common.logger import logger

app_name = os.path.basename(__file__).split('.')[0]
logger = logger(app_name)
# origin = r'C:\Users\ht\Desktop\切割-运单数据'
origin = r'C:\Users\ht\Desktop\abcd'
save_path = r'C:\Users\ht\Desktop\abcd'
all_folder = [f for f in Path(origin).glob('*') if not str(f).endswith('.zip')]
logger.info(f'---{len(all_folder)}---')

for f in all_folder:
    logger.info(f)

for f in all_folder:
    zip_folder_name = str(f).split('\\')[-1]
    start_time = time.time()
    logger.info(f'{zip_folder_name}开始压缩')
    with zipfile.ZipFile(os.path.join(save_path, f'{zip_folder_name}.zip'), 'w', zipfile.ZIP_DEFLATED) as zip_obj:
        for root, dirs, files in os.walk(str(f)):
            for file in files:
                zip_obj.write(os.path.join(root, file))
                # break
            break
    logger.info(f'第{all_folder.index(f)}个{f} 压缩完成, 使用了{time.time() - start_time}')


