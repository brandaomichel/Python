nome = 'Michel'
idade = 8
profissao = 'analista'
linguagem = 'ecl'

print('Ola me chamao %s. tenho %d, trabalho com %s ' % (nome, idade, profissao))

nome = 'Michel'
idade = 8
profissao = 'analista'
linguagem = 'ecl'

print('Ola me chamao {}. tenho {}, trabalho com {} '.format(nome, idade, profissao))

nome = 'Michel'
idade = 8
profissao = 'analista'
linguagem = 'ecl'

print(f'Ola me chamao {nome}. tenho {idade}, trabalho com {profissao} ')

PI = 3.14159

print(f'Valor de Pi: {PI:.2f}')

print(f'Valor de Pi: {PI:10.2f}')


dados = {'name': "michel", "age": 29}

print('Nome: {name} Idade: {age}'.format(**dados))


