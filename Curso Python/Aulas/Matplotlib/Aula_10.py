import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 20, 0.5)
y1 = x1 * 2

x2 = np.arange(0, 20, 0.5)
y2 = np.sin(x2)

plt.subplot(1, 2, 1)

plt.title('A Primeira funcao')
plt.plot(x1, y1, c= 'green', lw= '6.5', ls='dashed')

plt.subplot(1, 2, 2)
plt.title('A Segunda Funcao')
plt.plot(x2, y2, c='red', lw='3.5', ls='solid')
plt.show()