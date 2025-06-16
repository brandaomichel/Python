from random import randrange
'''Este modulo contem uma funcao que retorna uma lista de numero aleatorios que pode podem ser definidos'''
numeros = []
def get_random_final(incial, final, tam):
    '''Esta funcao retorna uma lista com numero aleatorios
    e recebe os parametros de entrada inicial numero minino que seja incluido na lista
    final numero maximo que sera acresentado na lista e tam tamanho da lista'''
    while len(numeros) < tam:
        num = randrange(1, 100)
        if min(num, incial) and num < max(num, final):
            numeros.append(num)

    return numeros