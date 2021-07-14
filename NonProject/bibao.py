# 理解Python的闭包与装饰器.
# 1.函数的嵌套调用；
def func0():
    print('-----------> func0')
    print('hi, my name is zhanghengtao. and you?')


def func1(name='zhangmin'):
    func0()
    print('-----------> func1')
    print(name)


def func2(name='youqian'):
    print('-----------> func2')
    print(name, end='\t')
    print(29, end='\t')
    print('woman')


def func3(name='zhaoliying'):
    # name = 'zhaoliying'
    print('-----------> func3')
    func2(name)
    print('****** hello world! ******')

# func0()
# func1()
# print(func0)
# print(func1)
# func2()
# func3()

# 2.函数的嵌套定义：闭包，装饰器；
# 闭包：在函数内部定义函数；内部调用外部的变量值；并返回内部函数。有严格闭包与非严格区分。
def f1():
    work = '日本 Zard 乐队主唱手'
    print('****** hello world! ******')
    def f0():
        print('坂井泉水')
        print('女')
        print(39)
        print(work)
    return f0


def f2():
    # work = '日本 Zard 乐队主唱手'
    print('****** hello world! ******')
    def f0():
        print('坂井泉水')
        print('女')
        print(39)
        # print(work)
    return f0


# f = f1()
# f()
# print(f)
# f = f2()
# f()

# 装饰器：入参必须是函数；具有闭包的特性。
# 入参函数有带参，不带参区别；装饰器也有带参与不带参区分；还有多层装饰器。
def g0():
    print("****** hello wold! ******")
    print('坂井泉水')


# g0函数已经定义使用，现在需要拓展其功能；重新定义或加入新函数调用，都可以实现。
# 但是需修改涉及原代码。
def g1():
    g0()
    print(39)
    print('女')
    print('日本 Zard 乐队主唱手')


# g0()
# g1()
# print(g0)
# print(g1)


def decorate(func):
    # song = "today is another day，敞开心扉，不要认输"
    print('--------- start 1 ---------')

    def wrapper():
        func()
        print(39)
        print('女')
        print('日本 Zard 乐队主唱手')
        # print(song)

    print('--------- end 1 ---------')
    return wrapper


def decorate1(func):
    print('--------- start 2 ---------')

    def wrapper():
        func()
        print("today is another day，敞开心扉，不要认输")
        print("https://www.baidu.com")
        print("https://baike.baidu.com/item/%E5%9D%82%E4%BA%95%E6%B3%89%E6%B0%B4/3482174?fr=aladdin")

    print('--------- end 2 ---------')
    return wrapper


@decorate1
@decorate
def h0():
    print("****** hello wold! ******")
    print('坂井泉水')


# h0()
# print(h0)


def decorate2(func):
    # song = "today is another day，敞开心扉，不要认输"

    def wrapper(msg):
        func(msg)
        print(39)
        print('女')
        print('日本 Zard 乐队主唱手')
        print("today is another day，敞开心扉，不要认输")

    return wrapper


@decorate2
def h1(msg):
    print("****** hello wold! ******")
    print('坂井泉水')
    print(msg)


# print(h1)
# h1('====== 基本信息 ======')
# h1('https://www.baidu.com')


def decorate3(msg):    # 带参数装饰器：第一层入参。
    def output(func):
        def wrapper():
            func()
            print(39)
            print('女')
            print('日本 Zard 乐队主唱手')
            print(msg)
        return wrapper
    return output


msg = "today is another day，敞开心扉，不要认输"


@decorate3(msg)
def y():
    print("****** hello wold! ******")
    print('坂井泉水')


y()
print(y)

