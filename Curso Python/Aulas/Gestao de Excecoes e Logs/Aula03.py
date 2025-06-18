print("Inicio")
lista = [1, 2, 3]
try:
    print(lista[0])
except:
    print('Falha ao acessar, linha náo encontrada')
finally:
    del lista
    print("Execucao sempre que o try-execpt acabar, mesmo que nao ocorra erro")
print('Fim')