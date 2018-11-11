# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:05:23 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

arrayNum = 10

np.random.seed(20)

testArray = np.linspace(0, 2*np.pi, arrayNum, endpoint=False)
radii = 10 * np.random.rand(arrayNum)
width = np.pi / 2 * np.random.rand(arrayNum)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(testArray, radii, width, bottom=0.0)

for r,bar in zip(radii, bars):
     bar.set_facecolor(plt.cm.viridis( r / 10.))
     bar.set_alpha(0.5)

plt.show()
