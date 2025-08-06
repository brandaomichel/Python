import re

texto = '00123451'

info = re.search('1', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')
    