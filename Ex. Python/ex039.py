num = 1
while num != 999:
    num = int(input("Numero: "))
    if num % 2 == 0:
        print(f'Numero: {num} é par')
    else:
        print(f'Numero: {num} é impar')