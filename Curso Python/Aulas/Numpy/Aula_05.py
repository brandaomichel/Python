import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array)
print(array.ndim)
print(array.size)
print(len(array))
print(array.shape)
print(array.dtype)
print(array.itemsize)
print(array.nbytes)

tipo_pessoa = np.dtype([('nome', 'S10'), ('idade', 'i4')])

array2 = np.array([('Rodrigo', 23), ('Paulo', 30)], dtype=tipo_pessoa)
print(array2)
print(array2.ndim)
print(array2.size)
print(array2.shape)
print(array2.dtype)
print(array2.itemsize)
print(array2.nbytes)

