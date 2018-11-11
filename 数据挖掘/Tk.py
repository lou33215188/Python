# -*- coding: utf-8 -*-
"""
Created on Fri May 18 22:22:51 2018

@author: 王磊
"""

import tkinter as tk
kdDict = ['申通快递', 'EMS邮政', '顺丰快递', '圆通快递', '中通快递', 
          '韵达快递', '天天快递', '汇通快递', '全峰快递', '德邦物流', '宅急送']
'''
root = tk.Tk()

root.title('快递查询系统')
var = tk.StringVar()
var.set('欢迎来到快递查询！')
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
textLabel = tk.Label(frame1, text='欢迎来到快递查询！',padx=10)
textLabel.pack(side=tk.LEFT)

button = tk.Button(frame2,text='选我！', command=callback)
button.pack()

frame1.pack()
frame2.pack()
'''
def callback():
     root1.destroy()
     print(var.get())
     root2 = tk.Tk()
     tk.Label(root2, text='v').grid(row=0, column=1)
     root2.mainloop()
root1 = tk.Tk()
root2 = tk.Tk()
'''
for key in kdDict:
     keyName.append(key)
     b = tk.Checkbutton(root, text=key, variable=keyName[-1])
     b.pack()


root.mainloop()
'''
var = tk.IntVar()
num = 0
for key in kdDict:
     num += 1
     radio = tk.Radiobutton(root1, text=key, variable=var, value=num, indicatoron=False)
     radio.pack(fill=tk.X)
button = tk.Button(root1, text='确定', command=callback)
button.pack()

root1.mainloop()
