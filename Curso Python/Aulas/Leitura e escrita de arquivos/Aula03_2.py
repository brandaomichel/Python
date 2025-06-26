#file = open('teste', 'w') 
#try:
#    file.write('hello world')
#finally:
#    file.close()

import os
try:
    os.remove('errrr')
except Exception as error:
    print('Ocorreu um erro: ' + str(error))