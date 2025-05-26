import math

a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

print(f"A solucao encontra e {x1} e {x2}")