lista = [x for x in range(0, 10)]
print(lista)

lista2 = ['1', 'zero', 'quatro']
lista1 = [x for x in lista2]
print(lista1)

lista_par = [x for x in range(1, 11) if x % 2 == 0]
print(lista_par)

lista_aux = [1, 5, 9]
lista_x = [x for x in range(1, 11) if x not in lista_aux]
print(lista_x)

listax = [x for x in range(-10, 20) if x < 10 if x >= 0]
print(listax)

listaaz = [x * 2 for x in range(0, 11)]
print(listaaz)

listaazz = [str(x)[0] for x in range(0, 11)]
print(listaazz)

listaxx = ['negativo' if x < 0 else 'positivo' for x in range(-3, 4)]
print(listaxx)

lista_ar_impar = [str(x) + ' par' if x % 2 == 0 else str(x) + ' impar' for x in range(1, 11)]
print(lista_ar_impar)