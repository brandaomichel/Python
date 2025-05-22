faz_soma = lambda x: x + 10
valor = faz_soma(2)
#print(valor)

multiplica = lambda x, y : x * y
mult = multiplica(5, 5)
#print(mult)

def multiplacaa(y):
    return lambda x: x * y

valor = multiplacaa(2)

print(valor(10))