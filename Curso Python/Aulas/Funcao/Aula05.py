def print_num(num):
    print(num)
    if num >= 10:
        return
    print_num(num + 1)

#print(print_num(0))

def print_str(texto, indice):
    if indice == len(texto):
        return
    print(texto[indice])
    print_str(texto, indice + 1)

#print_str("Python", 0)

def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)

print(fatorial(5))