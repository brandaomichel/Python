def printa_positivo(numero):
   assert(numero > 0)
   print(numero)

try:
    print(printa_positivo(-1))
except AssertionError as error:
    print('O erro e ', str(error))

except Exception as erro1:
    print('Erro qualquer ' + str(erro1))
