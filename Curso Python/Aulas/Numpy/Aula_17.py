import numpy as np

array = np.array([1, 3, 4, 2, 7, 4])
array_find = np.where(array >= 4)
array_find2 = np.where((array == 4) | (array == 7))
array_find2 = np.where((array == 4) | (array == 7))
array_find3 = np.any(array == 1)
array_find4 = np.any((array == 1) & (array < 10))
array_find5 = np.all(array > 0)
# print(array_find)
# print(array_find2)
# print(array_find5)
array1 = np.array([1, 0, 1, 1, 1, 0, 0])
filtera = array1 == 1
# print(array1[filtera])    
filtered_arrya = np.array([i for i in array1 if i == 0])
print(filtered_arrya)
