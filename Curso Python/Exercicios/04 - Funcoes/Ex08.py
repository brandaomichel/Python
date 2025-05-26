def tipo(*args):
    for arg in args:
        print(type(arg))

print(tipo(1.1, 2, 3))