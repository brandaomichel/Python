class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe....")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe")

    def falar(self):
        print('Au')

def criar_cachorro():
    c = Cachorro("Dog", "Branco", False)
    print(c.nome)

c = Cachorro("Chappie", "Amarelo")
c.falar()

print("Python")

del c 

print("Python")
print("Python")
print("Python")
# criar_cachorro()

