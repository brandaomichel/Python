import re

texto = 'este notebook utiliza python'

info = re.search("python", texto)

if info != None:
    print('Encontro ocorrencia em: ', info.span())
    print('Numero encontrado : ', info.group())
else:
    print('Valor invalido')