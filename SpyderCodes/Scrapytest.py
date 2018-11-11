# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:37:50 2018

@author: 王磊
"""

import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import os

def getHTMLTEXT(url):
    try:
        response = requests.get(url, timeout=30, verify=False)
        response.raise_for_status()
        if 'charset' not in response.headers.keys():       # 确保编码方式的正确
            response.encoding = response.apparent_encoding
        return response.text
    except:
        return 'getHTMLTEXT Error!'

            
def saveComments(floders='D:/Python/aMAZON'):
     pass


def mainFunction():
     commodityURLS = []
     
     
     
     