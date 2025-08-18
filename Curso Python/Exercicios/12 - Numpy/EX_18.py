import numpy as np

def ordena_impar_unicos(arr):
    arr = np.sort(arr)
    filterr = arr % 2 == 1
    return np.unique(arr[filterr])

array = np.random.randint(0, 10, (100))
print(ordena_impar_unicos(array))