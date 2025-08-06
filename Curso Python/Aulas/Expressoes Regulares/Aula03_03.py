import re

texto = 'aaaaaaa'

info = re.search('^(aa){2,3}$', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')