import logging
import pytest
import allure
from Interface.recordsys import *


class TestBaseFunc5(object):
    '''
    1、登陆管理系统；
    2、按条件查找记录；
    3、更改存在的记录；
    4、显示所有的记录；
    5、退出管理系统；
    '''

    @allure.feature('基础功能测试')
    @allure.title('更改记录1')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_base_op6(self):
        with allure.step(self.__doc__):
            pass
        flag = False    # default without save and exit
        run_system()
        logging.info('登陆ZT管理系统')
        get_msg()
        logging.info('按条件查找记录')
        print('Zard is very popular in china...')
        logging.info('Zard is very popular in japan and china and so on other country...')
        modify_msg()
        logging.info('更改存在的记录')
        print('坂井泉水 is very popular in china...')
        logging.info('坂井泉水 is very popular in japan and china and so on other country...')
        show_msg()
        logging.info('显示所有的记录')
        exit_msg()
        logging.info('退出管理系统')
        assert flag
