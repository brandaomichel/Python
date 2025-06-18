class Caracter:
    def __init__(self, caracter):
        self.__caracter = ''
        self.__caracter = caracter
    
    @property
    def caracter(self):
        return self.__caracter

    @caracter.setter
    def caracter(self, value):
        if len(value) > 1:
            raise Exception('Caracter dever ter no maximo tamanho 1')
        
        self.__caracter = value
    
letra = Caracter("a")
print(letra.caracter)

try:
    letra.caracter = 'ab'
except Exception as ex:
    print(str(ex))