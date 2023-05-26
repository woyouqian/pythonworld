def message0():
    print()
    print('------'*6)
    print('====== 欢迎使用ZT管理系统 ======')


def message1():
    print('\t1.增加新的记录；')


def message2():
    print('\t2.按条件查找记录；')


def message3():
    print('\t3.更改存在的记录；')


def message4():
    print('\t4.按条件删除记录；')


def message5():
    print('\t5.显示所有的记录；')


def message6():
    print('\t6.保存记录；')


def message7():
    print('\t7.退出该系统；')
    print('------'*6)


def run_system():
    message0()
    message1()
    message2()
    message3()
    message4()
    message5()
    message6()
    message7()


if __name__ == '__main__':
    run_system()
