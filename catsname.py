# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:36:39 2018

@author: 王磊
"""

catnames=[]
while True:
    print('Enter the name of cat ' +str(len(catnames)+1)+'(or enter nothing to    stop.):')
    name = input()
    if name=='':
        break
    print(len(catnames))
    catnames[len(catnames)]=catnames[len(catnames)] + [name]
print('The cat names are: ')
for name in catnames:
    print(' ' +name)
