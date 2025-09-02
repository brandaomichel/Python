import matplotlib.pyplot as plt
import numpy as np

font_props = {
    'family': 'arial',
    'color': 'blue',
    'weight': 'bold',
    'size': 16
}
font_props2 = {
    'family': 'arial',
    'color': 'green',
    'weight': 'bold',
    'size': 18
}
# x = np.array([1, 2, 3, 4, 5])
# y = x * 2
# plt.xlabel('Vendas')
# plt.ylabel('Temperatura')
# plt.title('Grafico de Vendas', y=0.9, loc='left', x=0.01)
# plt.plot(x, y)
# plt.show()

x= np.arange(-10, 10, 0.1)
y = x ** 2
plt.text(-5, 50, 'E uma parabola', fontdict=font_props2)
plt.xlabel('Vendas', fontdict=font_props)
plt.ylabel('Temperatura', fontdict=font_props)
plt.title('Vendas', fontdict=font_props)

plt.plot(x, y)
plt.show()