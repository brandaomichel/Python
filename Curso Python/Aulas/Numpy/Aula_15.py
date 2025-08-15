import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array12 = np.concatenate((array1, array2), axis=0)
# print(array12)

array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[7, 7, 9], [10, 11, 12]])
array22 = np.concatenate((array3, array4), axis=0)
# print(array22)
array23 = np.concatenate((array3, array4), axis=1)
# print(array23)

array12r = np.vstack((array1, array2))
array12c = np.hstack((array1, array2))
# print(array12r)
# print(array12c)

array22r = np.vstack((array3, array4))
array33c = np.hstack((array3, array4))
print(array22r)
print(array33c)