import pytest
import logging
from uiauto.producttest.param_parser import yamlf, yaml_parser


@pytest.fixture(scope='class')
def fixture_start():
    print('------ 准备环境，即将开始登陆系统测试 ------')
    logging.info('一切已准备就位，开始测试')
    yield
    print('------ 测试结束，开始清除数据并恢复环境 ------')
    logging.info('测试结束，清除数据并恢复环境')


life = {
          "life": [
            {
              "name": "平凡的世界",
              "author": "路遥"
            },
            {
              "name": "人生",
              "author": "路遥"
            },
            {
              "name": "第七天",
              "author": "余华"
            }
          ]
        }


@pytest.fixture(scope='class')
def env_fixture():
    print('------ 准备环境，即将开始登陆系统测试 ------')
    logging.info('一切已准备就位，开始测试')
    yield life
    print('------ 测试结束，开始清除数据并恢复环境 ------')
    logging.info('测试结束，清除数据并恢复环境')
