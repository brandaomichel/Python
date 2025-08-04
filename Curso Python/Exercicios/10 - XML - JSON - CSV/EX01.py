lista = []
with open('Python/Curso Python/Exercicios/10 - XML - JSON - CSV/exercicio1.txt', 'rt') as file:
    for linhas in file:
        lista.append(linhas)

print(lista)