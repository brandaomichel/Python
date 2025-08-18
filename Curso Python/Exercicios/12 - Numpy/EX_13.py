import numpy as np

def positivo(arr):
    
    return len(np.where(arr > 0)[0])

array = np.array([1, 2, 3, 4, 5, 6, -2, -1, -3])
print(positivo(array))