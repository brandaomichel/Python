def subtrai(n1, n2):
    return n1 - n2

sutratacao = subtrai(10, 3)

#print(sutratacao)

def comprimento(n):
    n = str(n)
    return len(n)

copri = comprimento('asd')
#print(copri)

def retona_multiplo(a, b, c):
    a += a
    b += b
    c += c
    return a, b, c

x, y, z = retona_multiplo(1, 2, 3)

print(x, y, z)

