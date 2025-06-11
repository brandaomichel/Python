class Base1:
    def __init__(self, atributo1):
        self.atribut1 = atributo1

    def Base1_print(self):
        print("Base1")

class Base2:
    def __init__(self, atributo2):
        self.atributo2 = atributo2

    def Base2_print(self):
        print("Base2")

class MinhaClasse(Base1, Base2):
    def __init__(self):
        Base1.__init__(self, 10)
        Base2.__init__(self, 20)

var = MinhaClasse()
print(var.atribut1)
print(var.atributo2)
var.Base1_print()
var.Base2_print()