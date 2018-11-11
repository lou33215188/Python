# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:08:07 2018

@author: 王磊
"""

import requests
from bs4 import BeautifulSoup

html=requests.get("http://nj.meituan.com/meishi/b1063/?attrs=65:154")
soup=BeautifulSoup(html.text,"lxml")
text=soup.find_all('欢乐')
print(text)
