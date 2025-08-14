import numpy as np

array = np.array([1, 2, 3, 4])
# for i in array:
#     print(i)

array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in array2:
    for j in i:
        print(j)
print('-------------------')
array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(array3, order='F'):
    print(x)