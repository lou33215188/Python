# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:22:43 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

def attenuation(aNumber):
     return np.exp(-aNumber) * np.cos(2*np.pi*aNumber)


xArray = np.arange(0.0, 6.0, 0.02)
yArray = attenuation(xArray)

plt.xlabel('横轴:时间', fontproperties='SimHei', fontsize=25, color='green')
plt.ylabel('纵轴:振幅', fontproperties='SimHei', fontsize=25, color='black')
plt.title('衰减函数', fontproperties='SimHei', fontsize=25)
#
#plt.annotate('', fontproperties='SimHei', fontsize=25, xy=(2,1), \
#             xytext=(3,1.5), arrowprops=dict(facecolor='green', shrink=0.1, width=2))

plt.plot(xArray, yArray, 'b-')
plt.axis([0,6,-1,2])
plt.grid(True)

plt.show()
