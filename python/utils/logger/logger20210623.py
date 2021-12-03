"""
python >= 3.6
"""
import os
import logging
from pathlib import Path
from datetime import datetime


def generate_logfile(log_file_name):
    stat_date = str(datetime.today().date()).replace('-', '')
    current_file = os.path.abspath(__file__)
    parents_path = Path(current_file).parent.parent

    log_path = Path(f'{parents_path}/log/{stat_date}')
    if not Path.exists(log_path):
        Path.mkdir(log_path, parents=True, exist_ok=True)
    log_file = Path(f'{log_path}/{log_file_name}.log')

    return log_file


def my_logger(log_file_name, file_name=__name__):
    log_file = generate_logfile(log_file_name)

    log = logging.getLogger(file_name)
    log.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s -%(funcName)s - %(lineno)d - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

    return log
