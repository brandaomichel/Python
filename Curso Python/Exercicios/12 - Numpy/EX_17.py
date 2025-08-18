import numpy as np

def retorna_array(arr, inicial, final):
    filter_ = (arr >= inicial) & (arr <= final)
    return arr[filter_]

array = np.array([i for i in range(-10, 11)])
print(retorna_array(array, 5, 7))