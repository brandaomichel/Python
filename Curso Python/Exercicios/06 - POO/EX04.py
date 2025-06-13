class Veiculo:
    def __init__(self, peso, rodas, potencia):
        self.peso = peso
        self.rodas = rodas
        self.potencia = potencia
    
    def __lt__(self, outro):
        return self.potencia < outro.potencia
    
    def __gt__(self, outro):
        return self.potencia > outro.potencia
    
    def distancia(self):
        return (self.peso / self.potencia) * 1000

class Onibus(Veiculo):
    def __init__(self, peso, rodas, potencia):
        super().__init__(peso, rodas, potencia)
    

class Carro(Veiculo):
    def __init__(self, peso, rodas, potencia):
        super().__init__(peso, rodas, potencia)

class Moto(Veiculo):
    def __init__(self, peso, rodas, potencia):
        super().__init__(peso, rodas, potencia)

bus = Onibus(200, 6, 400)
carro = Onibus(300, 4, 100)
moto = Onibus(100, 2, 50)

print(bus > carro)
print(bus < moto)
print(bus < carro)