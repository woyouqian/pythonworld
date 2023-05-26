from Interface.info import print1, print2
from time import sleep


class TestCaserun2(object):

    def test_sample3(self):
        print1()
        print2()
        sleep(2)

    def test_sample4(self):
        assert 6 > self.sample4()

    def sample4(self):
        print('the god is a girl!')
        return 2 + 2

