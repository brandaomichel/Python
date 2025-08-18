import numpy as np 

arr1 = np.array([1, 2, 3, 4, 5, 6, 18])
arr2 = np.array([1, 2, 3, 4, 5, 6, 3])
arr3 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
arr4 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

array1 = np.add(arr3, arr4)
array2 = np.subtract(arr3, arr4)
array3 = np.multiply(arr3, arr4)
array4 = np.divide(arr3, arr4)
array5 = np.floor_divide(arr3, arr4)
array6 = np.power(arr1, arr2)
array7 = np.mod(arr1, arr2)
array8 = np.divmod(arr1, arr2)
array9 = np.sqrt(arr1)

arr10 = np.array([3.123127])
array_1 = np.around(arr10, 2)
array_2 = np.floor(arr10)
print(array_2)