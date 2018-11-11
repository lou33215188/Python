import tkinter as tk

def callback():
    var.set('吹吧你，我才不信呢')

root = tk.Tk()



frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

var = tk.StringVar()
var.set('FBI Warning！')
theLabel = tk.Label(
                frame1, 
                textvariable=var,
                justify=tk.LEFT)
theLabel.pack(side=tk.LEFT)

photo = tk.PhotoImage(file='D:\Python\ooxx\\19d36e9b17.gif')
imageLabel = tk.Label(frame1, image=photo)
imageLabel.pack()

theButton = tk.Button(frame2, text='我已满十八岁', command=callback)
theButton.pack()
frame1.pack()
frame2.pack()

root.mainloop()