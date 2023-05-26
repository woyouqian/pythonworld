'''

def func1():
    "function: output hello world!"
    print('hello world!')


class printfmsg(object):
    """
    function: 1.print hello world!
            2.print welcome to Python world!
            3.print welcome to Linux world!
            4.print welcome to Windows world!
    """

    def printf1(self):
        print(self.__doc__)

    @staticmethod
    def printf2():
        print('hello world!')
        print('welcome to Python world!')
        print('welcome to Linux world!')
        print('welcome to Windows world!')


# help(func1)
# print(dir(func1))
print(func1.__doc__)
func1()
print('------'*11)
print(printfmsg.__doc__)
# print(printfmsg.printf2())
msg = printfmsg()
msg.printf1()
msg.printf2()
# print(__file__)
'''
import pytest
import yaml
import configparser


# built-in fixture
def test_builtin_fixture1(recwarn, request, testdir):
    pass
    request
    testdir
    pytest.FixtureRequest
    pytest.Testdir
    pytest.MonkeyPatch
