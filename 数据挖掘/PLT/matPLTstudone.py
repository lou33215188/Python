import matplotlib.pyplot as plt


lines = plt.plot([0, 1, 2, 3], [1, 2, 3, 5], 'b-', linewidth=2.0)
# plot返回一个线对象(line_2d)列表
# 填入的是x,y轴坐标，对应的x值为[0, 1, 2, 3]
# 如果只有一个参数，则为y轴坐标
# 第三个参数为点格式
# linewidth 控制线的宽度

lines[0].set_antialiased(False)
# set_antialiased方法实现开启/去除平滑

plt.setp(lines, color='r', linewidth=2.0)
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)  # matlab风格
# setp()可以作用于一个列表对象或者是一个单一的对象。
# 你可以使用python风格的关键字参数或者是MATLAB风格的string/value对为参数
# line_2d对象具有的属性和取值,见OneNote:人工智能-数据挖掘

plt.ylabel("First numbers")
# 添加y轴标签

plt.axis([0, 6, 0, 10])
# axis规定 x 轴显示范围为 0-6  规定y轴显示范围为 0-10

plt.show()
