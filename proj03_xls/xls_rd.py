import xlrd
import xlwt
from xlrd import open_workbook
from xls_do import xlsDoIt
from time import localtime, asctime


def get_sheet_obj():
    # 待分析的excel表格，在电脑存储绝对路径。
    file = "D:\\codefiles\\proj02\\Excel_01.xlsx"
    xls_obj = open_workbook(filename=file)

    all_sheets = xls_obj.sheet_names()
    print(all_sheets)
    do_sheet = input("enter you want to operate sheet: ")
    if do_sheet in all_sheets:
        sheet_obj = xls_obj.sheet_by_name(do_sheet)
        return sheet_obj
    else:
        print("%s not exist!"%do_sheet)


def xls_read(sheet_obj):
    xlsDo = xlsDoIt()
    title_list = sheet_obj.row_values(0)
    print(title_list)
    do_col = input("enter you want to operate column,like 'xxx.xxx': ")
    do_cols = do_col.split('.')
    for col in do_cols:
        if col in title_list:
            index = title_list.index(col)

            col_info = sheet_obj.col_values(index)
            col_info.pop(0)
            print(col_info)
            xlsDo.xls_column_kind(col_info)
        else:
            print("column msg error,please confirm: ")
            print(col)


if __name__=="__main__":
    from io_do import *

    date = asctime(localtime())
    txt_file = open_file()
    write_file(txt_file, info=date)
    write_file(txt_file, info='======'*11)
    close_file(txt_file)

    sheet_obj = get_sheet_obj()
    if sheet_obj is not None:
        xls_read(sheet_obj)

