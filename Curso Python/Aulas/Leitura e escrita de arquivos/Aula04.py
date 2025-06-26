import os 
#os.mkdir('Python\Curso Python\Aulas\Leitura e escrita de arquivos\steste')
#os.rmdir('Python\Curso Python\Aulas\Leitura e escrita de arquivos\steste')


#for i in range(0, 10):
#   nome_pasta = 'pasta' + str(i)
#    try:
#        os.mkdir(nome_pasta)
#    except:
#        pass
#
#    try:
#        open(nome_pasta + '/texto.txt', 'wt').close()
#    except:
#        pass

for i in range(0, 10):
    nome_pasta = 'pasta' + str(i)
    try:
        os.remove(nome_pasta + '/texto.txt')
    except:
        pass

    try:
        os.rmdir(nome_pasta)
    
    except:
        print('Falha ao remover a pasta', nome_pasta)