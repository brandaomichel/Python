import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 19)
y = -x ** 4
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Grafico da funcao y = - x ** 4')
plt.plot(x, y, color='orange', lw='1.5', marker='+')
plt.show()