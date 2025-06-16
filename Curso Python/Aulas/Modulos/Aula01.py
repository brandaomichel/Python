import Aula01teste
#print(dir(Aula01teste))
print(Aula01teste.PI)
var = Aula01teste.Teste()
Aula01teste.My_Func(10)

from Aula01teste import PI
print(PI)

from Aula01teste import My_Func
My_Func('Teste')

from Aula01teste import PI as numpI
print(numpI)