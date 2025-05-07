# 01
saldoConta = 5000
valorDivida = 2000

if saldoConta >= valorDivida:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")

# 02
cpf = '123.123.123-00'
senhaSistema = '123'
senhaUser = input('Informe a senha')
if senhaSistema == senhaUser:
    print(cpf)
else:
    print("Senha Invalida")

# 03
idade = int(input())

if idade <= 3:
    print('Bebe')
elif idade > 3 and idade <= 13:
    print('Crianca')
elif idade > 13 and idade <= 18:
    print('Adolecente')
elif idade > 18 and idade <= 65:
    print('Voce e adulto')
else:
    print('Idoso')

# 04
n1 = int(input('Primeiro Numero'))
n2 = int(input('Segundo Numero'))
operacao = input('Qual operacao: ')
if operacao == '+':
    print(n1 + n2)
elif operacao == "-":
    print(n1 - n2)
elif operacao == "*":
    print(n1 * n2)
elif operacao == "/":
    print(n1 / n2)