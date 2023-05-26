import pytest

from Interface.message import *
from time import sleep


class TestCaserun3(object):

    @pytest.mark.skip()
    def test_sample5(self):
        message0()
        message1()
        message2()
        message3()
        message4()
        message5()
        message6()
        message7()
        sleep(3)

    def test_sample6(self):
        self.test_sample5()

