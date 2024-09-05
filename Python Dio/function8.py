def somar(a, b):
    return a + b

def subtr(a, b):
    return a - b

def multi(a, b):
    return a * b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'o Resulado da op = {resultado}')

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtr)
exibir_resultado(10, 10, multi)

op = somar 

print(op(1,23))