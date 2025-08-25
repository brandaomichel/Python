import pandas as pd

data = {'Sede': ['Nova York', 'Sao Paulo', 'Nova York', 'Londres', 'Londres'],
        'Piloto': ['Mike Ross', 'Sebatian Thomas', 'Glen', 'Michael Schum', 'Luiz da Silva'],
        'Mundias': [10, 11, 0, 3, 44],
        'Vitorias': [321, 229, 12, 44, 1023]}

datta = pd.DataFrame(data, index=['XRacing', 'Equatorial', 'Typo', 'BlueRace', 'Capa Racing'])

datta.loc['Equatorial', 'Piloto'] = 'Antonio Racer' # EX06
print(datta)

datta.loc['XRacing', ['Sede', 'Vitorias']] = ('Sao Paulo', 322) # Ex 07
print(datta)

datta.loc['RedCow'] = ('Sao Paulo', 'Fernando Vetel', 0, 0) # Ex 08
print(datta)

print(datta.sort_values('Vitorias', ascending=False))

