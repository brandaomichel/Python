class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def inseri_idade(self, idade):
        self.idade = idade

pessoa = Pessoa('Michel')
pessoa.inseri_idade(30)

print(pessoa.idade)