print('Inicio')
lista = [1, 2, 3]
numero = 0
try:
    divisao = 10 / numero
    print(lista[10])
except IndexError as erro1:
    print('Erro de acesso ao indice ' + str(erro1))
except ZeroDivisionError as erro2:
    print('Erro de divisao por 0 ' + str(erro2))
except Exception as erro3:
    print('Ocorreu outro erro ' + str(erro3))
else:
    print('Nao teve erro')

print('Fim')