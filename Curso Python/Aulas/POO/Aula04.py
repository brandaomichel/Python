class Tipo1:
    def __init__(self, outra_classe):
        self.outra = outra_classe
    
class Tipo2:
    numero = 10

classe2 = Tipo2()

classe1 = Tipo1(classe2)

print(classe1.outra.numero)

class Exemplo:
    def __init__(self):
        pass

lista = []
ex1 = Exemplo()
ex2 = Exemplo()

lista.append(ex1)
lista.append(ex2)

print(lista[0])