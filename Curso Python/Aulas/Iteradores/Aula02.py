class ColecaoNumeros:
    def __init__(self, numero_max):
        self.max = numero_max
    
    def __iter__(self):
        self.numero_atual = 1
        return self

    def __next__(self):
        if self.numero_atual <= self.max:
            retorno = self.numero_atual
            self.numero_atual += 1
            return retorno
        else:
            raise StopIteration

colecao = ColecaoNumeros(6)

for item in colecao:
    print(item)

iterador = iter(colecao)
print(next(iterador))
print(next(iterador))