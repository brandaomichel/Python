import pandas as pd

data = {'Sede': ['Nova York', 'Sao Paulo', 'Nova York', 'Londres', 'Londres'],
        'Piloto': ['Mike Ross', 'Sebatian Thomas', 'Glen', 'Michael Schum', 'Luiz da Silva'],
        'Mundias': [10, 11, 0, 3, 44],
        'Vitorias': [321, 229, 12, 44, 1023]}

datta = pd.DataFrame(data, index=['XRacing', 'Equatorial', 'Typo', 'BlueRace', 'Capa Racing'])
# print(datta)

print(datta.loc['BlueRace']) # Ex 02

print(datta.loc['Capa Racing']['Mundias']) # Ex03

mask = datta['Mundias'] > 10 # Ex4

print(datta[mask]) #Ex4

mask2 = (datta['Mundias'] > 10) & (datta['Vitorias'] > 300)
print(datta[mask2])