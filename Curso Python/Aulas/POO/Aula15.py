class Veiculo:
    def __init__(self):
        self.__marcha = 1
    
    def aumenta_marcha(self):
        self.__marcha += 1
        self.__marcha = min(self.__marcha, 5)

    def diminui_marcha(self):
        self.__marcha -= 1
        self.__marcha = max(self.__marcha, 1)

    def marca_atual(self):
        return self.__marcha

carro = Veiculo()
carro.aumenta_marcha()
print(carro.marca_atual())
carro.diminui_marcha()
print(carro.marca_atual())
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
print(carro.marca_atual())