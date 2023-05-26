# know and use logging module...
import logging
from logging import getLogger
from logging import config

# default level is warning
# reBASIC_FORMAT = "%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s"
reBASIC_FORMAT = "%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(name)s:%(message)s"
logging.basicConfig(format=reBASIC_FORMAT, datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
# logging.basicConfig(filename='.\\rst.txt', format=reBASIC_FORMAT, datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
# logging.Formatter()
logging.debug('hello world! level is debug.')
logging.info('hello world! level is info.')
logging.warning('hello world! level is warn.')
logging.error('hello world! level is error.')
logging.fatal('hello world! level is fatal.')
logging.critical('hello world! level is critical, eq fatal.')

logger = getLogger('this me do')
logger.setLevel(logging.WARNING)

# print(logger.getEffectiveLevel())
logger.debug('hello Python world! level is debug.')
logger.info('hello world2! level is info.')
logger.warning('hello world2! level is warn.')
logger.error('hello world2! level is error.')
logger.fatal('hello world2! level is fatal.')
logger.critical('hello world2! level is critical, eq fatal.')
