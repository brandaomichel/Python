def conta_vogais(texto):
    vogais = 'a', 'e', 'i', 'o', 'u'
    qt_vogais = 0
    for a in range(len(texto)):
        if texto[a] in vogais:
            qt_vogais += 1
        


    return qt_vogais

print(conta_vogais('aaaaaaaaaa'))