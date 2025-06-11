class Base:
    def __base__privada(self):
        print("Pertenco somente a base")
    
    def _baseprotegidade(self):
        print('Pertcenco a base e quem me herdar')

class Filha(Base):
    def acessa_protegida(self):
        self._baseprotegidade()

filha = Filha()
filha.acessa_protegida()