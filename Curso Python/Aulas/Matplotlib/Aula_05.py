import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.5)
y = x ** 6

plt.plot(x, y, color='Yellow')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('A funcao x = y = x **6')
plt.show()