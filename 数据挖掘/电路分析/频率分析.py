# -*- coding: utf-8 -*-
"""
Created on Tue May 22 00:36:35 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

def imZ_RL(R, L, oumiga):
     return np.sqrt((R**2 + (oumiga*L)**2))

def oumi_RL(R, L, oumiga):
     return np.arctan((oumiga*L)/R)

R = 1
L = 1

testoumiga = np.arange(0, 3, 0.2)
resultimZ = imZ_RL(R, L, testoumiga)

figOne = plt.figure(figsize=(12,6), num="PictureOne")

figOne.add_subplot(221)
plt.plot(testoumiga, resultimZ)
plt.title('频率特性:|Z|', fontproperties='SimHei', fontsize=25, color='green')
plt.xlabel('w')
plt.ylabel('|Z|')

figOne.add_subplot(222)
plt.plot(testoumiga, oumi_RL(R, L, testoumiga))
plt.title('频率特性:|Fi|', fontproperties='SimHei', fontsize=25, color='red')
plt.xlabel('w')
plt.ylabel('Fi')

plt.suptitle('频率分析', fontproperties='SimHei', fontsize=25, color='black')
plt.legend()
plt.show()
