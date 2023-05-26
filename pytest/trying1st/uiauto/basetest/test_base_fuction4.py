import logging
import pytest
import allure
from Interface.recordsys import *


class TestBaseFunc4(object):
    '''
    1、登陆管理系统
    2、按条件查找记录
    3、退出管理系统
    '''

    @allure.feature('基础功能测试')
    @allure.title('按条件查找记录')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures('fixture_start')
    # @pytest.fixture(scope='function', params=['Zard'])
    def test_base_op5(self):
        with allure.step(self.__doc__):
            pass
        run_system()
        logging.info('登陆ZT管理系统')
        get_msg()
        logging.info('按条件查找记录')
        print('Zard is very popular in china...')
        logging.info('Zard is very popular in japan and china and so on other country...')
        exit_msg()
        logging.info('退出管理系统')
