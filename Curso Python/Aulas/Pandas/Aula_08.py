import pandas as pd

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')

data.loc['Carlos'] = (56, 'Engenheheiro', 1.76)
print(data)

data_adicional = pd.DataFrame({'Idade': [34, 21, 54],
                               'Profissão': ['Paraquedista', 'Professor', 'Cozinheiro'],
                               'Altura': [1.79, 1.76, 1.90]},
                               index=['Julia', 'Roberto', 'Jack']
                               )

data_adicional.index.name = 'Nomes'
print(data_adicional)

data = pd.concat([data, data_adicional])
print(data)

data = pd.read_csv('Python\Curso Python\Aulas\Pandas\pessoas.csv', index_col='Nome')
data['Sobrenome'] = None
print(data)

data['Sobrenome'] = ['Silva', 'Torres', 'Oliveira', '', '', '']
print(data)

data.insert(loc=1, column='Data Nascimento', value=['30/09/1994' for i in range(6)])
print(data)

