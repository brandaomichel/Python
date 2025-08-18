import numpy as np

array = np.random.randint(0, 10, (4, 9))

print(array.reshape((36)))
print(array.reshape((6,6)))