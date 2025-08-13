import re

texto = '310 + 4453'

info = re.search('^ *(\d+ *(-|\+) *\d+) *$', texto)

if info != None:
    print('Conta valida')
else:
    print('Invalida')