import requests
import urllib
from chardet import detect


def downloadHtml(url):
    resp = requests.get(url)
    # print(type(resp))
    # char = requests.chardet.detect(resp.content)
    # char = detect(resp.content)
    # resp.encoding = char.get('encoding')
    # print(resp.headers)
    # print(resp.content)
    web_str = resp.text
    # print(web_str)
    return web_str


if __name__ == '__main__':
    url = "https://www.w3school.com.cn/python/index.asp"
    downloadHtml(url)

