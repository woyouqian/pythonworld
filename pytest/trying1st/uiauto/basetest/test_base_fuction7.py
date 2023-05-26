import logging
import pytest
import allure
from Interface.recordsys import *


class TestBaseFunc7(object):
    '''
    1、登陆管理系统；
    2、按条件查找记录；
    3、按条件删除记录；
    4、显示所有的记录；
    5、退出管理系统；
    '''

    def setup_class(self):
        print('------ 准备环境，即将开始登陆系统测试 ------')
        logging.info('一切已准备就位，开始测试')

    @allure.feature('基础功能测试')
    @allure.title('删除记录1')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_base_op8(self):
        with allure.step(self.__doc__):
            pass
        flag = False    # default without save and exit
        run_system()
        logging.info('登陆ZT管理系统')
        get_msg()
        logging.info('按条件查找记录')
        print('Zard is very popular in china...')
        # logging.info('Zard is very popular in japan and china and so on other country...')
        delete_msg()
        logging.info('删除存在的记录')
        # print('坂井泉水 is very popular in china...')
        # logging.info('坂井泉水 is very popular in japan and china and so on other country...')
        show_msg()
        logging.info('显示所有的记录')
        logging.warning('删除该记录失败--Zard')
        exit_msg()
        logging.info('退出管理系统')
        assert flag

    def teardown_class(self):
        print('------ 测试结束，开始清除数据并恢复环境 ------')
        logging.info('测试结束，清除数据并恢复环境')
