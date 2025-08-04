import csv

class Empresa:
    def __init__(self, id, nome, numero_funcionarios, lucro):
        self.id = id
        self.nome = nome
        self.numero_funcionarios = numero_funcionarios
        self.lucro = lucro
    
empresas = []

with open('Python/Curso Python/Exercicios/10 - XML - JSON - CSV/exercicio6.csv') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')

    for linha in leitor:
        emp = Empresa(linha[0], linha[1], linha[2], linha[3])
        empresas.append(emp)

for emp in empresas:
    print(emp.id, emp.numero_funcionarios, emp.lucro)