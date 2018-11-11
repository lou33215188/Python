import easygui as fl
import os

file_path = fl.fileopenbox(default='*.py')

with open(file_path) as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】内容如下：" % title
    text = f.read()
    fl.textbox(msg.title, text)