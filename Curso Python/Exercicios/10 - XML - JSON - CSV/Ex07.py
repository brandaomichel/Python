import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def transformar_dic(*args):
        dicionario = dict()
        for pessoa in args:
            dicionario[pessoa.nome] = pessoa.idade
        
        return dicionario
    
pessoa1 = Pessoa("Carlos", 45)
pessoa2 = Pessoa("Eduardo", 23)
pessoa4 = Pessoa("Pedro", 12)

dic_pessoas = Pessoa.transformar_dic(pessoa1, pessoa2, pessoa4)
texto = json.dumps(dic_pessoas, indent=4)
print(texto)
with open('Exercicio7.json', 'wt') as arquivo:
    arquivo.write(texto)