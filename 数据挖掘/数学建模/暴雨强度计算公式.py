# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:49:38 2018

@author: 王磊
"""

#
#Wednesday, June 6, 2018
#4:42 PM
#
#Qy=Ψ·q·F计算
#式中：
#Qy—设计雨水流量(L/s);
#Ψ—径流系数;取0.9
#q—暴雨强度（L/s·ha）
#（ha公顷）;
#F—汇水面积（ha）
#其中
#	
#式中：
#P—设计重现期，取2年
#t—降雨历时（min）;取5min
#则q5=414L/(s·ha)(p=2、t=5min)


import matplotlib.pyplot as plt
import numpy as np


def qCalc(t, P=10, A1=17.9, C=12.07, b=13.30, n=0.80):
     result = 166.667*A1*(1 + C/A1 * np.log10(P)) /(np.power(t+b,n))
     return result

def QCalc(fi, q, F):  # 单位是m3/s
     result = fi*q*F/1000
     return result

def kCalc(q):
     result = (0.669*q+0.561)/(0.225+3*q)
     return result

def xieshui(q1):
     result = 0.221*q1 - 8.07
     return result

def vl(q, k=1):
     result = q + k*5.92*np.power(10.0,-6)
     return result

def yita( vs, Q, p=12):
     resulte = np.power(np.e, -(p*0.223*(vs+Q)-8.07)*(vs+Q))
     result = np.sqrt(1-np.power(resulte, 1.00001))
     return result  
     

t = 5 * 60 # 单位是s
fi = 0.9 # 径流系数
A1 = 17.9 # 汇水面积
F = 1.7407  # ha
p = 20


plt.title('比值函数', fontproperties='SimHei', fontsize=25, color='black')
testX = np.arange(0,500,0.5)
testq = qCalc(testX/50)         #暴雨强度
testQ = QCalc(fi, testq, F)   #流量
testQ2 = QCalc(fi, testq, F-1)  # 平面的流量
vlr = vl(testQ)      #vl流入
vs = 4*vlr          #总的流入
ryita = yita(vs,testQ2)   #η的值

plt.plot(testX, ryita)
plt.xlabel('t')
plt.ylabel('η')
plt.show()







