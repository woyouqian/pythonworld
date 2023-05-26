from Interface.info import define_name, run, print1
from time import sleep


class TestCaserun1(object):

    def test_sample1(self):
        run()
        define_name()
        sleep(2)

    def test_sample2(self):
        print1()

