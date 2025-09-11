import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe Baixa', 'Classe Media', 'Classe Alta'])
dados = np.array([10, 30, 80])
cores = np.array(['r', 'g', 'y'])
offsets = np.array([0.2, 0.03, 0.03])

bordas = {
    'linewidth': 1,
    'edgecolor': 'black',
    'linestyle': 'dotted'
}

text_props = {
    'color': 'black',
    'style': 'oblique',
    'size': 15
}

plt.figure(figsize=(7, 7))
plt.pie(dados, labels=classes,  colors=cores, shadow=True, startangle=90, radius=0.8, explode=offsets, wedgeprops=bordas, textprops=text_props, autopct= lambda value: '%.2f %s' % (value, '%'))
plt.title('Distriuicao de Classes')
plt.legend(classes, loc='upper right')
plt.show()