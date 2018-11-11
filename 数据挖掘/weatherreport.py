# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:19:04 2018

@author: 王磊
"""

#coding=utf-8  
import urllib.request as urllib2  
from city import cityDict 
import json  
  
  
  
cityname = input("你想查询那个城市的天气:")  
citycode=""  
  
try:  
    citycode =cityDict[cityname]  
except:  
    print("not Found")  
if citycode:  
    try:  
        url= "http://www.weather.com.cn/data/cityinfo/"+citycode+".html"#构造网址  
        content = urllib2.urlopen(url).read()#读取网页源代码  
        data =json.loads(content)#使用json库将字符转化为字典  
        #print type(data)  
        #print (content)  
        res =data["weatherinfo"]#获取字典  
        str_temp=("%s :%s~%s")%(res["weather"],res["temp1"],res["temp2"])#格式化字符  
        print(str_temp)#输出天气信息  
    except:  
        print("Not Found!!")  
        