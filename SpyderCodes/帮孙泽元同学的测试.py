# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:46:08 2018

@author: 王磊
"""

import json

def loadFont():
    setting = json.load("李白.json","r")
    family = setting['content']
    return family

def jsonl():
     dic = []
     with open("李白.json",'r', encoding='utf-8') as file:
          alllines = file.readlines()
          for eachline in alllines:
               dic.append(eval(eachline))
          
     return dic


allJsonString = jsonl()      
jsonDict = []
for eachString in allJsonString:
     eachString[0]