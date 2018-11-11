# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:44:50 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(0, 255, size=[40,40,40])

x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')
ax.scatter(x[:10], y[:10], z[:10], c='y')
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

plt.show()


