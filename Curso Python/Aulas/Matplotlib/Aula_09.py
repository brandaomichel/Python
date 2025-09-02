import matplotlib.pyplot as plt
import numpy as np

# print(plt.style.available)
x1 = np.arange(1, 100)
y1 = x1 ** 2

plt.style.use('dark_background')
plt.grid(c='gray')
plt.plot(x1, y1)
plt.show()