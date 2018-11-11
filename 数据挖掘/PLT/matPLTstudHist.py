import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)


# 直方图

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# 所有text()命令返回一个matplotlib.text.Text实例，像上面的线一样
# 可以通过关键字参数在text()定制文本样式，也可以通过setp()来定制文字的样式：

t = plt.xlabel('my data', fontsize=14, color='red')
plt.setp(t, color='blue')

plt.axis([40, 160, 0, 0.03])
plt.grid(True)
# 显示网格线
plt.show()
