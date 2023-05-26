import pytest


def define_name():
    print("my name is pytest, used in IT auto-test!")
    print("student name is ZHT.")


def run():
    print('welcome to back here!')
    print('you could know and learn pytest tool again.')


def print1():
    print('hello world!')
    print('pytest version:  ', end='')
    print(pytest.__version__)


def print2():
    print('就是这么的丝滑顺六 ', end='')
    print(3+3, end=' !')


if __name__ == '__main__':
    run()
    define_name()
    print1()
    print2()
