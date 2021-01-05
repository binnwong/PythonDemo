# coding=utf-8
# import logging
#
#
# file_name = 'logger.txt'
# formatter = '%(asctime)s -- %(filename)s[line:%(lineno)d] %(levelname)s\t%(message)s'
# logging.basicConfig(format=formatter, level=logging.DEBUG)
# # logging.basicConfig(filename=file_name, format=formatter, level=logging.DEBUG)
#
# logger = logging.getLogger(__name__)
#
# logger.debug('debug10')
# logger.info('info20')
# logger.warning('warning30')
# logger.error('error40')
# logger.critical('critical50')


# import logging
#
#
# file_name = 'logger.txt'
# formatter = '%(asctime)s -- %(filename)s[line:%(lineno)d] %(levelname)s\t%(message)s'
# logging.basicConfig(filename=file_name, format=formatter, level=logging.DEBUG)
#
# logger = logging.getLogger(__name__)
#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setLevel(20)
# console_formatter = logging.Formatter('%(asctime)s - %(filename)s - [line]:%(lineno)d - %(levelname)s - %(message)s')
# console.setFormatter(console_formatter)
# logger.addHandler(console)
#
# logger.debug('debug->10')
# logger.info('info->20')
# logger.warning('warning->30')
# logger.error('error->40')
# logger.exception('exception->40')
# logger.critical('critical->50')
# logger.fatal('fatal->50')


# import logging
#
#
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
#
# formatter = '%(asctime)s -<>- %(filename)s -<>- [line]:%(lineno)d -<>- %(levelname)s -<>- %(message)s'
# file_handler = logging.FileHandler('log.txt')
# file_handler.setLevel(level=logging.INFO)
# log_formatter = logging.Formatter(formatter)
# file_handler.setFormatter(log_formatter)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(level=logging.INFO)
# console_formatter = logging.Formatter(formatter)
# console_handler.setFormatter(console_formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
#
# logger.info('info')
# logger.error('error')


# import logging
# from logging.handlers import TimedRotatingFileHandler
# import time
#
#
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
#
# formatter = '%(asctime)s -<>- %(filename)s -<>- [line]:%(lineno)d -<>- %(levelname)s -<>- %(message)s'
# time_rotate_file = TimedRotatingFileHandler(filename='time_rotate', when='S', interval=2, backupCount=5)
# time_rotate_file.setFormatter(logging.Formatter(formatter))
# time_rotate_file.setLevel(logging.INFO)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(level=logging.INFO)
# console_handler.setFormatter(logging.Formatter(formatter))
#
# logger.addHandler(time_rotate_file)
# logger.addHandler(console_handler)
#
# while True:
#     logger.info('info')
#     logger.error('error')
#     time.sleep(1)


# import logging
# from logging.handlers import RotatingFileHandler
# import time
#
#
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
#
# formatter = '%(asctime)s -<>- %(filename)s -<>- [line]:%(lineno)d -<>- %(levelname)s -<>- %(message)s'
# size_rotate_file = RotatingFileHandler(filename='size_rotate', maxBytes=1*1024, backupCount=5)
# size_rotate_file.setFormatter(logging.Formatter(formatter))
# size_rotate_file.setLevel(logging.INFO)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(level=logging.INFO)
# console_handler.setFormatter(logging.Formatter(formatter))
#
# logger.addHandler(size_rotate_file)
# logger.addHandler(console_handler)
#
# while True:
#     logger.info('info')
#     logger.error('error')
#     time.sleep(1)


import logging
from logging.handlers import RotatingFileHandler
from threading import Lock


class LoggerProject(object):

    def __init__(self):
        self.mutex = Lock()
        self.formatter = '%(asctime)s -<>- %(filename)s -<>- [line]:%(lineno)d -<>- %(levelname)s -<>- %(message)s'

    def _create_logger(self):
        _logger = logging.getLogger(__name__)
        _logger.setLevel(level=logging.INFO)
        return _logger

    def _file_logger(self):
        size_rotate_file = RotatingFileHandler(filename='size_rotate', maxBytes=1024*1024, backupCount=5)
        size_rotate_file.setFormatter(logging.Formatter(self.formatter))
        size_rotate_file.setLevel(logging.INFO)
        return size_rotate_file

    def _console_logger(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level=logging.INFO)
        console_handler.setFormatter(logging.Formatter(self.formatter))
        return console_handler

    def pub_logger(self):
        logger = self._create_logger()
        self.mutex.acquire()
        logger.addHandler(self._file_logger())
        logger.addHandler(self._console_logger())
        self.mutex.release()
        return logger


log_pro1 = LoggerProject()
log_pro2 = LoggerProject()
logger1 = log_pro1.pub_logger()
logger2 = log_pro2.pub_logger()
logger1.info('aaa')
logger2.info('aaa')
print('logger1: ', id(logger1))
print('logger2: ', id(logger2))
print('log_pro1: ', id(log_pro1))
print('log_pro2: ', id(log_pro2))



