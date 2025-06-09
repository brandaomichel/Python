class Teste:
    pass

minha_clasee = Teste()
#print(type(minha_clasee))

class NossaClasse:
    def __init__(self):
        print("Eu existo")

var = NossaClasse()
#print(type(var))

class Pessoa:
    especie = "Sapiens"
    num_pessoas = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.num_pessoas += 1
        print(f"Pessoa com nome {nome} e idade {idade} criados")

pessoa1 = Pessoa('Michel', 20)
pessoa2 = Pessoa('Ju', 30)
pessoa2 = Pessoa('Fatima', 30)

print(Pessoa.num_pessoas)

