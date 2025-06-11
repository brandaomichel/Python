class Veiculo:
    def __init__(self,nome, gasolina, potencia):
        self.nome = nome
        self.gasolina = gasolina
        self.potencia = potencia

    @classmethod
    def cria_carro(cls):
        return cls('Carro', 'Comun', 200)

    @classmethod
    def criat_trato(cls):
        return cls('trator', 'aditivada', 500)

veiculo1 = Veiculo.cria_carro()
veiculo2 = Veiculo.criat_trato()
print(veiculo1.nome)
print(veiculo2.nome)
print(veiculo2.gasolina)
