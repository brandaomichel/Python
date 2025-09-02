import matplotlib.pyplot as plt
import numpy as np

font_props = {
    'family': 'arial',
    'color': 'blue',
    'weight': 'bold',
    'size': 8
}
font_props2 = {
    'family': 'arial',
    'color': 'green',
    'weight': 'bold',
    'size': 8
}

x= np.arange(-10, 10, 0.1)
y = x ** 2
plt.figure(figsize=(3.2,2.4))
plt.text(-5, 50, 'E uma parabola', fontdict=font_props2)
plt.xlabel('Vendas', fontdict=font_props)
plt.ylabel('Temperatura', fontdict=font_props)
plt.title('Vendas', fontdict=font_props)

plt.plot(x, y)
plt.show()