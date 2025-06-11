class Formas_geometricas:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

class Quadrado(Formas_geometricas):
    lado = 10

class Triangulo(Formas_geometricas):
    angulo = 30

quadrado = Quadrado(100, 50)
triagulo = Triangulo(20, 30)

print(quadrado.altura)
print(quadrado.lado)
print(triagulo.altura)
print(triagulo.angulo)