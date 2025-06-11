class Formas_geometricas:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def funcao_herdadae(self):
        print("Sou herdado")

class Quadrado(Formas_geometricas):
    pass

class Triangulo(Formas_geometricas):
    pass

quadrado = Quadrado(100, 50)
triagulo = Triangulo(20, 30)

quadrado.funcao_herdadae()