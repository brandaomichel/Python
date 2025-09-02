import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(1, 100)
y1 = x1 ** 2

plt.plot(x1, y1)
plt.grid(
    color='blue',
    linestyle='dotted',
    lw= 1.5,
    alpha=0.5
    )
plt.show()
