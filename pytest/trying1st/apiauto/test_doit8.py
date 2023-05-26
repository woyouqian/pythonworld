import pytest
import allure
import logging
# from Interface.info import *
from Interface.know import *
from Interface.message import *


class Testcaserun8(object):

    def setup_class(self):
        print('------ 一切准备就位，开始测试ZT管理系统 ------')
        logging.critical('------ 一切准备就位，开始测试ZT管理系统 ------')

    def teardown_class(self):
        print('------ 基本测试结束，清除数据恢复环境 ------')
        logging.fatal('------ 测试结束，清除数据恢复环境 ------')

    def test_run(self):
        with allure.step('登陆系统'):
            print()
            message0()
            message1()
            message2()
            message3()
            message4()
            message5()
            message6()
            message7()
            print()
            logging.info('欢迎使用ZT管理系统')

    def test_add(self):
        with allure.step('增加记录'):
            message1()
            logging.info('1.增加新的记录；')

    def test_search(self):
        with allure.step('查找记录'):
            message2()
            logging.info('2.按条件查找记录；')

    def test_modify(self):
        with allure.step('编辑记录'):
            message3()
            logging.info('3.更改存在的记录；')

    @allure.step('查看记录')
    def test_display(self):
        message5()
        logging.info('5.显示所有的记录；')

    @pytest.mark.run(5)
    def test_delete(self):
        with allure.step('删除记录'):
            message4()
            logging.info('4.按条件删除记录；')
        assert 0 > 1

    @allure.step('保存记录')
    def test_save(self):
        message6()
        logging.info('6.保存记录；')
