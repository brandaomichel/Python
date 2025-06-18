def retorna_indice(lista, posicao):
    try:
        num = lista[posicao]
        return num
    except:
        return None
print(retorna_indice([1, 3, 2], 6))

