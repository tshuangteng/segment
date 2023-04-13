import logging
from logging.handlers import TimedRotatingFileHandler

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0


class MyLogger(logging.Logger):
    def __init__(self, log_name, log_path, log_level='DEBUG', file=True, console=False):
        self.log_name = log_name
        self.log_path = log_path
        self.log_level = log_level

        # 使用父类的实例来初始化
        # logging.Logger.__init__(self, self.log_name, self.log_level)
        super().__init__(self.log_name, self.log_level)

        if file:
            self.__setFileHandler__()

        if console:
            self.__setStreamHandler__()

    def __setFileHandler__(self):
        log_file = f'{self.log_path}/{self.log_name}.log'
        file_handler = TimedRotatingFileHandler(log_file, when='D', interval=1, backupCount=7, encoding='utf-8')
        file_handler.suffix = "%Y%m%d.log"

        # test output log file by second
        # file_handler = TimedRotatingFileHandler(log_file, when='S', interval=2, backupCount=7, encoding='utf-8')
        # file_handler.suffix = "%Y%m%d_%H%M%S.log"

        formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s -%(funcName)s - %(lineno)d - %(message)s')
        file_handler.setFormatter(formatter)

        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self):
        formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s -%(funcName)s - %(lineno)d - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.stream_handler = stream_handler
        self.addHandler(stream_handler)


if __name__ == '__main__':
    # import time
    #
    # logger = MyLogger('app', './log', console=True)
    # number = 1
    # while 1:
    #     logger.info(f'app logging test -------  {number}')
    #     number += 1
    #     time.sleep(1)
    pass
