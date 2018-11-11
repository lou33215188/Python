import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            )
# shrink - 收缩

plt.xscale('log')
# 还提供了对数(logarithmic)和分对数(logit)坐标。
# 当数据的维度跨越许多数量级时，这种坐标就很有用，改变坐标轴的刻度很容易

plt.ylim(-2, 2)
plt.show()
