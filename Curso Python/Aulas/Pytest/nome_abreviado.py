abr = []
def abreviatura(nome):
    for i in range(len(nome.split())):
        abr.append(nome.split()[i][0])
    return ' '.join(abr)
