class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim plim")
    
    def para(self):
        print("Parando Bicicleta")
        print("Bicicleta Parada")
    
    def correr(self):
        print("Vrummmm")
    
    #def __str__(self):
    #   return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike1 = Bicicleta("Vermelha", "Caloi", 2022, 600)

bike1.buzinar()
bike1.correr()
bike1.para()
print(bike1.cor, bike1.modelo, bike1.ano)

bike2 = Bicicleta("Verde", "Monark", 2000, 800)
bike2.buzinar()
print(bike2)