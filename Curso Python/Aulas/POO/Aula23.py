from copy import copy
#lst1 = 10
#lst2 = lst1

#lst2 = 20
#print(lst1)

lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(20)
#print(lista1)

class Classe:
    def __init__(self):
        self.num = 10

class1 = Classe()
class2 = copy(class1)
class1.num = 20
print(class2.num)


lst1 = [1, 2, 3]
lst2 = copy(lst1)
lst2.append(10)
print(lst1)