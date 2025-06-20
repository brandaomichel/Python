texto1 = 'Ola'
print("#".join(texto1))

lista = ['a', 'b', 'c', 'd']
letras = ' '.join(lista)
print(letras)

letrass = '-'.join([str(i) for i in range(10)])
print(letrass)

def anos():
    for i in range(2020, 2030):
        yield str(i)

letra = '-'.join(anos())
print(letra)