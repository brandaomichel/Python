class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

produtos = []

with open("Python/Curso Python/Exercicios/10 - XML - JSON - CSV/exercicio2.txt", 'rt') as file:
    for linha in file:
        indice_separa = linha.index("R$")

        nome = linha[:indice_separa - 1]
        valor = linha[indice_separa : len(linha) - 1]
        produto = Produto(nome, valor)

        produtos.append(produto)

for produto in produtos:
    print(produto.nome, produto.valor)