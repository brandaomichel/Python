import re

texto = 'Segunda-Feira'

info = re.search("^(Segunda-Feira|Terca-Feira|Quarta-feira|Quinta-Feira|Sexta-Feira|Sabado|Domingo)$", texto)

if info != None:
    print('Encontro ocorrencia em: ', info.span())
    print('Numero encontrado : ', info.group())
else:
    print('Valor invalido')