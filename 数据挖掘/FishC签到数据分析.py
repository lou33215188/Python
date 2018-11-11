# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:41:15 2018

@author: 王磊
"""

import requests
from bs4 import BeautifulSoup
import time
import random

count = int(input("请输入你想获取的页数："))
numbers = count
page = 1
target = []
tim = []

while count>0:
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        }

    url ="http://bbs.fishc.com/plugin.php?id=k_misign:sign&operation=list&op=&page="+str(page)+"&inajax=1&ajaxtarget=ranklist"

    res = requests.get(url,headers = headers)

    soup = BeautifulSoup(res.text,"lxml")

    tr = soup.find_all("tr")

    del tr[0]

    del tr[15]

    name = []
    alldays = []
    monthdays = []
    lasttime = []
    level = []
    bonus = []
    result = []

    for each in tr:
        name.append(each.find_all("td")[0].text)
        alldays.append(each.find_all("td")[1].text)
        monthdays.append(each.find_all("td")[2].text)
        lasttime.append(each.find_all("td")[3].text)
        level.append(each.find_all("td")[4].text)
        bonus.append(each.find_all("td")[5].text)

    for each in range(len(tr)):
        result.append(name[each]+"   "+alldays[each]+"   "+monthdays[each]+"   "+lasttime[each]+"   "+level[each]+"   "+bonus[each])

    for each in result:
        print(each)
    
    count -=1
    page +=1
    target += alldays
    tim += lasttime

    sleep = random.randint(60,65)
    print("数据还有{}秒到达战场，请等待一下下".format(sleep))
    time.sleep(sleep)
    
print("已经为您统计{}条数据，正在为您分析：".format(numbers*15))
  
targets =[]
for each in target:
    targets.append(int(each))
    
targets.sort()

amount = len(targets)

if amount%2 == 0:
    print("今日签到的人总天数中位数为：{}".format(targets[int(amount/2)]))
    print("今日签到的人总天数中位数为：{}".format(targets[int((amount/2)+1)]))

else:
    print("今日签到的人总天数中位数为：{}".format(targets[int((amount+1)/2)]))

dic = {}
tims = []
for each in tim:
    tims.append(each[11:13])
    
for each in tims:
    if each in dic:
        dic[each] += 1
    else:
        dic[each] = 1
        
sorteddic = sorted(dic.items(),key=lambda x:x[0])
date = input("请输入今天的日期：（格式为：xxxx—xx—xx）：")
hour = input("请输入现在时间精确到小时即可（24小时制)：")
for i in range(int(hour)+1):
    with open((date+".text"),"a") as file:
        file.write(str(sorteddic[i])+"\n")
