import numpy as np

arr1 = np.array([1, 2, 3, 4]) 
arr2 = np.array([3, 4, 5, 6, 7]) 
arr3 = np.array([3,3 , 4, 5, 4, 5, 6, 7]) 
new_array_1 = np.union1d(arr1, arr2)
new_array2 = np.intersect1d(arr1, arr2)
new_array3 = np.unique(arr3)
print(new_array3)

