# know and use logging module 2...
import logging
from logging import getLogger
from logging import config

# default level is warning
# 全局配置和handler处理器配置，只存其一即可！
# 使用logging.basicConfig全局配置时，终端显示和文件保存只能选其一，不能同时共存。
# 日志器与handler处理器同时设置level，以logger为准！
# 日志器无绑定handler时，以全局配置为准！


# 1.create logger
logger1 = getLogger('the 1st logger')
logger1.setLevel('INFO')
logger2 = getLogger('the 2nd logger')
logger2.setLevel(logging.WARNING)

# 2.create handler cpu and format
fh = logging.FileHandler('.\\rst.txt')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

reBASIC_FORMAT = "%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(name)s:%(message)s"
fmt = logging.Formatter(fmt=reBASIC_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(fmt=fmt)
ch.setFormatter(fmt=fmt)

# 3.add handler to logger
# logger1.addHandler(fh)
# logger1.addHandler(ch)
logger2.addHandler(fh)
logger2.addHandler(ch)

logger1.debug('hello world! level is debug.')
logger1.info('hello world! level is info.')
logger1.warning('hello world! level is warn.')
logger1.error('hello world! level is error.')
logger1.fatal('hello world! level is fatal.')
logger1.critical('hello world! level is critical, eq fatal.')

logger2.debug('hello Python world! level is debug.')
logger2.info('hello world2! level is info.')
logger2.warning('hello world2! level is warn.')
logger2.error('hello world2! level is error.')
logger2.fatal('hello world2! level is fatal.')
logger2.critical('hello world2! level is critical, eq fatal.')
