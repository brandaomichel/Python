class Natural:
    def __init__(self, numero):
        self.__numero = numero
    
    @property
    def numero(self):
        print('Pengando numero')
        return self.__numero

    @numero.setter
    def numero(self, value):
        if value >= 0:
            self.__numero = value
            print('Setando numero para ', value)

numero = Natural(10)
numero.numero = 20
print(numero.numero)
numero.numero = -1
print(numero.numero)