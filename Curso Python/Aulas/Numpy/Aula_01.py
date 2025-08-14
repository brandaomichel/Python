import numpy

boolean =  numpy.bool_(True)
print(boolean)

string = numpy.str_("This is a text")
print(string)
print(type(string))

# Inn de 32 bits
inteiro = numpy.intc(-10)
print(inteiro)
print(type(inteiro))

# Int sem sinal
uinteiro = numpy.uintc(102)
print(uinteiro)
print(type(uinteiro))

# Int de 64 bits
long = numpy.int64(812738917)
print(long)
print(type(long))

#Int 64 sem sinal
ulong = numpy.uint(812738917)
print(ulong)
print(type(ulong))

