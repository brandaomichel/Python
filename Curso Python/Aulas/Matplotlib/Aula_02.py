import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1, 2, 3, 4, 5])
y1 = x1 * 2

x2 = np.array([5, 10, 15])
y2 = x2 + 2
# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.show()

x3 = np.arange(1, 10)
y3 = x3 * 2

x4 = np.arange(1, 10)
y4 = x4 ** 2

# plt.plot(x3, y3)
# plt.plot(x4, y4)
# plt.axis([0, 10, -1, 50])
# plt.show()

x1 = np.arange(1, 10)
y1 = x1 * 2

x2 = np.arange(1, 10)
y2 = x2 ** 2

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlim(0,10)
plt.ylim(-1,50)
plt.show()