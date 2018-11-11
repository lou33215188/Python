# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:16:41 2018

@author: 王磊
"""

import requests
# from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from useragents import USER_AGENTS
import random
import os


def getHTMLTEXT(url):
    try:
        headers = {"User-Agent" : random.choice(USER_AGENTS)
                  }
        response = requests.get(url, timeout=30, verify=False, headers=headers)
        response.raise_for_status()
        if 'charset' not in response.headers.keys():       # 确保编码方式的正确
            response.encoding = response.apparent_encoding
        return response.text
    except:
        return 'getHTMLTEXT Error!'

def loadintxt(fileName):
     with open(fileName, 'r', encoding='utf-8') as file:
          comment = file.readlines()
     
     return comment


os.chdir('D:\Python\Spider\AMAZONcom')

count = 0

files = os.listdir()
for each in files:
     os.chdir(each)
     eachtxt = os.listdir()
     for eachtwo in eachtxt:
          comment = loadintxt(eachtwo)
          for eachline in comment:
               if eachline != '\n':
                    count += 1
     os.chdir('..')
print(count)

     
