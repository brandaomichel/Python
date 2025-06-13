class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.deleter
    def nome(self):
        print('Deletando nome')
        del self.__nome

istancia = Pessoa('Michel')
del istancia.nome
