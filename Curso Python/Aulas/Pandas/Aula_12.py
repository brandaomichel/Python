import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

data.loc['Willian'] = (25, 'Dev' , 1.75)
data.loc['Lando'] = (30, 'Dev', 1.80)
data.loc['Max'] = (22, 'Dev', 1.76)
data.loc['Sebastioa'] = (24, 'Dev', 1.67)
data.loc['Lucas'] = (21, 'Dev', 1.67)

print(data)

grupos = data.groupby('Profissão')

for indice, grupo in grupos:
    print(indice)
    print(grupo)

a = grupos.get_group('Dev')
print(a)

grupos = data.groupby(['Profissão', 'Idade'])
print(grupos.describe())