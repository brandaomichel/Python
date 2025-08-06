import re

texto = 'aa'

info = re.search('^(aa|bb)?$', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')