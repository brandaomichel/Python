class Segredo:
    def __init__(self):
        self.__segredo = 'Senha123'
    
    def __printa_segrado(self):
        print(self.__segredo)

    def printa_segrado(self):
        self.__printa_segrado()

seg = Segredo()
seg.printa_segrado()