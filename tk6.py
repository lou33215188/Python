from tkinter import *

root = Tk()

Girls = ['苍井空', '武藤兰', '高坂桐乃', '我喜欢的人']

var = []

for eachGirl in Girls:
    var.append(IntVar())
    b = Checkbutton(root, text=eachGirl, variable=var[-1])
    b.pack(anchor='w')




root.mainloop()
