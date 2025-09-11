import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
y = np.array([1, 4, 9, 12, 4, 7, 4, 9, 2, 1])

plt.scatter(x, y)
plt.title('Grafico de dispersao')
plt.show()