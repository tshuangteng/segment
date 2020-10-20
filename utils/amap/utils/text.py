import pandas as pd
import re
import xlwt
import codecs
from common.logger import logger

logger = logger(app_name='app', file_name=__name__)


def excel_to_txt(excel_file, text_file):
    with codecs.open(text_file, 'w', 'utf-8') as f:
        neg = pd.read_excel(excel_file, header=None, index=None)
        f.write(neg.to_string())


def text_line_append(txt_file, save_file, index, rows_info):
    with codecs.open(txt_file, 'r') as f, open(save_file, 'a') as fw:
        data = f.readlines()[index + 1].replace('\t', '').replace('\n', '')
        append_info = '    '.join(str(e) for e in rows_info)
        line = data + '    ' + append_info
        fin = line.replace('\n', '').replace('\t', '')
        logger.info(fin)
        fw.write(fin + '\n')
        logger.info(f'成功写入第{index}行，文件：{save_file}')


def text_to_excel(text_file, excel_file):
    book = xlwt.Workbook()
    ws = book.add_sheet('Sheet1')

    f = open(text_file, 'r', encoding='utf8')
    data = f.readlines()

    for i in range(len(data)):
        row = data[i].split()
        for j in range(len(row)):
            ws.write(i, j, row[j])
            logger.info(f'第{i}行写入成功。')
    book.save(excel_file)
    f.close()

# text_to_excel('save_latlon.txt', 'save_latlon.xls')
