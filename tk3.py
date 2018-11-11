from tkinter import *

root = Tk()
theLabel = Label(root, 
                text='FBI Warning！',
                justify=LEFT)
theLabel.pack(side=LEFT)

photo = PhotoImage(file='D:\Python\ooxx\\19d36e9b17.gif')
imageLabel = Label(root, image=photo)
imageLabel.pack()

thatLabel = Label(root,
                    text='请年满18周岁再看！',
                    image=photo,
                    compound=CENTER,
                    font=('宋体', 20),
                    fg='red',

                    )
thatLabel.pack(side=RIGHT)

root.mainloop()
