import numpy as np

array = np.array([1, 2, 3])
copy_array = array
copy_array[0] = 0
print(array)

array2 = np.array([1, 2, 3])
copy_2 = array2.copy()
print(array2)