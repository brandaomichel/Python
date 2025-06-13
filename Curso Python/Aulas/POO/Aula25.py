numero = 10
class Teste:
    def __init__(self):
        self.lista = [1, 2, 3]
    
    def __del__(self):
        print("Fui deletado")

teste = Teste()
del teste