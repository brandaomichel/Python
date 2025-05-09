dados_maria = {
    'sexo': 'F',
    'cpf': '123.123.123-10',
    'rg': '12345612'
}

dados_joao = {
    'sexo': 'M',
    'cpf': '321.654.987-10',
    'rg': '1234444'
}

dados_ana = {
    'sexo': 'F',
    'cpf': '098.987.876-12',
    'rg': '12309887'
}

dados_por_nome = {
    'ana': dados_ana,
    'maria': dados_maria,
    'joao': dados_joao
}

print(dados_por_nome['maria']['cpf'])
print(dados_por_nome['joao']['sexo'])

dados_por_nome2 = {
    'ana': {
      'sexo': 'M',
      'cpf': '321.654.987-10',
      'rg': '1234444'
    },
    'maria': {
        'sexo': 'F',
        'cpf': '12312312312',
        'rg': '12312123'
    },
    'joao': {
        'sexo': 'M',
        'cpf': '123123123',
        'rg': '123123123'
    }
}

print(dados_por_nome2)

print(dados_por_nome2['ana']['rg'])