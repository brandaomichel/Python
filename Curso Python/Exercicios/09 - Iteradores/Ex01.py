def meses():
     meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

     for i in meses:
          yield i

for mes in meses():
     print(mes)