# -*- coding: utf-8 -*-
"""
Created on Sat May  5 23:17:17 2018

@author: 王磊
"""

# coding:utf-8  
import numpy as np
import matplotlib.pyplot as plt

def drawHeart():
     plt.figure(figsize=(12, 6))
     arrayOne = np.linspace(-np.pi/2, np.pi/2, 1000)
     x = np.cos(arrayOne)
     y = np.sin(arrayOne) + np.power(x, 2.0/3)
     
     plt.plot(x, y, color='red', linewidth=2, label='h')
     plt.plot(-x, y, color='red', linewidth=2, label='h')
     plt.xlabel('横轴:时间', fontproperties='FangSong', fontsize=20, color='r')
     plt.ylabel('纵轴:高度', fontproperties='FangSong', fontsize=20, color='b')
     
     plt.xlim(-2, 2)
     plt.ylim(-1.5, 2)
     
     plt.show()

if __name__ == '__main__':
     drawHeart()
