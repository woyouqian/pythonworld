'''
------------------------------------
====== 欢迎使用ZT管理系统 ======
	1.增加新的记录；
	2.按条件查找记录；
	3.更改存在的记录；
	4.按条件删除记录；
	5.显示所有的记录；
	6.保存该记录；
	7.退出该系统；
------------------------------------
'''

import logging
import pytest
import allure
from Interface.recordsys import *


# @pytest.mark.usefixtures('fixture_start')
class TestBaseFunc1(object):

    @allure.feature('基础功能测试')
    @allure.title('登陆ZT管理系统')
    @allure.step('登陆管理系统')
    @pytest.mark.usefixtures('fixture_start')
    def test_base_op1(self):
        run_system()
        logging.info('登陆ZT管理系统')

    @allure.feature('基础功能测试')
    @allure.title('退出管理系统')
    @allure.step('退出管理系统')
    def test_base_op2(self):
        exit_msg()
        logging.info('退出管理系统')
