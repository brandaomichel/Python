from copy import copy

class Classe:
    def __init__(self):
        self.num = 10

class1 = Classe()
class2 = copy(class1)
print(class2 is class1)