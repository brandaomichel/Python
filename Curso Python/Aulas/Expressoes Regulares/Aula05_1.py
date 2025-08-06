import re

texto = '99224466'

info = re.search('^99([0-9]{6})$', texto)

if info != None:
    print('Numero Valido')
else:
    print('Numero Invalido')