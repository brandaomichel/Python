import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
y = 5 * x + 1

plt.title('Funcao y = 5x + 1')
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

plt.plot(x, y, c='b',mfc='r', marker='s')
plt.show()