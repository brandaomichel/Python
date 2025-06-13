class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        print("pegando nome")
        return self.__nome
    
    def set_nome(self, nome):
        print("setando nome")
        self.__nome = nome
    
    def del_nome(self):
        print("Deletando nome")
        del self.__nome

    nome = property(get_nome, set_nome, del_nome)

instancia = Pessoa('Michel')

del instancia.nome