from random import randint

n1 = int(input("Qual numero minimo do intervalo:\n"))
n2 = int(input("Qual numero maximo do intervalo:\n"))

tentativas = int(input("Quantas tentantivas para acertar:\n"))
numeroal = randint(n1, n2)
qntd_numero = []

while True:
    numero = int(input("Escolha um numero:\n"))
    qntd_numero.append(numero)
    tent = tentativas - len(qntd_numero)
    if len(qntd_numero) == tentativas:
        print(f"Todas tentativas falharam o numero correto seria: {numeroal}")
        break
    elif numero == numeroal:
        print('Parabens voce acertou !!!')
        break
    else:
        print(f'Numero errado tente novamente, voce tem {tent} tentativas')
