#arquivo = open("exemplo.txt", "wt")
#arquivo.write("Teste de escrita dentro do arquivoso\n")
#arquivo.write('Esta e a segunda linha de teste')
#arquivo.close()

#lista = ['Michel', ' Juliana', ' Joao', 'Maria']
#arquivo = open("nomes.txt", 'wt')

#for i in lista:
    #arquivo.write(i + "\n")
#arquivo.close()

#texto = 'Ana\nMichel\nJuliana\n'
#arquivo = open('Nomes2.txt', 'wt')
#arquivo.writelines(texto)
#arquivo.close()

lista = [str(i) + ' \n' for i in range(0, 20)]
arquivos = open('Numeros.txt', 'wt')
arquivos.writelines(lista)
arquivos.close()