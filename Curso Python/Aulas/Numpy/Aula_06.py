import numpy as np

array1 = np.zeros(9)
array2 = np.ones(3)
array3 = np.empty(6)
array4 = np.identity(4)

print(array1)
print(array2)
print(array3)
print(array4)

array5 = np.zeros((3,3 ))
array6 = np.ones((4,4 ))

print(array5)
print(array6)

array7 = np.arange(9)
array8 = np.arange(4, 16)
print(array7)
print(array8)

array9 = np.arange(2, 16+1, 2)
print(array9)

array10 = np.full((4, 4), 10)
print(array10)

array_float = np.random.rand(4, 4)
array_int = np.random.randint(5, 10, (5, 5))
print(array_float, end='\n')
print(array_int)