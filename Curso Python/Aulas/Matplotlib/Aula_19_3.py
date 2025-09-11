import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
y = np.array([1, 4, 9, 12, 4, 7, 4, 9, 2, 1])
z = np.array([25, 70, 50])

z_indices = np.array([0, 2, 1, 1, 1, 0, 2, 2, 1, 1, 0])

cores = np.array(['r', 'r', 'g'])
z_cores = np.array([[0, 2, 1, 1, 1, 0, 2, 2, 1, 1, 0]])

plt.scatter(x, y, c=cores[z_cores], marker='o', s=z[z_indices])
plt.title('Grafico de dispersao')
plt.show()