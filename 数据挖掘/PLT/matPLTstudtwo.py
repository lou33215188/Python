import numpy as np
import matplotlib.pyplot as plt

# MATLAB和pyplot都有当前图形(figure)和当前坐标系(axes)的概念。
# 所有的绘图命令都是应用于当前坐标系的。
# gca()和gcf()(get current axes/figures)分别获取当前axes和figures的对象。
# 通常，你不用担心这些，因为他们都在幕后被保存了
# 下面是一个例子，创建了两个子绘图区域(subplot)


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure("2subplot")
# figure的第一个参数是标题名字

plt.subplot(211)
# 211指从上到下分2分,从左到右分一分,选第一份。
# 以上两句可以不写，因为figure(1)和subplot(111)会被自动执行
# subplot()中的参数分别指定了numrows、numcols、fignum
# 其中fignum的取值范围为1到numrows*numcols
# 分别表示的是将绘图区域划分为numrows行和numcols列个子绘图区域，fignum为当前子图的编号。
# 编号是从1开始，一行一行由左向右编号的。
# 参数可以是1，1，1但是如果都是小于10的就可以省略

plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.axes([0.3, 0.4, 0.2, 0.3])
# axes可以灵活的调节所在的位置
# axes([left,bottom,width,height])

'''
text()命令可以被用来在任何位置添加文字，
xlabel()、ylabel()、title()被用来在指定位置添加文字。
'''

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title('这是一个标题', fontproperties='SimHei')
plt.show()

'''我们可以使用clf()和cla()(clear current figure/axes)清除当前figure和当前axes。
如果你创建了许多figures，你需要注意一件事：
figure的内存直到显示调用close()函数才会被完全释放，
否则它并没有被全部释放。
如果只是删掉对figure的引用，或者是通过关闭window进程管理器关闭该figure，
这都是不完全删除figure的，因为pyplot在内部维持了一个引用，直到close()被调用。'''
