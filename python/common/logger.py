import logging
import sys
from pathlib import Path
from python.common.constant import PROJECT_PATH
from datetime import datetime


def generate_logfile(app_name):
    """Get current platform name by short string."""
    project_name = str(PROJECT_PATH.parts[-1])
    # stat_date = datetime.today().date() - timedelta(days=1)
    stat_date = datetime.today().date()

    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        log_path = Path('/{}/log/{}'.format(project_name, stat_date))
        if not Path.exists(log_path):
            Path.mkdir(log_path, parents=True, exist_ok=True)
        log_file = Path('{}/{}.log'.format(log_path, app_name))
        return log_file

    elif (sys.platform.startswith('win') or
          sys.platform.startswith('msys') or
          sys.platform.startswith('cyg')):
        log_path = Path('{}/log/{}'.format(PROJECT_PATH, stat_date))
        if not Path.exists(log_path):
            Path.mkdir(log_path, parents=True, exist_ok=True)
        log_file = Path('{}/{}.log'.format(log_path, app_name))
        return log_file
    else:
        raise OSError('Unsupported platform: ' + sys.platform + ', and unable create log file.')


def my_logger(app_name, file_name=__name__):
    """setting logger"""
    log_file = generate_logfile(app_name)
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
