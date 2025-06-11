class Veiculo:
    __numero_veiculos = 0
    def __init__(self,nome, gasolina, potencia):
        self.nome = nome
        self.gasolina = gasolina
        self.potencia = potencia
        Veiculo.__numero_veiculos += 1

    @staticmethod
    def get_num_carros():
        return Veiculo.__numero_veiculos

carro = Veiculo("Carro", "Gas", 200)
carro2 = Veiculo("Caminhao", "Disesl", 1000)
print(Veiculo.get_num_carros())
print(carro2.get_num_carros())