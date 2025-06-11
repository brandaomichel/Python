class Forma_Geometrica:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
class Quadrado(Forma_Geometrica):
    def __init__(self, altura, largura, atributo_quadrado):
        Forma_Geometrica.__init__(self, altura, largura)
        self.atributo_quadrado = atributo_quadrado

class Triangulo(Forma_Geometrica):
    def __init__(self, altura, largura, atributo_triangulo):
        super().__init__(altura, largura)
        self.atributo_triangulo = atributo_triangulo

quadrado = Quadrado(100, 200, 'quadrado')
triangulo = Triangulo(200, 300, 'Triangulo')

print(quadrado.altura)
print(quadrado.atributo_quadrado)
print(triangulo.largura)
print(triangulo.atributo_triangulo)