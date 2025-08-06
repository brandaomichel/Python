import re

texto = 'xxxxxxxxxx'

info = re.search('^x{7,}$', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')