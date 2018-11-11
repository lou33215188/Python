# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:09:35 2018

@author: 王磊
"""

import matplotlib.pyplot as plt

fig1 = plt.figure(num=1, figsize=(1, 2))
plt.plot(1, 2)
fig2 = plt.figure(num=0, figsize=(1, 1))
plt.plot(2, 3)
plt.show()
plt.close()
