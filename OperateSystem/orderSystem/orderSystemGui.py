# 6.使用GUI界面实现其功能；尝试个复杂的界面实现
# song对象纳括（歌曲名、歌手、来源、分类别、评价1-6*、备注（mark备用字段））


import tkinter as tk

from tkinter.constants import *


root = tk.Tk()
root.maxsize(width=650, height=600)
root.title("ZT order system")

l_topic = tk.Label(root, text="ZT歌曲点播平台", width=100, height=3, justify=CENTER, font=("楷体", 24))
l_topic.pack(side=TOP)

f_input = tk.Frame(root, relief=SOLID, borderwidth=2, background='green')
tk.Label(f_input, text="检索区", width=20, height=1).pack(side=LEFT, padx=5, pady=5)
e1 = tk.StringVar()
e1.set("歌曲名、歌手、类别")
e_input = tk.Entry(f_input, textvariable=e1, width=550, justify=LEFT)
e_input.pack(side=LEFT, pady=25)
f_input.pack()


def frame_button(f, name, order):
    tk.Button(f, text=name, relief=RAISED, width=12, height=1, command=order).pack(side=LEFT, padx=5, pady=15)


func_dict = {"显示": None, "歌曲名": None, "歌手": None, "类别": None, "新增": None, "删除": None}
f_func = tk.Frame(root, borderwidth=2)
for key in func_dict.keys():
    frame_button(f=f_func, name=key, order=func_dict[key])
f_func.pack()

play_dict = {"随机播放": None, "顺序播放": None, "播放": None, "暂停": None, "上一首": None, "下一首": None}
f_play = tk.Frame(root, borderwidth=2)
for key in play_dict.keys():
    frame_button(f=f_play, name=key, order=play_dict[key])
f_play.pack()

f_music = tk.Frame(root, borderwidth=3, background='green', height=5)
tk.Label(f_music, text="歌曲播放控制区", width=100, height=3, justify=CENTER, font=("楷体", 16)).pack(side=TOP)
f_music.pack(pady=10)

f_display = tk.Frame(root, borderwidth=2)
t_display = tk.Text(f_display, width=250, height=7)
t_display.pack(side=LEFT, padx=15, pady=20)
f_display.pack()

f_exit = tk.Frame(root, borderwidth=2)
tk.Button(root, text='clear', width=12, height=1, command=None).pack(side=LEFT, padx=100, pady=10)
tk.Button(root, text='exit', width=12, height=1, command=root.quit).pack(side=LEFT, padx=100, pady=10)
f_exit.pack()

root.mainloop()

