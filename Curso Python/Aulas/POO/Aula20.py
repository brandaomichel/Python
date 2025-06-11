class Teste:
    def __init__(self, gasolina):
        pass

    @classmethod
    def class_method(cls):
        print(cls)
    
    @staticmethod
    def static_method():
        print("Static method")

Teste.class_method()
Teste.static_method()

testando = Teste("Aditivada")
testando.class_method()