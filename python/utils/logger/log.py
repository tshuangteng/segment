import logging
import os
import sys
from pathlib import Path
from datetime import datetime

_current_file_path = os.path.abspath(__file__)
project_path = Path(_current_file_path).parent.parent.parent


def generate_logfile(log_file_name):
    """Get current platform name by short string."""
    stat_date = str(datetime.today().date()).replace('-', '')

    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        log_path = Path(project_path, f'log/{stat_date}')
        if not Path.exists(log_path):
            Path.mkdir(log_path, parents=True, exist_ok=True)
        log_file = Path(f'{log_path}/{log_file_name}.log')
        return log_file

    elif (sys.platform.startswith('win') or
          sys.platform.startswith('msys') or
          sys.platform.startswith('cyg')):
        log_path = Path(f'{project_path}/log/{stat_date}')
        if not Path.exists(log_path):
            Path.mkdir(log_path, parents=True, exist_ok=True)
        log_file = Path(f'{log_path}/{log_file_name}.log')
        return log_file
    else:
        raise OSError('Unsupported platform: ' + sys.platform + ', and unable create log file.')


def mylogger(log_file_name, file_name=__name__):
    """setting logger"""
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
