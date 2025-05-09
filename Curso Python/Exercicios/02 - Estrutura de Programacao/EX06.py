texto = 'Ola Mundo     '
num = 0
espaco = 0
while num != len(texto):
    if texto[num] == ' ':
        espaco += 1

    num += 1

print(espaco)