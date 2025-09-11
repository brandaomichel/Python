import matplotlib.pyplot as plt
import numpy as np

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 6, 8, 10])

# plt.bar(x, y, color='g', width=0.3)
# plt.show()

# y1 = np.array([1, 2 ,3])
# x1 = np.array(['Um', 'Dois' , 'Tres'])
# plt.barh(x1, y1, color='r', height=0.4)
# plt.title('Grafico de barras')
# plt.ylabel('Numeros')
# plt.xlabel('Valores')
# plt.show()

valores_left = np.arange(0, 6)
valores_right = np.arange(6, 0, -1)
xs = np.arange(6)

plt.bar(xs, valores_left, color='y')
plt.bar(xs, -valores_right, color='g')

plt.legend(['A', 'B'])
plt.title('Grafico de barras Dividido')
plt.ylabel('Valores Y')
plt.xlabel('Valores left x rigth')
plt.show()
# valores_left = np.arange(0, 6)
# valores_right = np.arange(6, 0, -1)
# ys = np.arange(6)

# plt.barh(ys, valores_left, color='y')
# plt.barh(ys, -valores_right, color='g')

# plt.legend(['A', 'B'])
# plt.title('Grafico de barras Dividido')
# plt.ylabel('Valores Y')
# plt.xlabel('Valores left x rigth')
# plt.show()