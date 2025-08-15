import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array = array.reshape(9)
print(array)

array2 = np.array([i for i in range(0, 27)])
print(array2)
print(array2)
array2 = array2.reshape(9, 3)
print(array2)
print(array2)
array2 = array2.reshape(3, 9)
print(array2)
print(array2)
array2 = array2.reshape(3, 3, 3)
print(array2)

array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array3 = array3.flatten()
print(array3)
