import shutil

for i in range(0, 10):
    nome_pasta = 'pasta' + str(i)

    try:
        shutil.rmtree(nome_pasta)

    except:
        print('Falha ao exlcuir a pasta')
