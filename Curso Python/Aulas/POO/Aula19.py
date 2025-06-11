class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome.capitalize()
    
    @nome.setter
    def nome(self, value):
        if len(value) != 0:
            self.__nome = value

pessoa = Pessoa('rodrigo')
print(pessoa.nome)
pessoa.nome = 'fernando'
print(pessoa.nome)