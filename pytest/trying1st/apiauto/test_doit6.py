import logging
from Interface.know import *


def test_print16():
    msg = '''
            # 全局配置和handler处理器配置，只存其一即可！
            # 使用logging.basicConfig全局配置时，终端显示和文件保存只能选其一，不能同时共存。
            # 日志器与handler处理器同时设置level，以logger为准！
            # 日志器无绑定handler时，以全局配置为准！
            '''
    logging.fatal(msg)
    print(msg)


class Testcaserun6(object):

    def test_print17(self):
        logging.info('this is 1th point of me...')
        printknow1()

    def test_print18(self):
        logging.info('this is 2nd point of me...')
        printknow2()

    def test_print19(self):
        logging.info('this is 3rd point of me...')
        printknow3()

