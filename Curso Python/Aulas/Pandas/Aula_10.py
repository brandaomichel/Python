import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

data.drop(columns=['Idade'], inplace=True)
print(data)

data.drop(columns=data.columns[[0, 1]], axis=1, inplace=True)
print(data)