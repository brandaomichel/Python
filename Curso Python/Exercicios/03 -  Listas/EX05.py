lista = [x for x in range(1, 31)]
dia = int(input('Dia de nascimento: '))
lista.remove(dia)
print(f'Lista sem o dia do seu nascimento: {lista}')