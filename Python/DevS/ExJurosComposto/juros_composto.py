from math import pow

def composto(capital, juros, tempo):
    return capital * pow((1 + juros), tempo)

def simple(capital, juros, tempo):
    return capital * juros * tempo

capital = float(input("Informe o valor Capital de investimento: "))
juros = float(input("Informe o juros anual em %: "))
tempo = int(input("Informe a quantidade de meses do investimento: "))
juros = juros / 100
tempo = tempo / 12

valor_final_composto = composto(capital, juros, tempo)
valor_final_simples = simple(capital, juros, tempo)
print(f'O Montante final dos juros composto e de R${valor_final_composto:.2f}')
print(f"Os Juros do rendimento foi de R${valor_final_composto - capital:.2f}")
print(f"O Montante final dos juros simples e de R${valor_final_simples }")