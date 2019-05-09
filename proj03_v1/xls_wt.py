import xlwt
from xls_rd import get_sheet_obj
from os import path
from io_do import *
from xlwt import Workbook
from xlwt import Worksheet

def xls_column(kind_str):
    column_str_list = kind_str.split('\n')
    if not column_str_list[-1]:
        column_str_list.pop()
    return column_str_list


def xls_wt(row, info):
    file_path = path.abspath('xls_rd.py').strip('xls_rd.py')
    file_name = "result.xls"
    file = file_path + file_name
    xls_obj = Workbook(encoding='utf-8')
    sheet_obj = xls_obj.add_sheet('Sheet1')
    for k in range(len(info)):
        sheet_obj.write(row, k, info[k])
    xls_obj.save(file)


def list_sum(goal_rows, count):
    resp_list = []
    for i in range(count):
        result = 0.0
        for row_vaule in goal_rows:
            result += float(row_vaule[i])
        resp_list.append(str(result))
    # print(resp_list)
    return resp_list


def excel_read(sheet_obj, goal_list):
    col_count = sheet_obj.ncols-1
    col_zero = sheet_obj.col_values(0)

    txt_file = open_file()
    file_path = path.abspath('xls_rd.py').strip('xls_rd.py')
    file_name = "result.xls"
    file = file_path + file_name
    xls_obj = Workbook(encoding='utf-8')
    xls_sheet = xls_obj.add_sheet('Sheet1')
    row = 0

    for goal in goal_list:
        goal_rows = []
        for j in range(1,len(col_zero)):
            if goal in col_zero[j]:
                row_vaule = sheet_obj.row_values(j)
                goal = row_vaule.pop(0)
                # 目标返回为二维list类型。
                goal_rows.append(row_vaule)
        if goal_rows:
            resp_list = list_sum(goal_rows, col_count)
            resp_list.insert(0, goal)
            print(resp_list)
            # 写入txt文本。
            info1 = ''
            for str1 in resp_list:
                info1 += str1+'      '
            write_file(txt_file, info1)
            # 写入excel表格。
            for k in range(len(resp_list)):
                xls_sheet.write(row, k, resp_list[k])
            row += 1
    xls_obj.save(file)
    write_file(txt_file, info='-----'*20)
    write_file(txt_file)
    close_file(txt_file)


if __name__ == "__main__":
    from time import localtime, asctime

    # 可用于在excel表格中进行按条件筛选/去重（同一对象的各列值累加求和，除去第一列），并记录到新的excel中。
    date = asctime(localtime())
    txt_file = open_file()
    write_file(txt_file, info=date)
    write_file(txt_file, info='======' * 11)
    close_file(txt_file)

    kind_str ="""jack
nike
lily
"""
    goal_list = xls_column(kind_str)
    sheet_obj = get_sheet_obj()
    if sheet_obj is not None:
        excel_read(sheet_obj, goal_list)
    # xls_wt(1, ['jack','nike','lily'])

