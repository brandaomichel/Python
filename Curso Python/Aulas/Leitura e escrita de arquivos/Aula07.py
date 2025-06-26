import json

# idades = {'Michel': 30, 'Ju': 32, 'Pedro': 18}

# print(json.dumps(idades, ensure_ascii=False))
# print(json.dumps([1, 2, 3, 4, 5]))

dados_pessoas = {
    'Rodrigo': {
        'CPF': 12345678901,
        'Sexo': 'Masculino',
        'Endereco': 'Rua 1',
        'Idade': 23 
    },
    'Fernando': {
        'CPF': 987654321,
        'Sexo': 'Masculino',
        'Endereco': 'Rua 2',
        'Idade': 23,
        'Filhos': ['Rodrigo', 'Lucas'] 
    }   
}

texto = json.dumps(dados_pessoas, indent=4)

print(texto)

with open('exemplo.json', 'wt') as arquivo:
    arquivo.write(texto)
    