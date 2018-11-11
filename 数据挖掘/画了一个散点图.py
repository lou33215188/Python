# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:28:14 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

xArray = np.random.randn(100)
yArray = np.random.randn(100)


ax = plt.subplot()

ax.plot(10 * xArray, 10 * yArray, 'ro')
ax.set_title('Simple Scatter')

xArray = np.random.randn(100)
yArray = np.random.randn(100)
plt.figure()
ax2 = plt.subplot()
ax2.plot(xArray*10, yArray*10, 'o')
ax2.set_title('Simple!')

plt.show()
