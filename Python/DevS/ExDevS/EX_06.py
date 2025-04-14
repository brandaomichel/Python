#0 01

def quadrado(qd=5):
    return qd * qd

print(quadrado(10))

def convert_celsius(fahrenheit):

    celsius = (5 / 9) * (fahrenheit - 32)

    return print(f"O valor convertido de fahrenheit para graus celsius: {celsius}")

faren = float(input("Informe o valor em Fahrenheit "))
convert_celsius(faren)

def calculo(quadrado, numero):

    if quadrado == "quadrado":
        return numero * numero
    
    elif quadrado == "cubo":
        return numero ** 3
    

num = int(input("Informe o numero: "))

soma = input("Quadro ou cubo: ")

print(calculo(soma, num))