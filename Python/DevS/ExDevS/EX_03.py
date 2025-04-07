# Ex01

numero = int(input("Digite o numero que deseja o fatorial: "))
n1 = 1

while numero > 0:
    
    n2 = numero
    n3 = n1 * n2
    n1 = n3
    numero = numero - 1

print(n1)

# Ex 02
senha = 9183
tentiva = 3
while tentiva != 0:
    tentiva -= 1
    senha_user = int(input("Digite a senha: "))
    if senha_user == senha:
        print("Acesso concedido")
        break
    else:
        print(f"Senha Invalida resta {tentiva} tentativas")