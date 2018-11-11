# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:11:34 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

arrayX = np.arange(-1, 5, 0.02)
arrayY = np.cos(np.pi * arrayX)

plt.plot(arrayX, arrayY, 'b.-')
plt.xlabel('横轴:时间', fontproperties='SimHei', fontsize=25, color='green')
plt.ylabel('纵轴:振幅', fontproperties='SimHei', fontsize=25, color='black')
plt.title('正弦函数:y = cos(πx)', fontproperties='SimHei', fontsize=25)

plt.annotate('极大值点', fontproperties='SimHei', fontsize=25, xy=(2,1), \
             xytext=(3,1.5), arrowprops=dict(facecolor='green', shrink=0.1, width=2))


plt.axis([-2,6,-2,2])
plt.grid(True)
plt.show()
