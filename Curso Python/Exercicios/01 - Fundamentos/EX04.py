# 01
ano_atual = 2025
ano_nascimento = 1994
idade = ano_atual - ano_nascimento
print(f"Idade {idade}")

# 02

n1 = 10
n2 = 20
n3 = 30
media = (n1 + n2 + n3) / 3
print(f"Media {media}")

# 03 IMC
peso = 80
altura = 1.65
imc = peso / (altura ** 2)
print(imc)

# 04
ovos = 11
pessoas = 4
ovos_sobram = ovos % pessoas
ovos_por_pessoa = (ovos - ovos_sobram) / pessoas
print(f'Para {pessoas} e {ovos}, sobram {ovos_sobram} para dividir por igual, cada pessoa recebe {ovos_por_pessoa:.0f} ovos')