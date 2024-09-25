class Pessoa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano  = ano
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano


pessoa = Pessoa("Michel", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")