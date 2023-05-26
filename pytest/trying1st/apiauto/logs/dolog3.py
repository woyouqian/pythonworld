import logging
import colorlog     # 继承logging module
from logging import getLogger
from logging import config


# 以下为项目级配置，采用配置文件方式
# 需要时搜索复制调试
# config.dictConfig()
# config.fileConfig()

# 1.create logger
logger3 = getLogger()
# logger3 = colorlog.getLogger()
logger3.setLevel(logging.INFO)

# 2.create handler cpu and format
fh = logging.FileHandler('.\\rst.txt')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
# ch = colorlog.StreamHandler()
ch.setLevel(logging.INFO)

reBASIC_FORMAT = "%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s"
# 配置日志颜色打印！
reBASIC_FORMAT2 = "%(log_color)s%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s"
fmt = logging.Formatter(fmt=reBASIC_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
colorfmt = colorlog.ColoredFormatter(fmt=reBASIC_FORMAT2, datefmt='%Y-%m-%d %H:%M:%S',
                                     log_colors=colorlog.default_log_colors)
fh.setFormatter(fmt=fmt)
ch.setFormatter(fmt=colorfmt)
# print(colorlog.default_log_colors)

# 3.add handler to logger
logger3.addHandler(fh)
logger3.addHandler(ch)

logger3.debug('hello Python world! level is debug.')
logger3.info('hello world 66! level is info.')
logger3.info('hello world 66! level is info.')
logger3.info('hello world 66! level is info.')
logger3.info('hello world 66! level is info.')
logger3.info('hello world 66! level is info.')
logger3.info('hello world 66! level is info.')
logger3.warning('hello world 66! level is warn.')
logger3.error('hello world 66! level is error.')
logger3.fatal('hello world 66! level is fatal.')
logger3.critical('hello world 66! level is critical, is eq fatal.')
