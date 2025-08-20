import pandas as pd

nomes = ['Michel', 'Lucas', ' Juliana', 'Maria']
data_Frame = pd.DataFrame(nomes)
# print(data_Frame)

numero = [['11', '12', '13', '14'], 
          ['11', '12', '13', '14'], 
          ['11', '12', '13', '14'], 
          ['11', '12', '13', '14']
          ]
dtf = pd.DataFrame(numero, columns=['a', 'b','c', 'd'], index=['x', 'y', 'z', 'w'])
print(dtf)