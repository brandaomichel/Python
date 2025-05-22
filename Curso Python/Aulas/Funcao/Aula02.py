def func(valor, nome = "Teste"):
    print(nome, valor)

#func(3, "asd")

def funcao(**args):
    print(type(args))
    print(args)
    print(args['Valor'])

#funcao(Valor = '10', operacao = 'soma', resultado = 10)

def printa(x):
    print(x)

def executa(func, x):
    func(x)

minha_funcao = printa
print(type(minha_funcao))

executa(minha_funcao, 10)