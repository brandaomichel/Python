class Veiculo:
    def __init__(self, marcha):
        self.marcha = marcha
    
    def aumentar_marcha(self):
        self.marcha += 1
        self.marcha = min(self.marcha, 5)
    
    def diminiu_marcha(self):
        self.marcha -= 1
        self.marcha = min(self.marcha, 1)

class Palio(Veiculo):
    def __init__(self, marcha):
        super().__init__(marcha)

class Golf(Veiculo):
    def __init__(self, marcha):
        super().__init__(marcha)
    def aumentar_marcha(self):
        self.marcha += 1
        self.marcha = min(self.marcha, 6)

carro = Palio(5)
carro.aumentar_marcha()
print(carro.marcha)

carro2 = Golf(4)
carro2.aumentar_marcha()
print(carro2.marcha)