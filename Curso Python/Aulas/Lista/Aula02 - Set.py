lista_set = {1, 2, 3}
#print(lista_set)

lista_set2 = {1, 2, 3}
lista_set2.add(5)

#print(lista_set2)
lista_set2.remove(1)

#print(lista_set2)
#print(len(lista_set2))

lista = {1, 2, 3, 4, True, '2'}

for i in lista:
    print(i)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4}
set_union = set_1.union(set_2)
print(set_union)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4}
set_union = set_1.intersection(set_2)
print(set_union)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4}
set_union = set_2.difference(set_1)
print(set_union)