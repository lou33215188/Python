import easygui as g
import os


def show_file(file_name):
    lines = 0
    text = ""
    total = 0
    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "【%s】源文件%d个，源代码%d行" % (i, file_list[i], lines)
    title = "统计结果出来了喔~"
    msg = "主人，您当前总共写了%d行代码\n\
    完成进度为%.2f%%,请您继续努力，离十万行代码还差%d行" % (total, total/1000, 100000 - total)
    g.textbox(msg, title, text)


def calc_code(file_name):
    lines = 0
    global text
    with open(file_name) as f:
        text += ("正在分析文件%s......\n" % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass
    return lines


def search_file(file_dir):
    os.chdir(file_dir)
    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            lines = calc_code(each_file)  # 统计行数
            # 统计文件数 
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)


target = [".cpp", ".c", ".py"]
file_list = {}
source_list = {}
text = ""
g.msgbox("请主人选择要打开的文件夹", "代码量统计")
path = g.diropenbox("请主人选择您的代码库", "文件管理")
search_file(path)
path = g.diropenbox("请主人选择您的代码库", "文件管理")
search_file(path)
title = "文件正在分析中..."
msg = "分析内容如下:"
g.textbox(msg, title, text)
show_file(path)
