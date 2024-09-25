class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal Voando")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")

# Exemplo Ruim de Heranca para "ganhar" o metodo voar
class Aviao(Passaro):
    def voar(self):
        print("Aviao esta decolando...")

def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())