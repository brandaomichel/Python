print("Inicio")
lista = [1, 2, 3]
try:
    print(lista[10])
except:
    print('Falha ao acessar, linha náo encontrada')
else:
    print("Nao houve erro")
print('Fim')