import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe Baixa', 'Classe Media', 'Classe Alta'])
dados = np.array([10, 30, 80])
cores = np.array(['r', 'g', 'y'])

plt.figure(figsize=(7, 7))
plt.pie(dados, labels=classes,  colors=cores, shadow=True, startangle=90)
plt.title('Distriuicao de Classes')
plt.legend(classes, loc='upper right')
plt.show()