lista = ["1", "1.2", "5", "10", "11.1", "123"]
decimal = []
for a in range(len(lista)):
    if lista[a].isdecimal():
        decimal.append(lista[a])

print(decimal)