def meses_enum():
    meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    for i in enumerate(meses):
        yield i

for indice, mes in meses_enum():
    print(indice+1, mes)

