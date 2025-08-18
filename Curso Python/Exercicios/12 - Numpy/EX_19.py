import numpy as np

def ordena_impar(arr):
    arr = np.sort(arr)
    filterr = arr % 2 == 1
    return arr[filterr]

array = np.random.randint(0, 10, (100))
print(ordena_impar(array))