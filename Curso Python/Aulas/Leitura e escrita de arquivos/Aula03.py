from os import path
import os

arquivo_existe = path.exists('exemplo.txt')

if arquivo_existe:
    print("O arquivos existe")
else:
    print('O arquivo nao existe')

os.remove('exemplo.txt')