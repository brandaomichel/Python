import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])

# print(np.split(array, 2))
# print(np.split(array, 3))
array2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
print(np.split(array2, 2))

array_1 = np.array_split(array, 2)
array_2 = np.array_split(array, 3)
array_3 = np.array_split(array, 4)
# print(array_1)
# print(array_2)
# print(array_3)

array22 = np.array([[1, 2, 3], [4, 5, 6]])
array_11 = np.array_split(array22, 2)
array_22 = np.array_split(array22, 3)
array_33 = np.array_split(array22, 4)
# print(array_11)
# print(array_22)
# print(array_33)

array3x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arrayx = np.hsplit(array3x, 3)
print(arrayx)