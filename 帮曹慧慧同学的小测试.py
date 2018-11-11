# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:42:02 2018

@author: 王磊
"""


#def func(string):
#     sumWord = 0
#     for eachWord in string:
#          sumWord += int(eachWord)
#     return sumWord
#
#n=input("请输入一个整数：")
#
#sumWord = func(n)
#
#print(sumWord)


def isdiff(number):
     flag = 0       #假设他是假的
     numberStr = str(number)  #确保分析的是一个字符串
     index = 0
     for eachNumberStr in numberStr:
          tempList = list(numberStr)
          tempList.pop(index)
          index+=1
          if eachNumberStr in tempList:
             flag = 1 
             break
              
     return flag     # 以后碰到判断的，直接返回一个flag就好了,=1为真 =0 为假
