def recebe_strin(st1, st2):
    int1 = int(st1)
    int2 = int(st2)
    return int1, int2

try:
    print(recebe_strin('a', '1'))

except:
    raise Exception('Falha no casting')