from abc import ABC, abstractclassmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractclassmethod
    def ligar(self):
        pass
    
    @abstractclassmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
        print("TV Ligada")
    
    def desligar(self):
        print("Desligando TV...")
        print("TV Desligada")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar...")
        print("A Ligado")
    
    def desligar(self):
        print("Desligando Ar...")
        print("Ar Desligado")
    
    @property
    def marca(self):
        return "SAMSUNG"
    

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)
