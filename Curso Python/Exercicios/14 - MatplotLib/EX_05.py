import matplotlib.pyplot as plt
import numpy as np

paises = np.array(['China', 'USA', 'Italia', ' Outros'])
dados = np.array([30, 40, 20, 10])
cores = np.array(['b', 'y', 'g', 'r'])

edge_prop = {
    'linewidth': 1,
    'edgecolor': 'black',
    'linestyle': 'dashed'
}

text_pros = {
    'color': 'black',
    'style': 'oblique',
    'size': 13,
    'family': 'sans'
}

plt.figure(figsize=(7, 7))
plt.pie(dados, labels=paises, colors=cores, shadow=True, radius=0.8, startangle=90, autopct= lambda value: '%.2f %s' %(value, ' %'), textprops=text_pros)
plt.legend(paises, loc='lower right')
plt.tight_layout()
plt.show()