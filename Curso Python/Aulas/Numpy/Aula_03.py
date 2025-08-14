import numpy 

array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(array)
print(type(array))
print(array.dtype)

array2 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype=numpy.int8)
print(array2)
print(type(array2))
print(array2.dtype)

array3 = numpy.array(['1', '234', '3', '4'], dtype=numpy.str_)
print(array3)
print(type(array3))
print(array3.dtype)

array4 = numpy.array(['abc', 'def', 'ghi'], dtype= 'S3')
print(array4)
print(array4.dtype)
print(array4.itemsize)
print(array4.nbytes)

array5 = numpy.array([3, 2, 1], dtype= 'i2')
print(array5)
print(array5.dtype)
print(array5.itemsize)
print(array5.nbytes)