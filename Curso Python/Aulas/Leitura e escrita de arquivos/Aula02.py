#with open('exemplo2.txt', 'wt') as arquivos:
#   arquivos.write('Teste')

#arquivo = open('Python\Curso Python\Aulas\Leitura e escrita de arquivos\exemplo.txt', 'rt')
#lido = arquivo.read()
#arquivo.close()
#print(lido)

arquivo = open('Python\Curso Python\Aulas\Leitura e escrita de arquivos\exemplo.txt', 'rt')
primeira_linhas = arquivo.readline()
segunda_linha = arquivo.readline()

print(primeira_linhas)
print(segunda_linha)

arquivo.close()

arquivo2 = open('Python\Curso Python\Aulas\Leitura e escrita de arquivos\exemplo.txt', 'rt')
for linha in arquivo2:
    print(linha)

arquivo2.close()

with open('Python\Curso Python\Aulas\Leitura e escrita de arquivos\exemplo.txt', 'rt') as file:
    for linha in file:
        print(linha)