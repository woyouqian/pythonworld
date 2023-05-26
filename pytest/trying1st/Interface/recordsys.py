def message0():
    print()
    print('------'*6)
    print('====== 欢迎使用ZT管理系统 ======')


def add_msg():
    print('\t1.增加新的记录；')


def get_msg():
    print('\t2.按条件查找记录；')


def modify_msg():
    print('\t3.更改存在的记录；')


def delete_msg():
    print('\t4.按条件删除记录；')


def show_msg():
    print('\t5.显示所有的记录；')


def save_msg():
    print('\t6.保存该记录；')


def exit_msg():
    print('\t7.退出该系统；')
    print('------'*6)


def run_system():
    message0()
    add_msg()
    get_msg()
    modify_msg()
    delete_msg()
    show_msg()
    save_msg()
    exit_msg()


if __name__ == '__main__':
    run_system()
