import pandas as pd

dicionario = {
    'Nome': ['Roger', 'Cristiano', 'Paulo', 'Carlos'],
    'Idade': [45, 34, 56, 21],
    'Profissao': ['Engenheiro', 'Dev', 'Metalurgico', ' Medico']
}

data_frame = pd.DataFrame(dicionario)

print(data_frame)

dicionario2 = {
    'Idade': [45, 34, 56, 21],
    'Profissao': ['Engenheiro', 'Dev', 'Metalurgico', ' Medico']
}

data_frame2 = pd.DataFrame(dicionario2, index=['Roger', 'Cristiano', 'Paulo', 'Carlos'])
print(data_frame2)