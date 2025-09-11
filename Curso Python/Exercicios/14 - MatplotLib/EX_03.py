import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2016, 2023)
y = np.array([3.15, 3.26, 3.88, 4.3, 5.33, 5.45, 5.39])

plt.title('Varial Dollar x Real')
plt.xlabel('Ano')
plt.ylabel('Valor do Real')

plt.bar(x, y, color='b')
plt.show()