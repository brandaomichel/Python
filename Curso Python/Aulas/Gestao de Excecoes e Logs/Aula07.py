def printa_positivo(numero):
    if numero < 0:
        raise ValueError('Valor nao pode ser negativo')
    
    print(numero)

try:
    print(printa_positivo(-1))
except ValueError as error:
    print('O erro e ', str(error))

except Exception as erro1:
    print('Erro qualquer ' + str(erro1))
