import re 

texto = '00:50'

infor = re.search("^([0-1][0-9]|[2][0-3]):[0-5][0-9]$", texto)

if infor != None:
    print('Horario Valido')
else:
    print('Horario invalido')