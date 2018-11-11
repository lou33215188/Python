# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:37:50 2018

@author: 王磊
"""

import os
import random
import time

import requests
from lxml import etree
# from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from useragents import USER_AGENTS

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def getHTMLTEXT(url):
    try:
        headers = {"User-Agent" : random.choice(USER_AGENTS)
                  }
        response = requests.get(url, timeout=30, verify=False, headers=headers)
        response.raise_for_status()
        if 'charset' not in response.headers.keys():       # 确保编码方式的正确
            response.encoding = response.apparent_encoding
        time.sleep(2)
        return response.text
    except:
        return 'getHTMLTEXT Error!'

def getComments(etreeHTML):
     comments = etreeHTML.xpath('//*[@data-hook="review"]/div/div[4]/span/text()')
     constumer = etreeHTML.xpath('//*[@id="customer_review-R19YD9W7Y7NAIX"]/div[2]/span[1]/a')
     return comments
# 获取当前页评论的函数 返回的comments是一个列表


def saveComments(comments, textComments='None.txt'):
     with open(textComments, 'w', encoding='utf-8') as commentFile:
            for eachcomment in comments:
                 eachcomment += '\n\n\n'
                 commentFile.write(eachcomment)

def loadinTXT(fileName='D:\\Python\\Spider\\商品链接.txt'):
     resultComments = []
     with open(fileName, 'r') as file:
          comments = file.readlines()
     for eachcomment in comments:
          eachcomment = eachcomment[:-1]
          resultComments.append(eachcomment)
          # 把每个链接后面的换行符拿走
     return resultComments  #返回的是每个商品的链接


def getCommentUrl(comurl):
     comHTMLTEXT = getHTMLTEXT(comurl)
     comHTML = etree.HTML(comHTMLTEXT)
     commentUrlfirst = comHTML.xpath('//*[@id="reviews-medley-footer"]/div[1]/a')[0].attrib['href']
     print('\n\n\n\n\n')
     commentUrl = commentUrlfirst.split('?')[0] + '_1' + '?pageNumber=1'
     
     return 'https://www.amazon.com' + commentUrl
# 该函数返回的是从商品页面获得的评论链接


def saveCommentUrl(commentUrl):
     with open('comment.txt', 'a') as file:
          file.write(commentUrl + '\n')


def mainFunction():
     

     commentURLS = []
#################################################################
#     commodityUrls = loadinTXT()
#     print(commodityUrls)
#     for eachcommodityUrl in commodityUrls:
#          try:
#               commentURL = getCommentUrl(eachcommodityUrl)
#               commentURLS.append(commentURL)
#               saveCommentUrl(commentURL)
#          except IndexError:
#               print(eachcommodityUrl + '\n\n\n')
#               continue
     # 到这里commentURLS包括了所有的评论首页
     
#     commentURLS = commentURLS
#################################################################
#  如果是第一次爬，取消注释即可，会自动缓存comment.txt文件
#  因为已经缓存过，所以直接使用以下的代码
     commentURLS = loadinTXT(fileName='D:\\Python\\Spider\\comment.txt')
     commentURLS = commentURLS[28: 29] + commentURLS[37: 38]
     # 断点重启!

##########################################################
     # 存放每个商品的评论首页面的URL
     floder = 'D:\\Python\\Spider\\AMAZONcom'
     os.chdir(floder)
     # 把工作目录转移到Spider/AMAZONcom目录下
     
     for eachUrl in commentURLS:
          #这里的eachURL指的是每个评论页面
          textFileName = eachUrl.split('/')[-2]
          #每个商品的文件名
          print(textFileName)
          if textFileName not in os.listdir():
               os.mkdir(textFileName)
          #创建每个商品的文件夹
          os.chdir(textFileName)
          #工作目录在每个文件夹里
          htmltext = getHTMLTEXT(eachUrl)
          html = etree.HTML(htmltext)
          # 利用etree解析html文本
          pageNum = int(html.xpath('//ul/li[7]/a')[0].text)
          # 从第一页的标签获取到总共的评论数目
          firstPageComments = getComments(html)
          # 获取第一页的评论
          saveComments(comments=firstPageComments, textComments='CommentsPage1.txt')
          # 先保存第一页的评论
          for eachNum in range(pageNum - 1):
               eachNum = eachNum + 1
               eachPageUrl = eachUrl[:-1] + str(eachNum)
               # eachPageUrl是指每一页评论的URL
               htmltextEach = getHTMLTEXT(eachPageUrl)
               htmlEach = etree.HTML(htmltextEach)
               # 得到了每一页的HTML文本对象
               eachPageComments = getComments(htmlEach)
               # 获取了每一页的评论
               textCommentsPrefix = 'CommentsPage'
               textComments = textCommentsPrefix +  str(eachNum) + '.txt'
               # 每个评论页面的评论
               saveComments( comments=eachPageComments, textComments=textComments)
               
          os.chdir(floder)
         
if __name__ == '__main__':
     mainFunction()




