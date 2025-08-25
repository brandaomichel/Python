import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

data.drop(index=['Roger', 'Diego'], inplace=True)
print(data)

data.drop(index=data.index[[0, 1]], inplace=True)
print(data)

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

data.drop(index=data[data['Altura'] >= 1.7].index, inplace=True)
print(data)