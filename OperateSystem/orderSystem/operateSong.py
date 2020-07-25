# ZT点歌平台
# 1.Python，利用面向对象，面向过程编写；
# 2.点歌系统可以记录，记事本/或excel形式存放于本地磁盘；
# 3.点歌系统实现增、删、改（弱功能）、查、检索（歌曲名、歌手、分类别、随机播放）功能；
# 4.点歌平台也可以从网页上获取歌单；
# 5.对外暴露必要的API接口；
# 6.使用GUI界面实现其功能；
# 7.利用Django框架实现Web/服务器端；
# 8.实现网络编程功能；

# song对象纳括（歌曲名、歌手、来源、分类别、评价1-6*、备注（mark备用字段））


from txtExcelOperate import FileOperate


class OrderSystem(FileOperate):
    """
    3.点歌系统实现增、删、改（弱功能）、查、检索（歌曲名、歌手、分类别、随机播放）功能；
    5.对外暴露必要的API接口；
    """

    def __init__(self):
        self.all_song = []
        self.file_txt = self.file_msg()[0]

    def input_msg(self):
        "song对象纳括（歌曲名、歌手、来源、分类别、评价1-6*、备注（mark备用字段））"
        song = []
        song_name = input("请输入歌曲名字：")
        song_singer = input("请输入歌手名字：")
        song_source = input("请输入歌曲来源：")
        if not song_source:
            song_source = "百度音乐"
        song_kind = input("请输入歌曲分类别（古典、民乐、武侠、流行、其它）：")
        if not song_kind:
            song_kind = "其它"
        song_evaluate = input("请输入对歌曲的评价（1-6 *）：")
        if not song_evaluate:
            song_evaluate = '*'
        song_mark = input("备注备用字段：")
        if not song_mark:
            song_mark = None

        if song_name and song_singer:
            song.append(song_name)
            song.append(song_singer)
            song.append(song_source)
            song.append(song_kind)
            song.append(song_evaluate)
            song.append(song_mark)

        return song

    def edit_msg(self, song):
        new_song = []
        song_name = input("请输入歌曲名字，%s：" % song[0])
        song_singer = input("请输入歌手名字，%s：" % song[1])
        song_source = input("请输入歌曲来源，%s：" % song[2])
        song_kind = input("请输入歌曲分类别（古典、民乐、武侠、流行、其它），%s：" % song[3])
        song_evaluate = input("请输入对歌曲的评价（1-6 *），%s：" % song[4])
        song_mark = input("备注备用字段，%s：" % song[5])
        if not song_name:
            song_name = song[0]

        if not song_singer:
            song_singer = song[1]

        if not song_source:
            song_source = song[2]

        if not song_kind:
            song_kind = song[3]

        if not song_evaluate:
            song_evaluate = song[4]

        if not song_mark:
            song_mark = song[5]

        new_song.append(song_name)
        new_song.append(song_singer)
        new_song.append(song_source)
        new_song.append(song_kind)
        new_song.append(song_evaluate)
        new_song.append(song_mark)

        return new_song

    def add_song(self):
        song = self.input_msg()
        if song:
            self.all_song.append(song)
            msg = "add a new song: %s ..." % str(song)
            self.txt_write(file=self.file_txt, msg=msg)

    def display_all_song(self):
        print('------' * 18)
        if self.all_song:
            print("歌曲名", end='\t\t')
            print("歌手", end='\t\t')
            print("歌曲来源", end='\t\t')
            print("类别", end='\t\t')
            print("评价", end='\t\t')
            print("备注")
            print()
            for song in self.all_song:
                for i in range(len(song)):
                    if i != 5:
                        print(song[i], end='\t\t')
                    else:
                        print(song[i])
        else:
            print("There is no any data, has no song!!!")
        print('------'*18)

    def clear_all_song(self):
        self.all_song.clear()
        msg = "clear all song recoder ..."
        self.txt_write(file=self.file_txt, msg=msg)

    def __search_song(self, keyword, index):
        some_song = []
        if self.all_song:
            for song in self.all_song:
                if keyword in song[index]:
                    some_song.append(song)

        return some_song

    def __display_song(self, some_song):
        if some_song:
            print('******' * 18)
            print("歌曲名", end='\t\t')
            print("歌手", end='\t\t')
            print("歌曲来源", end='\t\t')
            print("类别", end='\t\t')
            print("评价", end='\t\t')
            print("备注")
            print()
            for song in some_song:
                for i in range(len(song)):
                    if i != 5:
                        print(song[i], end='\t\t')
                    else:
                        print(song[i])
            print('******' * 18)
        else:
            print("There is no any data, has no song!!!")

    def search_by_name(self, name):
        index = 0
        some_song = self.__search_song(name, index)
        self.__display_song(some_song)
        return some_song

    def search_by_singer(self, singer):
        index = 1
        some_song = self.__search_song(singer, index)
        self.__display_song(some_song)
        return some_song

    def search_by_kind(self, kind):
        index = 3
        some_song = self.__search_song(kind, index)
        self.__display_song(some_song)
        return some_song

    def __delete_song(self, some_song):
        if some_song:
            for song in some_song:
                self.all_song.remove(song)
                msg = "delete a song: %s ..." % str(song)
                self.txt_write(file=self.file_txt, msg=msg)

    def delete_by_name(self, name):
        some_song = (self.search_by_name(name))
        self.__delete_song(some_song)

    def delete_by_singer(self, singer):
        some_song = (self.search_by_singer(singer))
        self.__delete_song(some_song)

    def delete_by_kind(self, kind):
        some_song = (self.search_by_kind(kind))
        self.__delete_song(some_song)

    def __change_song(self, some_song):
        if some_song:
            for song in some_song:
                index = self.all_song.index(song)
                new_song = self.edit_msg(song)

                self.all_song.insert(index, new_song)
                self.all_song.remove(song)
                msg = "edit song: %s become to %s ..." % (str(song), str(new_song))
                self.txt_write(file=self.file_txt, msg=msg)

    def change_by_name(self, name):
        some_song = self.search_by_name(name)
        self.__change_song(some_song)

    def change_by_singer(self, singer):
        some_song = self.search_by_singer(singer)
        self.__change_song(some_song)


if __name__ == '__main__':
    System = OrderSystem()
    # print(System.all_song)
    # System.add_song()
    # System.add_song()
    # System.add_song()
    # System.display_all_song()
    # System.search_by_name('你')
    # System.search_by_singer("周华健")
    # System.delete_by_name('你')
    # System.display_all_song()
    # System.change_by_name("神话情话")
    # System.display_all_song()
    print(dir(System))

