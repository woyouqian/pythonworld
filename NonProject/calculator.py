import tkinter as tk
from tkinter.constants import *
from math import fabs


def clear():
    e1.set('')
    minus_data.clear()
    suan_shi.clear()


def back():
    if e1.get() == '':
        minus_data.clear()
        suan_shi.clear()
        pass
    else:
        var_str = e1.get()[:-1]
        if not var_str:
            var_str = ''
        e1.set(var_str)


global minus_data
minus_data = {}
global suan_shi
suan_shi = []
flag = True


def turnoff():
    global flag
    minus_data.clear()
    suan_shi.clear()
    if flag:
        e1.set('')
        flag = False
    else:
        e1.set('0')
        flag = True


def e_deal():
    datas = []
    operator = []
    # msg = e1.get()
    msg = e.get()
    if msg:
        data = ''
        input_list = list(msg)
        for i in input_list:
            if i.isdigit():
                data += i
            else:
                if i != '.':
                    datas.append(data)
                    operator.append(i)
                    data = ''
                else:
                    data += i
        datas.append(data)

    # print(datas)
    # print(operator)
    return datas, operator


def ishas():
    if minus_data and suan_shi:
        msg = e.get()
        if msg:
            if len(suan_shi) == 1:
                obj = str_dealing(suan_shi[0])
                key_name = obj[1]
                resp = suan_shi[0].rstrip(key_name) + minus_data.get(key_name)
                s = str_different(msg, resp)
                resp += s
                req = suan_shi[0] + s
            else:
                todo = []
                done = []
                for i in range(len(suan_shi)):
                    obj = str_dealing(suan_shi[i])
                    done.append(obj)
                    key_name = obj[1]
                    doing = suan_shi[i].rstrip(key_name) + minus_data.get(key_name)
                    todo.append(doing)

                resp = todo[0]
                for j in range(1, len(todo)):
                    resp += todo[j].lstrip(todo[j-1])

                req = suan_shi[0]
                for k in range(1, len(done)):
                    req += done[k][0].lstrip(todo[k-1]) + done[k][1]

                s = str_different(msg, resp)
                resp += s
                req += s
            if resp == msg:
                return True, req
    else:
        req = ''
        return False, req


def str_deal(req):
    datas = []
    operator = []
    if req:
        r = ''
        req_list = list(req)
        for i in req_list:
            if i not in ('+', '-', '*', '/'):
                r += i
            else:
                operator.append(i)
                datas.append(r)
                r = ''
        datas.append(r)

    # print(datas)
    # print(operator)
    return datas, operator


def str_dealing(chars):
    if chars:
        _data = ''
        for i in range(1, len(chars) + 1):
            char = chars[0 - i]
            if char not in ('+', '-', '*', '/'):
                _data += char
            else:
                break

    else:
        return
    var_key = str_reversed(_data)
    other = chars.rstrip(var_key)
    return [other, var_key]


def str_reversed(chars):
    count = len(chars)
    string = ''
    if count != 0:
        for i in range(1, count+1):
            char = chars[count-i]
            string += char
    return string


def str_different(str0, str1):
    result = ''
    z1 = len(str0) - len(str1)
    if z1 > 0:
        for i in range(1, z1+1):
            result += str0[0-i]
        result = str_reversed(result)
    return result


def calculator_run():
    status, req = ishas()
    # print(status)
    # print(req)
    if status and len(req) != 0:
        datas, operator = str_deal(req)
        for key in minus_data.keys():
            # in list, insert is first and delete late.
            place = datas.index(key)
            datas.insert(place, minus_data[key])
            datas.remove(key)
    else:
        datas, operator = e_deal()
    # print(datas)
    # print(operator)

    if datas and operator:
        flag = True
        result = float(datas[0])
        for i in range(len(operator)):
            var = float(datas[i + 1])
            if operator[i] == '+':
                result += var
            elif operator[i] == '-':
                result -= var
            elif operator[i] == '*':
                result *= var
            elif operator[i] == '/':
                if int(var) != 0:
                    result /= var
                else:
                    flag = False
                    break

        if flag:
            e1.set(result)
        else:
            e1.set('ERROR!')
    minus_data.clear()
    suan_shi.clear()


def plus_minus():
    msg = e1.get()
    if msg:
        _data = ''
        for i in range(1, len(msg)+1):
            char = msg[len(msg)-i]
            if char not in ('+', '-', '*', '/'):
                _data += char
            else:
                break

    else:
        return

    medium = str_reversed(_data)
    var_data = float(medium)
    var_data *= -1
    if str(var_data) == msg:
        msg = msg.lstrip('-')
        var_data *= -1

    e_str = msg.rstrip(medium) + str(var_data)
    e1.set(e_str)

    # get plus or minus data here.
    minus = str(var_data)
    var = 'var'
    var += str(len(minus_data))
    minus_data[var] = minus
    middle = e_str.rstrip(minus) + var
    suan_shi.append(middle)


def percent():
    _data = float(e1.get())
    if _data > 0:
        _data *= 100
        e1.set(_data)


def absolute():
    _data = fabs(float(e1.get()))
    e1.set(_data)
    minus_data.clear()
    suan_shi.clear()


root = tk.Tk()
root.title("calculator")
root.maxsize(width=300, height=400)

l_topic = tk.Label(root, text="ZT Calculator", width=50, height=3)
l_topic.pack(side=TOP)

f_entry = tk.Frame(root, relief=SUNKEN, borderwidth=2)
e1 = tk.StringVar()
# tk.Entry(f_entry, width=38, textvariable=e1, justify=RIGHT).pack(side=LEFT, padx=5, pady=6)
e = tk.Entry(f_entry, width=38, textvariable=e1, justify=RIGHT)
e.pack(side=LEFT, padx=5, pady=6)
e1.set('')
f_entry.pack()

set_dict = {'back': back, 'exit': quit, 'clear': clear, 'on/off': turnoff}
f_set = tk.Frame(root, borderwidth=2)
for key in set_dict.keys():
    tk.Button(f_set, text=key, width=8, height=1, command=set_dict[key]).pack(side=LEFT, padx=3, pady=3)
f_set.pack()


def button(frame, info):
    tk.Button(frame, text=info, width=8, height=1, command=lambda: e.insert(END, info)).pack(side=LEFT, padx=3, pady=3)


f0 = tk.Frame(root, borderwidth=2)
for info in [1, 2, 3]:
    button(f0, info)
tk.Button(f0, text='=', width=8, height=1, command=calculator_run).pack(side=LEFT, padx=3, pady=3)
f0.pack()


def frame_button(name_msgs):
    if name_msgs:
        f = tk.Frame(root, borderwidth=2)
        for msg in name_msgs:
            button(f, msg)
        f.pack()
    else:
        pass


frame_button([4, 5, 6, '.'])
frame_button([7, 8, 9, '/'])
frame_button([0, '+', '-', '*'])

often_dict = {'+/-': plus_minus, '%': percent, '|x|': absolute, 'NC': None}
f1 = tk.Frame(root, borderwidth=2)
for key in often_dict.keys():
    tk.Button(f1, text=key, width=8, height=1, command=often_dict[key]).pack(side=LEFT, padx=3, pady=3)
f1.pack()

tk.Label(root, text="飞天名人鸟", width=38, justify=CENTER, font=("楷体", 24)).pack(pady=11)
tk.mainloop()


if __name__ == "__main__":
    pass

