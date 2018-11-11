from tkinter import *

root = Tk()

var = IntVar()

radio1 = Radiobutton(root, text='one', variable=var, value=1)
radio2 = Radiobutton(root, text='two', variable=var, value=2)
radio3 = Radiobutton(root, text='three', variable=var, value=3)

radio1.pack()
radio2.pack()
radio3.pack()



root.mainloop()
