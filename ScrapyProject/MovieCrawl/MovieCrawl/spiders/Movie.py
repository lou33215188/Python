# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from MovieCrawl.items import MoviecrawlItem
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getHTMLTEXT(url):
    try:
        response = requests.get(url, timeout=30, verify=False)
        response.raise_for_status()
        if 'charset' not in response.headers.keys():       # 确保编码方式的正确
            response.encoding = response.apparent_encoding
        return response.text
    except:
        return 'getHTMLTEXT Error!'
            

class MovieSpider(scrapy.Spider):
    name = 'Movie'
    allowed_domains = ['80s.tw/movie']

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


    def parseFunc(self, response):
        item = MoviecrawlItem()
        element = response.xpath('//*[@id="minfo"]/div[1]/img')
        try:
            pcitreLink = element[0].xpath('@src').extract()[0]
            item['pictureLink'] = pcitreLink
        except IndexError:
            item['pictureLink'] = 'Pciture Not Found!\n The Link is ' + response.url
        try:
            title = element[0].xpath('@title').extract()[0]
            item['cineName'] = title
        except IndexError:
            item['cineName'] = 'CineName Not Found\n The Link is ' + response.url
        try:
            downloadLink = response.xpath('//*[@id="myform"]/ul/li[2]/span[3]/a/@href').extract()[0]
            item['downloadLink'] = downloadLink
        except IndexError:
            item['downloadLink'] = 'DownLoad Link Not Found !\n The Link is ' + response.url
        try:
            iD = response.xpath('//*[@id="wap-enter"]/a/@href').extract()[0].split('/')[-1]
            item['iD'] = iD
        except IndexError:
            item['iD'] = 'ID Not Found ! \n The Link is ' + response.url

        yield item