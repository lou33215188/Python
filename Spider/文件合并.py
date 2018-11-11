# -*- coding: utf-8 -*-
"""
Created on Sat May 19 21:19:56 2018

@author: 王磊
"""

import os


def loadintxt(fileName):
     with open(fileName, 'r', encoding='utf-8') as file:
          comment = file.readlines()
     
     return comment

def addtxt(textcomments, fileName='D:\\Python\\Spider\\allcommenttxt.txt'):
     with open(fileName, 'a', encoding='utf-8') as file:
          file.writelines(textcomments)


os.chdir('D:\\Python\\Spider\\AMAZONcom')

files = os.listdir()
for each in files:
     os.chdir(each)
     eachtxt = os.listdir()
     for eachtwo in eachtxt:
          comment = loadintxt(eachtwo)
          addtxt(comment)
                         
     os.chdir('..')
