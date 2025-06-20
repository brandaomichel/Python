lista = [1, 2, 3]
iterador = iter(lista)

while True:
    try:
        print(next(iterador))
    
    except:
        break