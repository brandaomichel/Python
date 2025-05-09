idades = {'Ana': 10, 'Clara': 20, 'joao': 34, 'fernanda': 20}
lista = idades.items()
print(lista)
for item in lista:
    print(item[0], item[1])

chaves = idades.keys()
valores = idades.values()

for item in chaves:
    print(item)
print('----')

for item in valores:
    print(item)

lista_nomes = list(idades.values())
pessoas20years = lista_nomes.count(20)
print(pessoas20years)

