from spiderw3school.downloadHtml import downloadHtml
from spiderw3school.spiderHtml import url_set
from spiderw3school.spiderHtml import headless_parser
from spiderw3school.saveData import createFile
from spiderw3school.saveData import saveData
from multiprocessing import Process
from multiprocessing import Pool


global cpus
cpus = 4

url = "https://www.w3school.com.cn/python/index.asp"
web = downloadHtml(url)
urls = url_set(web)
total = len(urls)
limit = total//cpus + 1


def run_func(i):
    root_url = "https://www.w3school.com.cn"
    file = createFile(i)
    for j in range(limit * i, limit * (i + 1)):
        if j < total:
            pop_url = root_url + urls[j]
            text_str = headless_parser(pop_url)
            saveData(file, strings=text_str)
        else:
            break


if __name__ == "__main__":
    print("==================== game start to end! ====================")
    # use mutiprocessing get it;

    for i in range(cpus):
        process = Process(target=run_func, args=(i,))
        process.start()

    process.join()

