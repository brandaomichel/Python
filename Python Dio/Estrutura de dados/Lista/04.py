qtnd = 0
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

for a in carros:
    qtnd += 1
    print(f"{qtnd}: {a}")