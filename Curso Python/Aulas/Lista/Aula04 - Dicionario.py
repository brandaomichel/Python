idades = {'Ana': 10, 'Clara': 20, 'joao': 34, 'fernanda': "ind"}
print(idades)

nome_numeros = {7.1: "Sete ponto um", 
                9.8: "nove ponto oito", 
                10.43: 'dez ponto quarenta e tres'}

print(nome_numeros)

print(idades['Clara'])

print(idades.get('fernanda'))

print(nome_numeros[7.1])

print('Ana' in idades)

idades['Ana'] = 30

print(idades['Ana'])

idades.pop('Ana')
print(idades)
idades.popitem()
print(idades)