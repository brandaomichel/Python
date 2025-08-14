import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(array)
array[0] = [10, 11, 12]
#print(array)
array[1, 1:3] = [0, 0]
#print(array)
array[0 , 0] = 101
#print(array)

array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2[:, 2] = [0, 0, 0]
print(array2)

array3 = np.array([1, 2, 3, 4])
array4 = np.append(array3, [5,6,7,8])
print(array4)

array5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array6 = np.append(array5, [[5, 6, 7]], axis=0) #Linha
array7 = np.append(array5, [[12], [6], [1]], axis=1) # coluna
print(array5)
print(array6)
print(array7)

array8 = np.array([1, 2, 3])
array_ = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array8 = np.insert(array8, 1, 10)
print(array8)

array9 = np.insert(array_, 1, [3, 3, 3], axis=0)

array10 = np.insert(array_, 1, [4, 4, 4], axis=1)
print(array9)
print(array10)

array9 = np.delete(array_, 1, axis=0)

array10 = np.delete(array_, 1, axis=1)
print(array9)
print(array10)
