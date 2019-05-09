def h(f):
    print("hello Python world!")
    print('------'*20)
    f()
    print("i am coming!")

# @h
def f():
    print("my name is zhanghengtao.")
    print("******"*20)

# h(f)


class g(object):

    def __init__(self):
        print("人生苦短，我只用Python！")

    @classmethod
    def h(cls):
        print("hello Python world!")
        print('------' * 20)
        print("i am coming!")

    # @classmethod
    @staticmethod
    def f():
        print("my name is zhanghengtao.")
        print("******" * 20)


g.h()
g.f()
z = g()
z.h()
z.f()

