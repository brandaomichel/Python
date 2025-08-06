import re
texto = '01234 ABC'

info = re.search("\w", texto)

if info != None:
    print("Encontada ocorrencia em: ", info.span())
    print("Oque foi encontrado: ", info.group())