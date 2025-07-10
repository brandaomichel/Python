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

raiz = xml.Element('DadosPessoais')
pessoa1 = cria_tag_pessoa('Michel', '12345678900', 'Masculino', 'Rua 2')
pessoa2 = cria_tag_pessoa('Maria', '12345678900', 'Feminino', 'Rua 3')
pessoa3 = cria_tag_pessoa('Carlos', '12345678900', 'Masculino', 'Rua 5')

raiz.append(pessoa1)
raiz.append(pessoa2)
raiz.append(pessoa3)

arvore = xml.ElementTree(raiz)

with open('dados_exemplo2.xlm', 'wb') as files:
    arvore.write(files)