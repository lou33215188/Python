# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:26:34 2018

@author: 王磊
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt  
import numpy as np
import xlrd
from scipy.interpolate import griddata

dataX = []
dataY = []
dataZ = []
dataXY = []
dataXYZ = []
file = r'C:\Users\Princeling\Documents\学习委员\数学建模\南工塔周围.xls'
wb = xlrd.open_workbook(filename=file)
ws = wb.sheet_by_name('Sheet1')
dataset = []
for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r,c).value)
    dataset.append(col)


for eachdata in dataset:
     if isinstance(eachdata[0], float):
          dataX.append(eachdata[1])
          dataY.append(eachdata[2])
          dataZ.append(eachdata[3])
          dataXY.append([eachdata[1],eachdata[2]])
          dataXYZ.append([eachdata[1],eachdata[2],eachdata[3]])


dataX = np.array(dataX)
dataY = np.array(dataY)
dataZ = np.array(dataZ)
lineX = np.arange(dataX.min(), dataX.max(), 1)
lineY = np.arange(dataY.min(), dataY.min(), 1)

dataX_Y = []
for each in dataX:
     dataX_Y.append(each)

for each in dataY:
     dataX_Y.append(each)
     
fig = plt.figure()
ax = Axes3D(fig)

dataX, dataY = np.meshgrid(dataX, dataY)
dataZ = np.sqrt(dataX**2, dataY**2)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(dataX, dataY, dataZ, rstride=1, cstride=1, cmap='rainbow')

plt.show()
#
#grid_z0 = griddata(dataXY, dataZ, dataX_Y, method='cubic')
#
#fig = plt.figure()  
#ax = fig.add_subplot(111, projection='3d')  
#  
## Make data  
#
#  
## Plot the surface  
#ax.plot(dataX, dataY, grid_z0, color='b')  
#  
#plt.show()  