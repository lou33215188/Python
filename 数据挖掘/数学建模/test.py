# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:56:09 2018

@author: 王磊
"""

import matplotlib as mpl  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  
import matplotlib.pyplot as plt  
  
mpl.rcParams['legend.fontsize'] = 10  

def func(x, y, z):
    return x*(1-x)*np.cos(4*np.pi*x) * (np.sin(4*np.pi*y**2)**2)*z

points = np.random.rand(10, 3)#实际点坐标
values = func(points[:,0], points[:,1],points[:,2])#实际点的值
fig = plt.figure()  
ax = fig.gca(projection='3d')  
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)  
z = np.linspace(-2, 2, 100)  
r = z**2 + 1  
x = r * np.sin(theta)  
y = r * np.cos(theta)  
ax.plot(x, y, z, label='parametric curve')  
ax.legend()  
  

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
plt.show()  