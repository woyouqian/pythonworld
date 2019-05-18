from xls_rd import get_sheet_obj


"""
def h(f):
    print("hello Python world!")
    print('------'*20)
    f()
    print("i am coming!")

# @h
def f():
    print("my name is zhanghengtao.")
    print("******"*20)

# h(f)


class g(object):

    def __init__(self):
        print("人生苦短，我只用Python！")

    @classmethod
    def h(cls):
        print("hello Python world!")
        print('------' * 20)
        print("i am coming!")

    # @classmethod
    @staticmethod
    def f():
        print("my name is zhanghengtao.")
        print("******" * 20)


g.h()
g.f()
z = g()
z.h()
z.f()
"""

def xls_column(column_str_list, flag=True):
    count = 0.0
    for i in range(len(column_str_list)):
        if column_str_list[i]:
            count += float(column_str_list[i])
    print("total is: ")
    print(count)
    if not flag:
        print("arg is: ")
        print(count / len(column_str_list))


def xls_sum(sheet_obj):
    title_list = sheet_obj.row_values(0)
    print(title_list)
    do_col = input("enter you want to operate column,like 'xxx.xxx': ")
    do_cols = do_col.split('.')
    for col in do_cols:
        if col in title_list:
            index = title_list.index(col)

            col_info = sheet_obj.col_values(index)
            col_info.pop(0)
            # print(col_info)
            print(col, end=' ')
            # flag为True求和，为False求平均。
            xls_column(col_info, flag=False)
        else:
            print("column msg error,please confirm: ")
            print(col)


if __name__ == "__main__":
    # 对excel表格中指定列项求和（除去为标题的第一行），int/float型；flag为True求和，为False求平均。
    sheet_obj = get_sheet_obj()
    if sheet_obj is not None:
        xls_sum(sheet_obj)



