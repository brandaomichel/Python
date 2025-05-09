array = []
array2 = list()

array_numero = [1, 2, 3]
array_floasts = [1.2, 5.3, -2.1]
array_str = ['a', 'b', 'c']
array_mist = ['A', 1, 2.3]
#print(array_numero)
#print(array_floasts)
#print(array_str)
#print(array_mist)

primeiro = array_numero[0]
#print(primeiro)
array_numero[0] = 2
primeiro = array_numero[0]
#print(primeiro)

array = [10, 2, 3]
#print(array)
array.append(2)
#print(array)
array.insert(2, '4')

#print(array)

array3 = [10, 2, 3, 20, '3']
#print(array3)
array3.remove(10)
#print(array3)
array3.pop(2)
#print(array3)
#print(len(array3))

array_t = [1, 'teste', 1.3, True]
#print(1 in array_t)
#print(False not in array_t)

#print(True not in array_t)

lista = [5, 6, 7, 2, 3, 4, 7]
teste = lista.count(7)
#print(teste)
pos = lista.index(7)
#print(pos)

lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
#print(lista1 + lista2)
mult = lista1 * 3
#print(mult)

numeros = ['um', 'dois', 'tres']
x,y,_ = numeros
#print(x)
#print(y)

cores = ['azul', 'preto', 'amarelo']

for x in cores:
    print(x)

cores = ['azul', 'preto', 'amarelo']

for i in range(0, len(cores)):
    print(cores[i])

listaa = [[1, 2, 3], [4, 5, 6]]
primeira_list = listaa[0]
segunda_list = listaa[1]
print(primeira_list)
print(segunda_list)
primeiro_elemento_primeira_list = listaa[0][0]
segundo_elemento_segunda_lista = listaa[1][1]
print(primeiro_elemento_primeira_list)
print(segundo_elemento_segunda_lista)