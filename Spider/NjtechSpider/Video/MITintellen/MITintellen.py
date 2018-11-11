# 文件保存至videoLink.txt 为所有视频的URL

import sys
import requests
import random
from lxml import etree
from useragents import USER_AGENTS


def getHTMLTEXT(url):
    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        response = requests.get(url, timeout=30, verify=False, headers=headers)
        response.raise_for_status()
        if 'charset' not in response.headers.keys():       # 确保编码方式的正确
            response.encoding = response.apparent_encoding
        return response.text
    except requests.exceptions.ConnectionError:
        return 'getHTMLTEXT Error!'


def getUrls(htmlText):
    video_num = 0
    htmlText_HTML = etree.HTML(htmlText)
    allDivs = htmlText_HTML.xpath('//*[@id="j-playlist-container"]/div/div')
    for eachDiv in allDivs:
        video_num += 1
        if video_num == 1:
            continue
        else:
            eachUrl = eachDiv.xpath('a')[0].attrib['href']
            print(eachUrl)
            if eachUrl not in allUrls:
                allUrls.append(eachUrl)
        print(video_num)

    return allDivs          # allDivs  - return for debug


def saveUrls():
    with open('videoLink.txt', 'w') as file:
        for eachUrl in allUrls:
            eachUrlForWrite = eachUrl + '\n'
            file.write(eachUrlForWrite)


start_url = "http://open.163.com/movie/2017/9/Q/S/MCTMNN3UI_MCTMNR8QS.html"
allUrls = [start_url]

if __name__ == '__main__':
    htmlText = getHTMLTEXT(start_url)
    allDivs = getUrls(htmlText)
    saveUrls()
