n1 = int(input('Qual numero deseja calcular o fatorial: '))
n2 = n1
for i in range(n1 - 1):
    n2 -= 1
    n3 = n1 * n2
    n1 = n3

print(n3)
