lista = ['a', 'b', 'c']

for indice, valor in enumerate(lista):
    print(indice, valor)

def anos():
    yield '2000'
    yield '2001'
    yield '2002'
    yield '2003'
    yield '2004'
    yield '2005'

for indice, valor in enumerate(anos()):
    print(indice, valor)

