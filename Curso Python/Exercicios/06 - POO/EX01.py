class Veiculos:
    def __init__(self, potencia, gasolina):
        self.potencia = potencia
        self.gaoslina = gasolina
    
carro1 = Veiculos(100, 200)
carro2 = Veiculos(200, 100)

print(f"Potencia do carro 1: {carro1.potencia} cavalos")
print(f'Alcance do carro 1: {carro1.gaoslina}')

print(f"Potencia do carro 2: {carro2.potencia} cavalos")
print(f'Alcance do carro 2: {carro2.gaoslina}')