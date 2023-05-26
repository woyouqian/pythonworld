import logging
import pytest
import allure
from Interface.recordsys import *


class TestBaseFunc2(object):

    @allure.feature('基础功能测试')
    @allure.title('增加新的记录1')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('fixture_start')
    def test_base_op3(self):
        with allure.step('登陆管理系统'):
            run_system()
            logging.info('登陆ZT管理系统')
        with allure.step('增加新的记录'):
            add_msg()
            logging.info('增加新的记录')
        with allure.step('显示所有的记录'):
            show_msg()
            logging.info('显示所有的记录')
        with allure.step('不保存退出管理系统'):
            exit_msg()
            logging.info('不保存退出管理系统')
            assert False
