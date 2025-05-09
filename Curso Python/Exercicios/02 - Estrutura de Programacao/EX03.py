qtd_nume = 1
soma = 0
while qtd_nume < 6:
    num = int(input(f'Informe {qtd_nume} num: '))
    if num < 0:
        num = 0

    soma += num
    qtd_nume += 1

print(soma)