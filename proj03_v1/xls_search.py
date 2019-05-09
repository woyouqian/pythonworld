import xlrd
import xlwt
from xlrd import open_workbook
from os import path
from xlwt import Workbook
from xlwt import Worksheet


def get_sheet_obj(file):
    xls_obj = open_workbook(filename=file)
    all_sheets = xls_obj.sheet_names()
    print(all_sheets)
    do_sheet = input("enter you want to operate sheet: ")
    if do_sheet in all_sheets:
        sheet_obj = xls_obj.sheet_by_name(do_sheet)
        return sheet_obj
    else:
        print("%s not exist!"%do_sheet)


def get_col_value0(sheet_obj):
    col_zero = sheet_obj.col_values(0)
    col_zero.pop(0)
    return col_zero


def excel_search(sheet_obj, goal_list):
    col_count = sheet_obj.ncols
    col_zero = sheet_obj.col_values(0)

    file_path = path.abspath('xls_search.py').strip('xls_search.py')
    file_name = "result.xls"
    file = file_path + file_name
    xls_obj = Workbook(encoding='utf-8')
    xls_sheet = xls_obj.add_sheet('Sheet1')

    for i in range(len(goal_list)):
        flag = False
        for j in range(1,len(col_zero)):
            if goal_list[i] in col_zero[j]:
                flag = True
                row_vaule = sheet_obj.row_values(j)
                print(row_vaule)
                # 写入excel表格。
                for k in range(col_count):
                    xls_sheet.write(i, k, row_vaule[k])
        if flag==False:
            print("there is no find %s."%goal_list[i])
            xls_sheet.write(i, 0, goal_list[i])
    xls_obj.save(file)
    

if __name__ == "__main__":
    # 可用于在excel表格中进行按条件筛选（使用唯一身份ID筛选，放置第一列，会自动除去首列），并记录到新的excel中。
    # file1为库excel表格路径；file2为待确认信息表格路径；绝对路径。
    file1 = "D:\\codefiles\\proj02\\Excel_01.xlsx"
    file2 = "D:\\codefiles\\proj02\\Excel_01.xlsx"
 
    sheet_obj1 = get_sheet_obj(file1)
    sheet_obj2 = get_sheet_obj(file2)
    goal_list = get_col_value0(sheet_obj2)
    # print(goal_list)
    if sheet_obj1 is not None:
        excel_search(sheet_obj1, goal_list)
    
