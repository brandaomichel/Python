import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
array_sum = np.sum(array, axis=1)

array_1 = np.cumsum(array)
array_2 = np.cumprod(array, axis=0)
array_3 = np.cumprod(array, axis=1)

array2 = np.array([1, 2, 3, 4, 5, 6])
print(np.amin(array, axis=1))
print(np.amax(array, axis=0))
# print(np.abs(array))

