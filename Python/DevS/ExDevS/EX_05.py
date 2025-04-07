fibo = int(input("Ate qual sequencia deseja calcular: "))

n1 = 1
n2 = 1

if fibo == 1 or fibo == 2:
    print("1")
else:
    for _ in range(2, fibo):
        elemento = n1 + n2
        n2 = n1
        n1 = elemento
        print(elemento)