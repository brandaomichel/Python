import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

data.loc['Roger', 'Idade'] = None
print(data)

print(data.isnull())
print(pd.isnull(data['Idade']))

mask = pd.notnull(data['Idade'])
print(mask)
print(data[mask])

copy = data.sort_values("Idade", ascending=True, inplace=False)
print(copy)

copy2 = data.sort_values('Idade', ascending=True, inplace=False, na_position='first')
print(copy2)

data.loc['Maria', 'Idade'] = 34

copy3 = data.sort_values(['Idade', 'Altura'], ascending=[True, True], inplace=False)
print(copy3)