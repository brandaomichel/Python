import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([2, 4, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 / array2)
print(array1 * array2)

array3 = np.array([[2, 4, 6], [1, 2, 4]])
array4 = np.array([[2, 4, 6], [1, 2, 4], [3, 4,5]])
print(array1 + array3)
print(array1 + array4)

array_1 = np.array([1, 2, 3])
print(array_1 + 2)

array_2 = np.array([10, 20, 30, 5])
array_3 = np.array([20, 40, 10, 5])
print(array_2 != array_3)
print(array_2 == array_3)
print(array_2 > array_3)

array_4 = np.array([10, 20, 30, 5])
array_5 = np.array([20, 40, 10, 5])
array_6 = np.array([20, 40, 10, 5])
print(np.array_equal(array_4, array_5))
print(np.array_equal(array_5, array_6))