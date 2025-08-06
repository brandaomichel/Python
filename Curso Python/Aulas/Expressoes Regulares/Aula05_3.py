import re

texto = '22/09/1990'

info = re.search('^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]{4})', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')