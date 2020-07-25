# 2.点歌系统可以记录，记事本/或excel形式存放于本地磁盘；
# txt格式作为日志文本，记录相增、删操作；xls格式作为存取data；


import logging
import csv
import xlrd
import xlwt

from time import ctime
from os import getcwd
from os import path


class FileOperate(object):

    @staticmethod
    def file_msg(file_type='txt'):
        """
        file_type只可取值'txt'或'excel'或'csv'，
        默认为txt,生成记事本对象；为excel则生成表格；为csv则生成csv文件.
        :param file_type: 只可取值'txt'或'excel'或'csv'
        :return: 返回相应的文件名，之前是否已存在
        """

        file_path = getcwd()
        if file_type == 'txt':
            file_name = 'recoder.txt'
            file = path.join(file_path, file_name)
            status = path.exists(file)
            if not status:
                f = open(file, 'a')
                f.close()
        elif file_type == 'excel':
            file_name = 'all songs.xls'
            file = path.join(file_path, file_name)
            status = path.exists(file)
            if not status:
                # f = open(file, 'w')
                # f.close()
                pass
        elif file_type == 'csv':
            file_name = 'all songs.csv'
            file = path.join(file_path, file_name)
            status = path.exists(file)
            if not status:
                f = open(file, 'w')
                f.close()
        else:
            logging.warning("file_type只可取值'txt'或'excel'或'csv'...")
            file = None
            status = False
        return file, status

    @staticmethod
    def txt_write(file, msg):
        with open(file, 'a') as f:
            f.write(ctime())
            f.write('\t')
            f.write(msg)
            f.write('\n')

    @staticmethod
    def csv_write(file, msg, func=True):
        # func取True时实现单次写；False时多次写
        if func:
            with open(file, 'w', newline='') as f:
                csv_obj = csv.writer(f)
                csv_obj.writerow(msg)
        else:
            f = open(file, 'w', newline='')
            csv_obj = csv.writer(f)
            csv_obj.writerows(msg)
            f.close()

    @staticmethod
    def csv_read(file):
        data = []
        with open(file, 'r') as f:
            csv_obj = csv.reader(f)
            # 去掉头部标题行
            next(csv_obj)
            for row in csv_obj:
                data.append(row)
        return data

    def create_excel(self, file):
        table = xlwt.Workbook()
        table.add_sheet('all songs', cell_overwrite_ok=True)
        table.add_sheet('备注')
        table.save(file)
        return table

    def xls_write(self, file, msg, name='all songs'):
        table = self.create_excel(file)
        sheet = table.get_sheet(name)
        for i in range(len(msg)):
            row = i
            for j in range(len(msg[i])):
                col = j
                sheet.write(row, col, label=msg[i][j])
        table.save(file)

    @staticmethod
    def xls_read(file, row_or_col=True):
        table = xlrd.open_workbook(file)
        sheets_name = table.sheet_names()
        name = input("enter a sheet name is from %s: " % sheets_name)
        sheet = table.sheet_by_name(name)
        data = []
        if row_or_col:
            for i in range(1, sheet.nrows):
                row_data = sheet.row_values(i)
                data.append(row_data)
        else:
            for j in range(sheet.ncols):
                col_data = sheet.col_values(j)
                data.append(col_data)

        return data


if __name__ == "__main__":
    # msg = ['歌曲名', '歌手', '来源', '分类别', '评价', '备注']
    # msg = [['歌曲名', '歌手', '来源', '分类别', '评价', '备注'],
    #        ['你', '屠洪刚', '百度音乐', '古典', '***', '《孝庄秘史》'],
    #        ['刀剑如梦', '周华健', '酷我音乐', '武侠', '****', '《倚天屠龙记》'],
    #        ['神话情话', '周华健', '酷我音乐', '武侠', '****', '《神雕侠侣》']]
    File = FileOperate()
    print(File.file_msg())
    # file, status = file_msg(file_type='csv')
    # file, status = file_msg(file_type='excel')
    # if file is not None:
        # csv_write(file, msg, func=False)
        # print(csv_read(file))
        # txt_write(file, msg="welcome to home, zhangtao. never give up, go on!")
    # print(file, end='\t')
    # print(status)
    # file = r'C:\Users\HP\Desktop\DoingIt\py2exe_0\orderSystem\all songs.xls'
    # File.create_excel(file)
    # File.xls_write(file, msg)
    # print(File.xls_read(file))

