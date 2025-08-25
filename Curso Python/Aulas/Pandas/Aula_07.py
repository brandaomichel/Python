import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

print(data)

data.at['Roger', 'Idade'] = 56
print(data)

data.iat[2, 0] = 35
print(data)

data.loc['Cristiano', 'Idade':'Profissão'] = (45, 'Dev')
print(data)

data.loc['Maria', ['Idade', 'Profissão']] = (65, 'Dev')
print(data)

data.iloc[0, 2] = 1.94
print(data)

data.loc[:, 'Idade'] = 76
print(data)

data.loc[:, 'Idade':'Profissão'] = None
print(data)

data.loc[:, ['Idade', 'Altura']] = (23, 1.8)
print(data)

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')
print(data)

data.loc[(data['Idade'] < 40), 'Altura'] = 1.99
print(data)

data.loc[(data['Idade'] == 34) & (data['Profissão'] == 'Programador'), ['Idade', 'Altura']] = (80, 1.00)
print(data)