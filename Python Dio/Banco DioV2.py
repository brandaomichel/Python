menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
LIMITE_DIARIO = 10

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Valor do Deposito: "))

        if valor > 0:

            saldo += valor
            extrato += f"Deposito no valor R${valor:.2f}"
            
        else:
            print("Valor invalido")
    
    elif opcao == "s":

        valor = float(input("Valor do Saque: "))

        if valor > saldo:
            print("Saldo Insuficiente!!")

        elif valor > limite:
            print("Limite Diario atingido")
        
        elif numero_saque >= LIMITE_SAQUE:
            print("Execedeu o limite de saque")

        elif valor > 0:
            saldo -= valor
            extrato += f"Deposito no valor R${valor:.2f}"
            numero_saque += 1

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Sem movimentacoes")
        else:
            print(f"\nSaldo R$ {saldo:.2fd}")
        print("\n=========================================")
    
    elif opcao == "q":
        
        break

    else:
        print("Opcoes invalidas, por favor selicione novamente a opcao desejada.")