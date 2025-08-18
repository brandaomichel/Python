import numpy as np

def divide_abs(arr, n):
    arr = np.array_split(arr, n)
    arr = np.abs(arr)
    return arr

array1 = np.array([1, 2, 3, 4, -5, -6])
print(divide_abs(array1, 3))