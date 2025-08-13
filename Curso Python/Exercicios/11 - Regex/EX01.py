import re

texto = '25'

info = re.search("^([2][0-9])|([3][0-5])$", texto)

if info != None:
    print('Encontro ocorrencia em: ', info.span())
    print('Numero encontrado : ', info.group())
else:
    print('Valor invalido')