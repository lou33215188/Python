from tkinter import *

root = Tk()
var = IntVar()

check = Checkbutton(root, text='测试', variable=var)
check.pack()

label = Label(root, textvariable=var)
label.pack()



root.mainloop()
