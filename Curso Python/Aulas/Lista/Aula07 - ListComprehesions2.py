lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = list(filter(lambda x: x % 2 == 0, lista))
print(lista)

lista_x = [[x for x in range(1, 5)] for y in range (1, 5)]
print(lista_x)

lista_y = [[str(x) + str(y) for x in range(1, 5)] for y in range (1, 5)]
print(lista_y)

lista_mul = [[str(x) + "*" + str(y) + "=" + str(x * y) for x in range (1,5 )] for y in range(1, 11)]
print(lista_mul)