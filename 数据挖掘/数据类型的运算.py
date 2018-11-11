# -*- coding: utf-8 -*-
"""
Created on Tue May  8 00:04:03 2018

@author: 王磊
"""

import numpy as np
import pandas as pd

dataA = pd.DataFrame(np.arange(15, dtype=np.int).reshape(3,5))
dataB = pd.DataFrame(np.arange(20, dtype=np.float).reshape(4,5))

dataC = dataA + dataB
dataD = dataA.add(dataB, fill_value=100)

dataE = pd.Series(np.arange(10))
dataF = dataE + dataA

print(dataA)
print(dataB)
print(dataC)
print(dataD)
print(dataE)
print(dataF)