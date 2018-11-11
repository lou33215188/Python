import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re


def get_one_page(url):                   #抓取网页
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
        pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                             '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                             '.*?integar">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
        items = re.findall(pattern, html)
        print(items)


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    parse_one_page(html)


if __name__ == '__main__':
    main()