import numpy as np

array = np.array([4, 1, 3, 2])
print(np.sort(array))

array2 = np.array([[38, 2, 1], [5, 5, 4]])
print(np.sort(array2, axis=1))
print(np.sort(array2, axis=0))