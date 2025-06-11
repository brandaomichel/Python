class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        print("Pegando nome")
        return self.__nome
    
    def set_nome(self, nome):
        if len(nome) > 0:
            print("Setando nome")
            self.__nome = nome

    nome = property(get_nome, set_nome)

pessoa = Pessoa('Michel')
print(pessoa.nome)
pessoa.nome = 'Marcos'
print(pessoa.nome)