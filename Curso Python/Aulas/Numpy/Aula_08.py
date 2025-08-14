import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array[0])
print(array[2:4])

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
print(matriz[2])
print(matriz[2][2])
print(matriz[2, 1])
print(matriz[1:3, :2])
print(matriz[1, 0:3])
print(matriz[2, :])
print(matriz[:, 2])

matriz2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(matriz2[1, :])
print(matriz2[:, 1])

matriz3 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 19], [19, 20, 21, 22, 23, 24, 25 , 26, 27]])

print(matriz3)
print(matriz3[1, 1:5])
print(matriz3[1, 0:8:2])