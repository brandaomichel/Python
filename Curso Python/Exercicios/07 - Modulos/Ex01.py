from random import randrange

numero = randrange(2, 100)

par_impar = 'par' if numero % 2 == 0 else 'impar'
print(f'o Numero {numero} e {par_impar}')