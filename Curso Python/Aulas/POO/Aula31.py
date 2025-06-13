class Veiculo:
    def __init__(self):
        pass
    
    def acelera(self):
        pass
    
class Moto(Veiculo):
    def __init__(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def re(self):
        print('Dando re')

def teste_re(var):
    if isinstance(var, Carro):
        var.re()
    else:
        print('Nao tem re')

moto = Moto()
carro = Carro()
teste_re(moto)
teste_re(carro) 