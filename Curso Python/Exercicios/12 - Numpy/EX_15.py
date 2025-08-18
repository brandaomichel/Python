import numpy as np

def is_negative(arr):
    return np.any(arr < 0)

array = np.array([1, 3, 4, 5, -2])
print(is_negative(array))