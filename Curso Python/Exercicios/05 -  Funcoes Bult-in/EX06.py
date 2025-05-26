def encontra(texto):
    letra = input("Qual letra deseja achar: ")
    return texto.count(letra)

print(f"Encontrei a letra {encontra("banana")} ")