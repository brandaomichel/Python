import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

print(data)
print(data.loc['Roger']['Idade'])
print(data.loc['Roger'][0])

print(data.loc['Roger'])
print(type(data.loc['Roger']))

print(data.iloc[0])
print(type(data.iloc[0]))


print(data.loc['Cristiano':'Jeferson'])
print(data.iloc[1:4])

print(data['Idade'])

idade = data['Idade']
print(idade[3])
print(idade[3])
print(idade['Diego'])

colunas = data[['Idade', 'Altura']]

print(type(colunas))