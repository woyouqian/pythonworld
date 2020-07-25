from sys import exit
from operateSong import OrderSystem


def run():
    display = '''========== 欢迎使用ZT点播歌曲平台 ==========
           0.清除所有歌曲；
           1.显示所有歌曲；
           2.新增歌曲信息；
           3.以歌曲名查找；
           4.以歌手名查找；
           5.以分类别查找；
           6.以歌曲名删除；
           7.以歌手名删除；
           8.以分类别删除；
           9.以歌曲名编辑；
           10.以歌手名编辑；
           11.excel格式保存；
           12.csv格式备份；
           13.退出系统；
===========================================
'''

    System = OrderSystem()
    # 同步本地歌曲资源数据
    file_xls, status = System.file_msg(file_type='excel')
    if status:
        System.all_song = System.xls_read(file_xls)
    file_csv, status = System.file_msg(file_type='csv')
    # if status:
    #     System.all_song = System.csv_read(file_csv)

    while True:
        print(display)
        num = input("请输入0-11中的某个值：")
        if num == '0':
            System.clear_all_song()
        elif num == '1':
            System.display_all_song()
        elif num == '2':
            System.add_song()
        elif num == '3':
            name = input("请输入歌曲名：")
            if name:
                System.search_by_name(name)
        elif num == '4':
            singer = input("请输入歌手名；")
            if singer:
                System.search_by_singer(singer)
        elif num == '5':
            kind = input("请输入分类别；")
            if kind:
                System.search_by_kind(kind)
        elif num == '6':
            name = input("请输入歌曲名：")
            if name:
                System.delete_by_name(name)
        elif num == '7':
            singer = input("请输入歌手名；")
            if singer:
                System.delete_by_singer(singer)
        elif num == '8':
            kind = input("请输入分类别；")
            if kind:
                System.delete_by_kind(kind)
        elif num == '9':
            name = input("请输入歌曲名：")
            if name:
                System.change_by_name(name)
        elif num == '10':
            singer = input("请输入歌手名；")
            if singer:
                System.change_by_singer(singer)
        elif num == '11':
            title = ['歌曲名', '歌手', '来源', '分类别', '评价', '备注']
            System.all_song.insert(0, title)
            System.xls_write(file_xls, msg=System.all_song)
            msg = "save all songs data as Excel..."
            System.txt_write(file=System.file_txt, msg=msg)
        elif num == '12':
            title = ['歌曲名', '歌手', '来源', '分类别', '评价', '备注']
            System.all_song.insert(0, title)
            System.csv_write(file_csv, msg=System.all_song, func=False)
            msg = "backup all songs data as CSV..."
            System.txt_write(file=System.file_txt, msg=msg)
        elif num == '13':
            print('GoodBye!!!')
            exit()
        else:
            pass


if __name__ == '__main__':
    run()

