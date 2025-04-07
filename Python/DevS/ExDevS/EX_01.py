# EX01
soma = sum([10, 11, 12, 13, 14])

print(soma)

# EX02
media = (10 + 15 + 20) / 3

print(media)

# EX04

peso_1 = int(input('Informe o Peso 1: '))
nota_1 = int(input('Informe a nota 1: '))
peso_2 = int(input('Informe o Peso 2: '))
nota_2 = int(input('Informe o nota 2: '))

mediaFinal = (nota_1 * peso_1 + nota_2  *peso_2) / (peso_1 + peso_2)

print(f"A media final e {mediaFinal}")

# EX04

menor = min(100.20, 34.90, 31.50, 18.95)

print(menor)

# EX05

num = int(input("Digite um numero: "))
if num % 2 ==0:
    print(True)
else:
    print(False)

# EX06

temp = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (5 / 9) * (temp - 32)

print(f"A temperatura de {temp} Fahrenheit em Celsius {celsius:.2f}")