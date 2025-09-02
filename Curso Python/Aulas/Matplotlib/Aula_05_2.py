import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = 5 * x + 1

plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.title('Grafico de vendas')
#solid, dashed, dotted, dashdot
plt.plot(x, y, c='g', linewidth='6.5', linestyle='dotted')
plt.show()