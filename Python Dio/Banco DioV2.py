import textwrap
def menu():
    menu = """

    [d] Depositard
    [s] Sacar
    [e] Extrato
    [nu] Novo Cliente
    [nc] Nova Conta
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: {valor:.2f}'
        print("\nDeposito realizado com sucesso")
    else:
        print("\nDeposito falhou ! Vaor invalido")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Voce nao tem saldo suficiente.")

    elif excedeu_limite:
        print("Valor do saque excedeu o limite")

    elif excedeu_saque:
        print("Excedido Numero maximo de saques")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}"
        numero_saque += 1
        print("Saque realizado com sucesso")
    else:
        print("Operacao invalida.")

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nao foram realizado movimentacoes" if not extrato else extrato)
    print(f"\nSaldo R$ {saldo:.2f}")
    print("\n=========================================")

def criar_usario(usuarios):
    cpf = input("Informe o CPF (Somento numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Ja existe usuario cadastrado")
        return
    
    nome =  input("Informe seu nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereco: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contar(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta Criado com Sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario nao econtrado")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = [] 

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_contar(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "q":
            break
        
        else:
            print("Operacao invalida, selecione novamente")

main()