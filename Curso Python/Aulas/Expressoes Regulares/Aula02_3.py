import re

texto = 'existem 64 predios com 700 metros'

info = re.findall('predios|metros', texto)

print(info)

text = 'ABCDefgHI123'

info2 = re.findall('[A-Z]|[0-9]', text)
print(info2)

info3 = re.search("^existem", texto)
if info3 != None:
    print('Encontrado ocorrencia em: ', info3.span())
    print('Oque foi econtradoÇ ', info3.group())

info4 = re.search("metros$", texto)
if info4!= None:
    print('Encontrado ocorrencia em: ', info4.span())
    print('Oque foi econtrado: ', info4.group())
