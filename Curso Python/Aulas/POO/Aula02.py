class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def print_string(self, nome):
        print(f"Meu nome e {nome}")
    
    def print_nome(self):
        self.print_string(self.nome)

pessoa1 = Pessoa("Michel", 30)

pessoa1.print_nome()
