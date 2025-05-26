def achar_index(texto, letra):
    indices = []
    for i in range(len(texto)):
        if texto[i] == letra:
            indices.append(i)

    return print(indices)
print(achar_index("canivete", "e"))