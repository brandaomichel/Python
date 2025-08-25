import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

print(data)

colunas = data.iloc[:,1:3]
print(colunas)

colunas2 = data.loc[:, "Idade": "Profissão"]
print(colunas2)

mask = data['Idade'] < 50
print(mask)

novo_df = data[mask]
print(novo_df)

df2 = data[(data['Idade'] > 40) & (data['Altura'] > 1.75)]
print(df2)