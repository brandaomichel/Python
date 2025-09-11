import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2016, 2023)
y1 = np.array([3.15, 3.26, 3.88, 4.3, 5.33, 5.45, 5.39])

y2 = np.array([8710.5, 9928.5, 915191.58, 8897.29, 6795.32, 7500.21, 7542.34])

plt.subplot(1, 2, 1)
plt.xlabel('Ano')
plt.ylabel('Valor Real R$')
plt.title('Variacao Dolar x Real')
plt.bar(x, y1, color='b', width=0.7)

plt.subplot(1, 2, 2)
plt.xlabel('Ano')
plt.ylabel('PIB per Capita')
plt.title('Variacao Do Pib Per Capita')
plt.plot(x, y2, color='y', lw='3.5', ls='solid', marker='s', mfc='g')

plt.suptitle('Situacao Economica do Brasil')
plt.tight_layout()
plt.show()
