import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 20, 0.5)
y1 = np.cos(x1)

x2 = np.arange(0, 20, 0.5)
y2 = np.cos(x2) * 2

plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.title('Grafico de Vendas')

plt.plot(x1, y1, c='g', lw='6.5', ls='dashed', label='Vendas', alpha=0.5)
plt.plot(x2, y2, c='b', lw='3.5', ls='solid', label='Temperatura')
#best
plt.legend(loc='lower right')
plt.show()