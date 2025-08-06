import re

texto = 'Texto teste'

info = re.search('(^[A-Za-z]+ +[AZa-z]+ *$)', texto)

if info != None:
    print('Enconcrato ocorrencia em', info.span())
    print('Oque foi encontrado', info.group())

else:
    print('Nao encontrado')