def pai():
    def filho():
        print('Filho')
    filho()

#pai()

def calculadora(n1, n2, operador):
    
    def soma(a, b):
        return a + b
    def sub(a, b):
        return a - b
     
    if operador == "+":
        return soma(n1, n2)
    elif operador == "-":
        return sub(n1, n2)


#print(calculadora(1, 1, "-"))

def pega_func_print():
    def print_var(var):
        print(var)
    
    return print_var

print_me = pega_func_print()

print_me(10)

print(type(print_me))