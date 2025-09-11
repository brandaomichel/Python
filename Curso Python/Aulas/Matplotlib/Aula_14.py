import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75, 1.50, 1.46, 1.65, 1.74, 1.76, 1.80, 1.73, 1.89, 1.90])
plt.hist(alturas, color='r', bins = [1.40, 1.50, 1.60, 1.70, 1.80, 2])
plt.xlabel('Alturas')
plt.ylabel('Ocorrencias')
plt.title('Distribuicao das alturas')
plt.show()