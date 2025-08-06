import re

texto = 'aabbaabbbbbbaaccaa'

info = re.search('(aa|bb){2}', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')