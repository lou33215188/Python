# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:45:15 2018

@author: 王磊
"""

import requests  
import json
import tkinter as tk


def getInformation():
     typeid = kd_dict[var.get()]  
     postid = strVar1.get()
     url = 'http://www.kuaidi100.com/query?type=%s&postid=%s'%(typeid, postid)  
     rs = requests.get(url)  
     kd_info = json.loads(rs.text)  
     msg = kd_info['message']  
     if msg == 'ok':
          textInformation = kd_info

     else:  
          if msg == '参数错误':
               textInformation = '您输入信息有误，请重输：'  
          else:
               textInformation = msg
     return textInformation

def showInformation():
     textInformation = getInformation()
     root2.destroy()
     global root3
     root3 = tk.Tk()
     root3.title('快递查询')
     frame1 = tk.Frame(root3)
     frame2 = tk.Frame(root3)
     text = tk.Text(frame1)
     text.pack()
     if isinstance(textInformation, str):
          text.insert(tk.INSERT, textInformation)
     
     else:
          data = textInformation['data']
          for eachdata in data:
               time = eachdata['time']
               context = eachdata['context']
               outputStr = '时间:%s %s' % (time, context) + '\n'
               text.insert(tk.INSERT, outputStr)
     textButton = tk.Button(frame2, text='确定', command=root3.destroy)
     textButton.pack()
     
     frame1.pack()
     frame2.pack()
     root3.mainloop()
     
def inputId():
     global root2
     root2 = tk.Tk()
     global strVar1
     root2.title('快递查询')
     strVar1 = tk.StringVar()
     tk.Label(root2, text='请输入快递单号:').grid(row=0, column=0)
     e = tk.Entry(root2, textvariable=strVar1)
     e.grid(row=0, column=1)
     buttonStr = tk.Button(root2, text='确定', command=showInformation,)
     buttonStr.grid(row=1, column=0, columnspan=2)
     root2.mainloop()
     
def callback():
     root1.destroy()
     inputId()


def mainFunc():
     rootStart.destroy()
     global root1
     root1 = tk.Tk()
     root1.title('快递查询')
     root1.minsize(400, 300)
     keyNum = 0
     frame1 = tk.Frame(root1)
     global var
     var = tk.IntVar()
     frame2 = tk.Frame(root1)
     
     textLabel = tk.Label(root1, text='请选择您需要的快递公司:')
     textLabel.pack()
     
     for key in kdDict:
          keyNum += 1
          radio = tk.Radiobutton(frame1, text=key, variable=var, value=keyNum, indicatoron=False)
          radio.pack(fill=tk.X)
     tk.Button(frame2, text='确定', command=callback).grid(row=13,column=0)
     tk.Button(frame2, text='退出', command=root1.destroy).grid(row=13, column=1)
     frame1.pack()
     frame2.pack()
     root1.mainloop()

def start():
     global rootStart
     rootStart = tk.Tk()
     rootStart.minsize(300, 100)
     rootStart.title('快递查询')
     textLabel = tk.Label(rootStart, text='欢迎来到快递系统！\n点击确认即可进入')
     textLabel.pack()
     but = tk.Button(rootStart, text='进入', command=mainFunc)
     but.pack()
     rootStart.mainloop()

kdDict = ['申通快递', 'EMS邮政', '顺丰快递', '圆通快递', '中通快递', 
          '韵达快递', '天天快递', '汇通快递', '全峰快递', '德邦物流', '宅急送']
kd_dict = {1:'shentong',2:'ems',3:'shunfeng',4:'yuantong',5:'zhongtong',\
           6:'yunda',7:'tiantian',8:'huitong',9:'quanfeng',10:'debang',11:'zhaijisong'}  

start()




            

