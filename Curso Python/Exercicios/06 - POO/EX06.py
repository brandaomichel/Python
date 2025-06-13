def testa_objet(obj):
    if isinstance(obj, (int, float, str, bool)):
        print("Objeto por valor")
    else:
        print("Objeto por referencia")

class Objeto:
    def __init__(self):
        pass

obj = Objeto()
valor = 3

testa_objet(obj)
testa_objet(valor)