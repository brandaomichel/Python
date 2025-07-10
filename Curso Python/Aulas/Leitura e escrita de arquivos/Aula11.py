import xml.etree.ElementTree as xml
import os

def cria_tag_pessoa(nome, cpf, sexo, endereco):

    no_pessoa = xml.Element("Pessoa", attrib={'Nome': nome})
    no_cpf = xml.SubElement(no_pessoa, 'CPF')
    no_cpf.text = cpf
    no_sexo = xml.SubElement(no_pessoa, 'Sexo')
    no_sexo.text = sexo
    no_endereco = xml.SubElement(no_pessoa, 'Endereco')
    no_endereco.text = endereco

    return no_pessoa

dados = {
    'Rodrigo': {
        'CPF': '12345678901',
        'Sexo': 'Masculino',
        'Endereco': 'Rua 1',
        'Idade': 23 
    },
    'Fernando': {
        'CPF': '987654321',
        'Sexo': 'Masculino',
        'Endereco': 'Rua 2',
        'Idade': 23,
        'Filhos': ['Rodrigo', 'Lucas'] 
    },
        'Ana': {
        'CPF': '987654321',
        'Sexo': 'Feminino',
        'Endereco': 'Rua 2',
        'Idade': 28
    }   
}

raiz = xml.Element("Dados pessoais")

for key in dados:
    nome = key
    dados_pessoa = dados[nome]
    cpf = dados_pessoa['CPF']
    sexo = dados_pessoa['Sexo']
    endereco = dados_pessoa['Endereco']
    #idade = dados_pessoa['Idade']
    pessoa = cria_tag_pessoa(nome, cpf, sexo, endereco)
    if 'Filhos' in dados_pessoa:
        filhos = xml.SubElement(pessoa, 'Filhos')
        for filho in dados_pessoa['Filhos']:
            pessoa_filho = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})

    raiz.append(pessoa)

arvore = xml.ElementTree(raiz)

with open('dados_pessoais.xlm', 'wb') as files:
    arvore.write(files)