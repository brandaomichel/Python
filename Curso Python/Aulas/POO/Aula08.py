class Classe_Pai:
    def __init__(self):
        print('Sou a classe pai')
    
class Classe_Filha1(Classe_Pai):
    def __init__(self):
        print('Sou a classe Filha 1')

class Classe_Filha2(Classe_Pai):
    def __init__(self):
        print('Sou a classe Filha 2')

fai = Classe_Pai()
filha1 = Classe_Filha1()
filha2 = Classe_Filha2()