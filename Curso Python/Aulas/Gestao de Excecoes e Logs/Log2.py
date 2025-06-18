from Log import custom_logger

print('Inicio')
lista = [1, 2, 3]

try:
    print(lista[4])
except:
    custom_logger("error", 'Indice fora do range')