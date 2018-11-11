# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:45:15 2018

@author: 王磊
"""

import requests  
import json
import tkinter as tk
from useragents import USER_AGENTS
import random


def getInformation():
     headers = {"User-Agent" : random.choice(USER_AGENTS)
                  }
     typeid = kd_dict[var.get()]  
     postid = strVar1.get()
     url = 'http://www.kuaidi100.com/query?type=%s&postid=%s'%(typeid, postid)  
     rs = requests.get(url, headers=headers)  
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
     tk.Button(frame2, text='确定', command=root3.destroy).grid(row=0, column=0,
              ipadx=30,ipady=10)
     tk.Button(frame2, text='继续查询(同一公司)', command=root3returninput).grid(row=0,
              column=1, ipadx=40, ipady=10)
     tk.Button(frame2, text='继续查询(不同公司)', command=root3returnmain).grid(row=0,
              column=2, ipadx=40, ipady=10)
          
     frame1.pack()
     frame2.pack()
     root3.mainloop()
     
def inputId():
     global root2
     root2 = tk.Tk()
     global strVar1
     root2.title('快递查询')
     strVar1 = tk.StringVar()
     tk.Label(root2,text='您选择的是%s' % kdDict[var.get()-1]).grid(row=0,column=0,columnspan=2)
     tk.Label(root2, text='请输入快递单号:').grid(row=1, column=0)
     e = tk.Entry(root2, textvariable=strVar1)
     e.grid(row=1, column=1)
     tk.Button(root2, text='确定', command=showInformation,).\
     grid(row=2, column=0, ipadx=20)
     tk.Button(root2, text='返回', command=root2returnmain).grid(
               row=2, column=1, ipadx=20)
     root2.mainloop()
     
def callback():
     root1.destroy()
     inputId()

def callmain():
     rootStart.destroy()
     mainFunc()

def root2returnmain():
     root2.destroy()
     mainFunc()

def root3returninput():
     root3.destroy()
     inputId()

def root3returnmain():
     root3.destroy()
     mainFunc()

def mainFunc():
     global root1
     root1 = tk.Tk()
     root1.title('快递查询')
     root1.minsize(300, 200)
     keyNum = 0
     frame1 = tk.Frame(root1)
     global var
     var = tk.IntVar()
     frame2 = tk.Frame(root1)
     
     textLabel = tk.Label(root1, text='请选择您需要的快递公司:')
     textLabel.pack()
     
     for key in kdDict:
          keyNum += 1
          if keyNum == 11:
               tk.Radiobutton(frame1, text=key, variable=var, value=keyNum, indicatoron=False)\
               .grid(row=(keyNum-1)//2, column=0, columnspan=2, ipadx=80,ipady=10)
          else:
               tk.Radiobutton(frame1, text=key, variable=var, value=keyNum, indicatoron=False)\
               .grid(row=(keyNum-1)//2, column=(keyNum-1)%2, ipadx=30,ipady=10)
     tk.Button(frame2, text='确定', command=callback).grid(row=13,column=0,ipadx=30,ipady=10)
     tk.Button(frame2, text='退出', command=root1.destroy).grid(row=13, column=1,ipadx=30,ipady=10)
     frame1.pack()
     frame2.pack()
     root1.mainloop()

def start():
     global rootStart
     rootStart = tk.Tk()   
     rootStart.minsize(100, 150)
     rootStart.title('快递查询')
     
     
     tk.Label(rootStart, text='欢迎来到快递系统！点击确认即可进入').grid(row=0,
             column=0)
     tk.Label(rootStart, text='作者:王磊 吴佳昱 程芷萱\n专业:电子信息工程\n班级:1701').grid(row=1,
             column=0) 
     tk.Button(rootStart, text='进入', command=callmain).grid(row=2,column=0,ipadx=30,ipady=10)
     rootStart.mainloop()

kdDict = ['申通快递', 'EMS邮政', '顺丰快递', '圆通快递', '中通快递', 
          '韵达快递', '天天快递', '汇通快递', '全峰快递', '德邦物流', '宅急送']
kd_dict = {1:'shentong',2:'ems',3:'shunfeng',4:'yuantong',5:'zhongtong',\
           6:'yunda',7:'tiantian',8:'huitong',9:'quanfeng',10:'debang',11:'zhaijisong'}  

start()




            

