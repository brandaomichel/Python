import numpy

ponto_float = numpy.float64(1002.002)
ponto_float2 = numpy.float32(1002.002)

print(ponto_float, type(ponto_float))
print(ponto_float2, type(ponto_float2))

int8 = numpy.int8(20)
int16 = numpy.int16(1000)
uint8 = numpy.uint8(12)
uint16 = numpy.uint16(13)
float16 = numpy.float16(16)
print('-------------------------')
print(int8, type(int8))
print(int16, type(int16))
print(uint8, type(uint8))
print(uint16, type(uint16))
print(float16, type(float16))