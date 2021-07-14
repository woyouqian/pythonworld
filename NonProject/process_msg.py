import multiprocessing
import random
import os
import time
from multiprocessing import Process, Queue

"""
def proc_send(pipe, urls):
    for url in urls:
        print("Process %s send: %s ..." % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print("Process %s recv：%s ..." % (os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    # Pipe常用来在两个进程间进行通信，两个进程分别位于管道的两端。
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['Python world url_' + str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
"""


def proc_write(q, urls):
    print("Process %s is writing ..." % os.getpid())
    for url in urls:
        q.put(url)
        print("Put %s to the queue ..." % url)
        time.sleep(random.random())


def proc_read(q):
    print("Process %s is reading ..." % os.getpid())
    while True:
        url = q.get()
        print("Get %s from queue ..." % url)


if __name__ =="__main__":
    q = Queue()
    process_write1 = Process(target=proc_write, args=(q, ['Python url_1', 'Python url_2', 'Python url_3', 'Python url_4']))
    process_write2 = Process(target=proc_write, args=(q, ['World url_5', 'World url_6', 'World url_7']))
    process_reader = Process(target=proc_read, args=(q,))

    process_write1.start()
    process_write2.start()
    process_reader.start()

    process_write1.join()
    process_write2.join()
    # process_reader.join()
    # 进程里有死循环存在，只能强行终止程序
    # time.sleep(6)
    process_reader.terminate()

