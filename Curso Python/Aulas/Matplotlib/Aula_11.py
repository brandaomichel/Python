import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 20, 0.5)
y1 = np.cos(x1)

x2 = np.arange(0, 20, 0.5)
y2 = np.cos(x2) * 2

plt.subplot(2, 2, 1)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Primeira funcao coseno')
plt.plot(x1, y1, c='green', lw='6.5', ls='dashed', label='y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.subplot(2, 2, 2)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Primeira funcao coseno')
plt.plot(x1, y1, c='red', lw='6.5', ls='dashed', label='y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.subplot(2, 2, 3)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Segunda funcao coseno')
plt.plot(x2, y2, c='blue', lw='3.5', ls='solid', label='y=cos(x) * 2')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.subplot(2, 2, 4)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Segunda funcao coseno')
plt.plot(x2, y2, c='y', lw='3.5', ls='solid', label='y=cos(x) * 2')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

# plt.tight_layout()
# plt.subplots_adjust(top=1.1, wspace=0.4, hspace=1)
plt.subplots_adjust(hspace=0.8, wspace=0.4)
plt.suptitle('Meus Graficos')
plt.show()
