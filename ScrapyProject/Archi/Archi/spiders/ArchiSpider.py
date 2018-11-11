# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree


def getHTMLTEXT(url):
    try:
        response = requests.get(url, timeout=30, verify=False)
        response.raise_for_status()
        if 'charset' not in response.headers.keys():       # 确保编码方式的正确
            response.encoding = response.apparent_encoding
        return response.text
    except:
        return 'getHTMLTEXT Error!'
            

class ArchispiderSpider(scrapy.Spider):
    name = 'ArchiSpider'
    allowed_domains = ['http://jzsc.mohurd.gov.cn/dataservice/query/comp/list']
    
    
    def start_requests(self):
        pageUrlPrefix = 'https://www.80s.tw/movie/list/-----p'  # 网页url的前缀
        crawlNum = 400
        thisPageMovieLinkPrefix = 'https://www.80s.tw'
        for eachNum in range(crawlNum):
            pageUrl = pageUrlPrefix + str(eachNum+1)
            htmlTEXT = getHTMLTEXT(pageUrl)   # 这里获得了每一页的HTML文本文件
            html = etree.HTML(htmlTEXT)  #利用lxml.etree来解析html文本
            thisPageMovieTags = html.xpath('//*[@id="block3"]/div[3]/ul[2]/li/a')  #这么页面所有电影的链接
            for eachTag in thisPageMovieTags:
                thisPageMovieLinkSuffix = eachTag.attrib['href']   #href仅仅是后缀，所以要拼接
                thisPageMOvieLink = thisPageMovieLinkPrefix + thisPageMovieLinkSuffix
                yield scrapy.Request(url=thisPageMOvieLink, callback=self.parseFunc)

    def parse(self, response):
        pass
