from io_do import *


class xlsDoIt(object):
    """
    1.xls_row方法对excel表格中某行求和或求平均运算，int/float型；flag为True求和，为False求平均；
    2.xls_column方法对excel表格中某行求和或求平均运算，int/float型；flag为True求和，为False求平均；
    3.xls_column_kind方法对excel表格中某列分析，得出包含哪些类，各类占比，str型；
    """

    def xls_row(self, row_str, flag=True):
        row_str_list = row_str.split('\t')
        count = 0.0
        for i in range(len(row_str_list)):
            count += float(row_str_list[i])
        print("total is: ")
        print(count)
        if not flag:
            print("arg is: ")
            print(count/len(row_str_list))

    def xls_column(self, column_str, flag=True):
        column_str_list = column_str.split('\n')
        count = 0.0
        for i in range(len(column_str_list)):
            if column_str_list[i]:
                count += float(column_str_list[i])
        print("total is: ")
        print(count)
        if not flag:
            print("arg is: ")
            print(count/len(column_str_list))

    def xls_column_kind(self, kind_str):
        # 入参为str类型时。
        if type(kind_str)==type('me'):
            column_str_list = kind_str.split('\n')
            if not column_str_list[-1]:
                column_str_list.pop()
        elif type(kind_str)==type(['me']):
            # 入参为list类型时。
            column_str_list = kind_str

        column_str_set = set(column_str_list)
        total = len(column_str_list)
        info1 = "total is: "+str(total)
        print(info1)
        txt_file = open_file()
        write_file(txt_file, info=info1)
        for i in range(len(column_str_set)):
            kind = column_str_set.pop()
            count = column_str_list.count(kind)
            occupy = 100*count/total
            info2 = "{kind} count is: {count}   {occupy}%".format(kind=kind, count=count, occupy=occupy)
            print(info2)
            write_file(txt_file, info=info2)

        write_file(txt_file, info='------'*11)
        write_file(txt_file)
        close_file(txt_file)


if __name__ == "__main__":
    # 此处给变量赋值row_str，column_str，kind_str.
#     row_str = "1	2	3	3.3	6.9"
#     column_str = '''1
# 2
# 4
# 5.1
# 6.6'''
    kind_str = ["nike","nike","lily","lining","nike","lining"]

    xlsDo = xlsDoIt()
    # xlsDo.xls_row(row_str, flag=False)
    # xlsDo.xls_column(column_str, flag=False)
    xlsDo.xls_column_kind(kind_str)


