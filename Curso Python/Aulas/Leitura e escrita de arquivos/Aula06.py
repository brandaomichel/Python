import csv

class Pessoa:
    def __init__(self, id, nome, profissao):
        self.id = id
        self.nome = nome
        self.profissao = profissao

    @staticmethod
    def ler_pessoas():
        pessoas = []
        with open('pessoas.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo, delimiter=',')
            for linhas in leitor:
                pessoa = Pessoa(linhas[0], linhas[1], linhas[2])
                pessoas.append(pessoa)
        
        return pessoas

    @staticmethod
    def salva_pessoas(*pessoas):
        with open('pessoas.csv', 'w') as arquivo:
            escritor_csv = csv.writer(arquivo, delimiter=',')
            for pessoa in pessoas:
                escritor_csv.writerow([pessoa.id, pessoa.nome, pessoa.profissao])

pessoa1 = Pessoa(1, 'Michel', 'Dev')
pessoa2 = Pessoa(2, 'Jose', 'Eng.')
pessoa3 = Pessoa(3, 'Carlos', 'Dev')

Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3)

lista_pessoas = Pessoa.ler_pessoas()

for pessoa in lista_pessoas:
    print(pessoa.id, pessoa.nome, pessoa.profissao)