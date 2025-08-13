import re

texto = '95664433'

info = re.search("^([0-9){8})$", texto)

if info != None:
    print('Numero valido')
    info2 = re.search("^95([0-9]{6}$)", texto)
    if info2 != None:
        print('Telefone Bloqueado')
    else:
        print('Telefone Liberado')
else:
    print('Numero invalido')


