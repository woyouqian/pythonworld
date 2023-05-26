import pytest
import logging
# from Interface.info import *
from Interface.know import *
from Interface.message import *


class Testcaserun7(object):

    def setup_class(self):
        print('------ 一切准备就位，开始测试ZT管理系统 ------')
        logging.critical('------ 一切准备就位，开始测试ZT管理系统 ------')
        logging.fatal('------ 一切准备就位，开始测试ZT管理系统 ------')

    def teardown_class(self):
        print('------ 基本测试结束，清除数据恢复环境 ------')
        logging.fatal('------ 基本测试结束，清除数据恢复环境 ------')
        logging.critical('------ 基本测试结束，清除数据恢复环境 ------')

    def test_run(self):
        run_system()
        logging.info('欢迎使用ZT管理系统')

    def test_add(self):
        message1()
        logging.info('1.增加新的记录；')

    def test_search(self):
        message2()
        logging.info('2.按条件查找记录；')

    def test_modify(self):
        message3()
        logging.info('3.更改存在的记录；')

    def test_display(self):
        message5()
        logging.info('5.显示所有的记录；')

    @pytest.mark.run(5)
    def test_delete(self):
        message4()
        logging.info('4.按条件删除记录；')

    def test_save(self):
        message6()
        logging.info('6.保存记录；')
