import re

texto = 'existem 64 predios com 700 metros'

info = re.search('predios', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')