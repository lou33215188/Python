# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:39:37 2018

@author: 王磊
"""

import matplotlib.pyplot as plt
import numpy as np

xArray = np.arange(0, 10, 0.02)
yArray = 6 * xArray

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot(121, projection='polar')
ax2 = plt.subplot(122, projection='polar')
ax2.set_theta_direction(-1)             
     
#     set_theta_direction方法用于设置极坐标的正方向
#     
#     当set_theta_direction的参数值为1,'counterclockwise'或者是'anticlockwise'
#     的时候，正方向为逆时针；
#     当set_theta_direction的参数值为-1或者是'clockwise'的时候，正方向为顺时针；
#     默认情况下正方向为逆时针

ax1.set_theta_zero_location('N')
#     set_theta_zero_location方法用于设置极坐标0°位置
#     
#     0°可设置在八个位置，分别为N, NW, W, SW, S, SE, E, NE
#     当set_theta_zero_location的参数值为'N','NW','W','SW','S','SE','E','NE'时，
#     0°分别对应的位置为方位N, NW, W, SW, S, SE, E, NE；
#     默认情况下0°位于E方位

ax1.set_thetagrids(np.arange(0, 360, 30))

#     et_thetagrids方法用于设置极坐标角度网格线显示
#     
#     参数为所要显示网格线的角度值列表
#     默认显示0°、45°、90°、135°、180°、225°、270°、315°的网格线

ax2.set_theta_offset(np.pi)

#     set_theta_offset方法用于设置角度偏离
#     
#     参数值为弧度值数值

ax2.set_rgrids(np.arange(15, 100, 10))

#     
#     set_rgrids方法用于设置极径网格线显示
#     
#     参数值为所要显示网格线的极径值列表，最小值不能小于等于0

ax1.set_rlabel_position(90)
#     
#     set_rlabel_position方法用于设置极径标签显示位置
#     
#     参数为标签所要显示在的角度

ax1.set_rlim(30, 50)
#     
#     set_rlim方法用于设置显示的极径范围
#     
#     参数为极径最小值，最大值

ax1.set_rticks(np.arange(10, 60 ,10))
#     
#     set_rticks方法用于设置极径网格线的显示范围


ax1.plot(xArray, yArray, 'r--',)
ax2.plot(xArray, yArray, 'b--',)

ax2.set_rmax(50)

#     set_rmax方法用于设置显示的极径最大值
#     
#     该方法要在绘制完图像后使用才有效

ax2.set_rmin(20)

#     set_rmin方法用于设置显示的极径最小值
#     
#     该方法要在绘制完图像后使用才有效

ax1.set_rscale('linear')
ax2.set_rscale('linear')
     
#     set_rscale方法用于设置极径对数坐标
#     
#     参数值为'linear','log','symlog'
#     默认值为'linear'
#     该方法要在绘制完图像后使用才有效
'''
Example:
     import numpy
     from matplotlib import pyplot
     
     # Enable interactive mode
     pyplot.ion()
     
     # Draw the grid lines
     pyplot.grid(True)
     
     # Numbers from -50 to 50, with 0.1 as step
     xdomain = numpy.arange(-50,50, 0.1)
     
     # Plots a simple linear function 'f(x) = x'
     pyplot.plot(xdomain, xdomain)
     # Plots 'sin(x)'
     pyplot.plot(xdomain, numpy.sin(xdomain))
     
     # 'linear' is the default mode, so this next line is redundant:
     pyplot.xscale('symlog')
     pyplot.show()
'''


plt.show()
