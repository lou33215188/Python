# -*- coding: utf-8 -*-
"""
Created on Fri May  4 17:04:54 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

MU = 100
SIGMA = 20
#bin 直方图的个数
# normad = 1 概率  normad = 0 个数
arrayA = np.random.normal(MU, SIGMA, 100)
plt.hist(arrayA, 20, normed=1, color='red')
plt.grid(True)
plt.show()

