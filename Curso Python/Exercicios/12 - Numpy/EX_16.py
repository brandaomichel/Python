import numpy as np

def remove_negativo(arr):
    filter_ = arr >= 0
    return arr[filter_]

array = np.array([2, 3, 4, -1 , -2])
print(remove_negativo(array))