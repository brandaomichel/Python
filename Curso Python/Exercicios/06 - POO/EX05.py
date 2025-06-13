class NumerpnEGATIVO:
    def __init__(self, numero):
        self.__numero = 0
        self.__numero = numero
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, value):
        if value <= 0:
            self.__numero = value
        
    def __lt__(self, outro):
        return self.__numero < outro.__numero

    def __gt__(self, outro):
        return self.__numero > outro.__numero

    def __sub__(self, outro):
        sub = self.__numero - outro.__numero
        if sub > 0:
            sub = 0
        return sub    

num1 = NumerpnEGATIVO(-10)
num2 = NumerpnEGATIVO(-20)
num3 = NumerpnEGATIVO(10)

print(num1.numero, num2.numero, num3.numero)
print(num1 > num2)
print(num1 - num2)