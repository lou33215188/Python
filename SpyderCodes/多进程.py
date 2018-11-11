# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:28:09 2018

@author: 王磊
"""
from multiprocessing import Process
import os

def runproc(name):
     print('Run Child process %s (%s)' % (name, os.getpid))


def main():
     print('Parent process %d' % os.getpid())
     p = Process(target=runproc, args=('test'))
     print('Child Process will start')
     p.start()
     p.join()
     print('Child Process end')

if __name__ == '__main__':
     main()
     
