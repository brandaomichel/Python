produtos = [['Carro', '200.000'], ['Cadeira', '1000'], ['Moto', '33000'], ['Geladeira', '2000'], ['Armario', '1500']]

for produto, valor in produtos:
    print(produto, valor)

def gen1():
    yield [1, 2]
    yield [3, 4]
    yield [5, 6]

for x, y in gen1():
    print(x, y)

def gen2():
    yield 1
    yield 2
    yield 3

def gen3():
    for i in gen2():
        yield i, 'a'
        yield i, 'b'
        yield i, 'c'

for x, y in gen3():
    print(x, y)