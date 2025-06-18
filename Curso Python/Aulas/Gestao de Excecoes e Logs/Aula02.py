print("Inicio")
lista = [1, 2, 3]
try:
    print(lista[10])
except Exception as error:
    print('Falha ao acessar, linha náo encontrada ' + str(error))
print('Fim')

try:
    numero = int('b')
except Exception as e:
    print("Falha no cast: " + str(e))