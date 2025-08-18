import numpy as np

def diviveis(arr):
    return np.where(arr % 3 ==0)[0]

array = np.array([4, 5, 6, 7, 8, 9])
print(diviveis(array))