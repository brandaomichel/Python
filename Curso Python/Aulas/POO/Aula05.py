class Formas_geometricas:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

class Quadrado(Formas_geometricas):
    pass

class Triangulo(Formas_geometricas):
    pass

quadrado = Quadrado(100, 50)
triagulo = Triangulo(20, 30)

print(quadrado.altura)
print(triagulo.altura)