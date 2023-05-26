import pytest
from Interface.info import *
from Interface.know import *
from time import sleep


def test_print10():
    print1()
    print2()


class TestCaserun5(object):

    @pytest.mark.run(order=1)
    def test_print8(self):
        run()
        print1()

    @pytest.mark.run(order=2)
    def test_print9(self):
        define_name()
        print2()

    def test_print11(self):
        sleep(2)
        printknow1()
        printknow2()
        printknow3()


if __name__ == '__main__':
    pytest.main(['-vs'])

