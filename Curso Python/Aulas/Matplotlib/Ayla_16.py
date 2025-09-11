import matplotlib.pyplot as plt
import numpy as np

altura_mundiais = np.random.normal(loc=175, scale=11, size=1000) / 100
altura_brasil = np.random.normal(loc=185, scale=9, size=1000) / 100

plt.hist(altura_mundiais, bins=7, color='b', alpha=0.5)
plt.hist(altura_brasil, bins=7, color='y', alpha=0.5)
plt.legend(['Altura Mundial', 'Altura Brasil'])
plt.xlabel('Alturas')
plt.ylabel('Ocorrencas')
plt.title('Distrubuicao de alturas')
plt.show()