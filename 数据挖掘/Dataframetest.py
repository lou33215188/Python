# -*- coding: utf-8 -*-
"""
Created on Mon May  7 23:13:19 2018

@author: 王磊
"""

import pandas as pd


dictOne = {'城市':['北京', '上海', '南京', '苏州', '无锡', '南通'],
           '人物':['习近平', 'Alice', '王磊', '程芷萱', '王镇', '吴佳昱'],
           '任务':['遗失的美好', '平生心愿', '少年行', '三山四海', '阴阳两界', '黑白路'],
           '经验值':[100, 1000, 1000000, 1000000, 10000, 10000]}

Test = pd.DataFrame(dictOne, index=[1,2,3,4,5,6,
                                    ])
