# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:57:29 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

def drawHeart():
     plt.figure(figsize=(12, 6))
     arrayOne = np.linspace(0, np.pi, 1000)
     x = np.sin(arrayOne)
     y = np.cos(arrayOne) + np.power(x, 2.0/3)
     
     plt.plot(x, y, color='red', linewidth=2, label='h')
     plt.plot(-x, y, color='red', linewidth=2, label='h')
     plt.xlabel('横轴:时间', fontproperties='FangSong', fontsize=20, color='r')
     plt.ylabel('纵轴:高度', fontproperties='FangSong', fontsize=20, color='b')
     
     plt.xlim(-2, 2)
     plt.ylim(-1.5, 2)
     
     plt.show()

if __name__ == '__main__':
     drawHeart()
