import lxml
import time
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver


def url_set(web):

    path = etree.HTML(web)
    div = path.xpath("//div[@id='course']")[0]
    urls = div.xpath(".//a/@href")
    print(urls)
    return urls


def bs4_spider(web):
    pass


def xpath_spider(web):
    path = etree.HTML(web)
    div = path.xpath("//div[@id='maincontent']")[0]
    str_divs = div.xpath(".//div")
    # print(str_divs)
    str_divs.pop(0)
    str_divs.pop()

    for obj in str_divs:
            print(obj.xpath("./text()"))
            print('------'*18)


def auto_parser(url):
    text_str = ''
    # driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver")

    driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver")
    driver.get(url)
    driver.maximize_window()
    try:
        # driver.find_element_by_xpath("//div[@id='maincontent']")
        str_divs = driver.find_elements_by_xpath("//div[@id='maincontent']//div")
        # print(str_divs)
        str_divs.pop(0)
        str_divs.pop()
        # print(str_divs)

        if str_divs:
            for div in str_divs:
                text_str += div.text + '\n\n'
            print(text_str)
            print('------'*18)
    except Exception as e:
        print('>>>>>>>>>>>---- %s' % e)
    finally:
        time.sleep(4)
        driver.close()

        return text_str


def phantomjs_parser(url):
    text_str = ''
    # driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver")
    # driver.get(url)
    # driver.maximize_window()

    driver = webdriver.PhantomJS()
    driver.get(url)
    try:
        # driver.find_element_by_xpath("//div[@id='maincontent']")
        str_divs = driver.find_elements_by_xpath("//div[@id='maincontent']//div")
        # print(str_divs)
        str_divs.pop(0)
        str_divs.pop()
        # print(str_divs)

        if str_divs:
            for div in str_divs:
                text_str += div.text + '\n\n'
            print(text_str)
            print('------'*18)
    except Exception as e:
        print('>>>>>>>>>>>---- %s' % e)
    finally:
        time.sleep(4)
        driver.close()

        return text_str


def headless_parser(url):
    text_str = ''
    # driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver")
    # driver.get(url)
    # driver.maximize_window()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver",
                              options=options,
                              # chrome_options=options
                              )
    driver.get(url)
    try:
        # driver.find_element_by_xpath("//div[@id='maincontent']")
        str_divs = driver.find_elements_by_xpath("//div[@id='maincontent']//div")
        # print(str_divs)
        str_divs.pop(0)
        str_divs.pop()
        # print(str_divs)

        if str_divs:
            for div in str_divs:
                text_str += div.text + '\n\n'
            print(text_str)
            print('------'*18)
    except Exception as e:
        print('>>>>>>>>>>>---- %s' % e)
    finally:
        time.sleep(5)
        driver.close()

        return text_str


def auto_click_next(url):
    # driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver")

    driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver")
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    for i in range(109):
        try:
            a = driver.find_element_by_xpath("//div[@id='bpn']//li[@class='next']/a")
            # print(a)
            a.click()
            time.sleep(4)
        except Exception as e:
            print(e)

    time.sleep(6)
    driver.close()


if __name__ == '__main__':
    from spiderw3school.downloadHtml import downloadHtml
    root_url = "https://www.w3school.com.cn"
    url = "https://www.w3school.com.cn/python/index.asp"
    # web = downloadHtml(url)
    # url_set(web)
    # xpath_spider(web)
    # auto_parser(url)
    # phantomjs_parser(url)
    # headless_parser(url)
    auto_click_next(url)

