import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')
print(data)
print(data.loc['Roger'])

print(len(data.columns))
print(data.columns)
print(len(data.index))
print(data.index)
print(data.shape)

for indice, linha in data.iterrows():
    print(indice, linha[0], linha[1], linha[2])

for coluna in data:
    print(coluna)

print(data['Idade'])
print(data['Altura'])

for coluna in data:
    print(data[coluna])