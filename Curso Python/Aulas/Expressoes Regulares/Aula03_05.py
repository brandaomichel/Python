import re

texto = 'Ola sou eu AQUI e nada para frente'

info = re.search('(.)*(AQUI)(.)*', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')