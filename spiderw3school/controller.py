from spiderw3school.downloadHtml import downloadHtml
from spiderw3school.spiderHtml import url_set
from spiderw3school.spiderHtml import headless_parser
from spiderw3school.saveData import createFile
from spiderw3school.saveData import saveData


class Controller(object):
    def __init__(self, url):
        web = downloadHtml(url)
        self.urls = url_set(web)
        # 爬取w3shool里Python教程（爬取1层内容），存为word作为电子书；
        self.fdoc = createFile()

    def url_join(self, url_pop):
        root_url = "https://www.w3school.com.cn"
        url = root_url + url_pop
        print(url)
        return url

    def get_one_url(self):
        url_pop = self.urls.pop(0)
        url = self.url_join(url_pop)
        return url

    def get_url_by_index(self, i):
        url_pop = self.urls[i]
        url = self.url_join(url_pop)
        return url

    def load_parser(self, url):
        text_str = headless_parser(url)
        return text_str

    def save(self, text):
        saveData(self.fdoc, strings=text)


if __name__ == "__main__":
    # root_url = "https://www.w3school.com.cn"
    url = "https://www.w3school.com.cn/python/index.asp"
    Ctrl = Controller(url)
    pop_url = Ctrl.get_one_url()
    text_str = Ctrl.load_parser(pop_url)
    Ctrl.save(text_str)

