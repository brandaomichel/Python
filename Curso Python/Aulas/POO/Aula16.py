class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        print("Pegando nome")
        return self.__nome
    
    nome = property(get_nome)

pessoa = Pessoa('Michel')
print(pessoa.nome)
