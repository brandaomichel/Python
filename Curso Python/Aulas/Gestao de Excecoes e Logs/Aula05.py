print('Inicio')
lista = [1, 2, 3]

try:
    print(lista[1])
except IndexError as erro1:
    print('Erro de acesso ao indice ' + str(erro1))
except:
    print('Ocorreu outro erro')
else:
    print('Nao teve erro')

print('Fim')