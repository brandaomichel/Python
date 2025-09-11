import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
y = np.array([1, 4, 9, 12, 4, 7, 4, 9, 2, 1])
z = np.array([100, 50, 150, 200, 100, 120, 130, 80, 90, 165])
cores = np.array(['r', 'r', 'g', 'b', 'b','r', 'y','brow', 'pink', 'gray'])
plt.scatter(x, y, c='b', marker='o', s=z)
plt.title('Grafico de dispersao')
plt.show()