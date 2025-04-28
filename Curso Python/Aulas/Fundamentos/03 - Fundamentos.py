# %s Texto
# %d inteiro
# %f real

nome = "Ana"
text_formatado = "O nome dela e %s" % (nome)
print(text_formatado)

name = "Rodrigo"
idade = 33
altura = 1.73
texto = "Nome e %s, a idade e %d e a altura %.2f" %(name, idade, altura)
print(texto)

valor = True
print("O valor e %s" %(valor))
print("O valor e %d" %(valor))

deciaml = 23.4566
print("A parte inteira e %d" % (deciaml))

texto2 = "Hello, assim se quebra uma linha,\n\t entendeu?\n\t\t fim"
print(texto2)

texto3 = "Deixa a 'palavra' entre aspas"
print(texto3)