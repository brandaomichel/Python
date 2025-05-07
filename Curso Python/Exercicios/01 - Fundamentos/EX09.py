# 01
nomeFull = 'Carlos Silva'
primeiroNome = nomeFull[0:7]
segundoNome = nomeFull[7:]
print(primeiroNome)
print(segundoNome)

# 02
text = input()
print(text[:-1])

# 03
palavra = input()
vogal =  ("a" in palavra) or ("e" in palavra) or ("i" in palavra) or ("o" in palavra) or ("us" in palavra)
print(f"A palavra {palavra} tem vogal : {vogal}")

#04
entrad = input()
saida = 'ABC' + entrad
print(saida)