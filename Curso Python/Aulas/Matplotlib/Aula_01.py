import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)
# plt.show()

x1 = np.array([0, 1, 2, 3, 4])
y2 = x1 * 2

plt.plot(x1, y2)
# plt.show()

y3 = np.array([-2, 2, 10, 4, 5])
x3 = np.array(['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'])

plt.plot(x3, y3)
plt.show()