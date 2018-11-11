import numpy as np
import matplotlib.pyplot as plt

arrayA = np.arange(0, 10, 0.02)
arrayYa = np.cos(arrayA)
arrayYb = np.sin(arrayA)
arrayYc = np.tan(arrayA)

plt.plot(arrayA,arrayYa,arrayA,arrayYb,arrayA,arrayYc)
plt.axis([0, 10, -4, 4])
plt.show()
