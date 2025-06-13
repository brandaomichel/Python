class Pessoa:
    def __init__(self, nome, cpf, depedente=None):
        self.nome = nome
        self.cpf = cpf
        self.depedente = depedente


pessoa1 = Pessoa('Michel', 123455)
pessoa2 = Pessoa('caralos', 12312312, '123')

print(f"Nome: {pessoa1.nome} CPF: {pessoa1.cpf} Depente: {pessoa1.depedente}")
print(f"Nome: {pessoa2.nome} CPF: {pessoa2.cpf} Depente: {pessoa2.depedente}")