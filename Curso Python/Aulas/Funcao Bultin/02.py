numero = 70
caractere = chr(numero)
print(f'O numero {numero} e mapeado para o caractere {caractere}')

lista = []
for i in range(1, 100):
    caracter = chr(i)
    lista.append(caracter)
    print(i, '-', caracter)
print(lista)

caracterr = "F"
numero = ord(caracterr)
print(caracterr, '-' , numero)