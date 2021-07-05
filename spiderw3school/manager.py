import time
from spiderw3school.controller import Controller


'''
def run(url):
    global cpus
    cpus = 4

    Ctrl = Controller(url)
    total = len(Ctrl.urls)
    limit = total//cpus + 1

    def running(i):
        file = createFile(i)
        for j in range(limit*i, limit*(i+1)):
            if j < total:
                pop_url = Ctrl.get_url_by_index(j)
                text_str = Ctrl.load_parser(pop_url)
                saveData(file, strings=text_str)
            else:
                break

    return running
'''


# url = "https://www.w3school.com.cn/python/index.asp"
# run_func = run(url)
# print(run_func)
# run_func(0)


if __name__ == "__main__":
    # root_url = "https://www.w3school.com.cn"

    url = "https://www.w3school.com.cn/python/index.asp"
    Ctrl = Controller(url)
    total = len(Ctrl.urls)
    start = time.time()
    print("==================== game start ====================")

    # 指定从第i条url继续爬取数据；
    # for i in range(99, total):
    for i in range(total):
        print("-------------------- the total is %d , the %d is running... --------------------" % (total, i+1))
        pop_url = Ctrl.get_one_url()
        # 取指定第i条的url值；
        # pop_url = Ctrl.get_url_by_index(i)
        text_str = Ctrl.load_parser(pop_url)
        Ctrl.save(text_str)
    
    end = time.time()
    all_time = end - start
    print("==================== game over! ====================")
    print("******************** programme run cost all time: %f sec... ********************" % all_time)

