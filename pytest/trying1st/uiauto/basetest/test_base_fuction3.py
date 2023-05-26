import logging
import pytest
import allure
from Interface.recordsys import *


class TestBaseFunc3(object):
    '''
    1、登陆管理系统
    2、增加新的记录
    3、显示所有的记录
    4、保存该记录
    5、退出管理系统
    '''

    @allure.feature('基础功能测试')
    @allure.title('增加新的记录2')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('fixture_start')
    def test_base_op4(self):
        with allure.step(self.__doc__):
            run_system()
            logging.info('登陆ZT管理系统')
            add_msg()
            logging.info('增加新的记录')
            show_msg()
            logging.info('显示所有的记录')
            save_msg()
            logging.info('保存该记录')
            exit_msg()
            logging.info('退出管理系统')
