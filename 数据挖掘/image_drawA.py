# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:53:18 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt

labels = 'Best','Great', 'Justsoso', 'bad'
explode = (0,0,0,0.1)
sizes = [20,30,50,100]

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False\
        ,startangle=90)

plt.title('Grade')
plt.axis('equal')
plt.show()
