import json

dicionario = None

with open('exemplo.json', 'rt') as arquivo:
    arquivo_lido = arquivo.read()
    dicionario = json.loads(arquivo_lido)

print(dicionario)
print(type(dicionario))
print(dicionario['Rodrigo']['Idade'])