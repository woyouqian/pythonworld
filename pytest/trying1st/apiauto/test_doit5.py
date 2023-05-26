from Interface.know import *
import logging
from logging import getLogger
logger = getLogger()


def test_print12():
    logging.info('hello world!')
    logger.error('hello world2!')
    printknow1()


def test_print13():
    num = 14
    logging.info('i am writing logs...')
    logger.info('i am writing logs 2...')
    printknow2()
    assert num == 15


def test_print14():
    logging.warning('i am writing logs now...')
    printknow3()


def test_print15():
    flag = '2 function call'
    printknow1()
    printknow3()
    assert '1 function' in flag

