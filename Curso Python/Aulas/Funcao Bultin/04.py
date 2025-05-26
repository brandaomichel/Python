lista = [5 ,6 , 1, 4, 0, 2]
lista.sort()
print(lista) 

lista.sort(reverse=True)
print(lista)

lista2 = ["a", "d", "x", "f", "m"]
lista2.sort()
print(lista2)

def sort_por_tamnho(item):
    return len(item)

lista = ["asdfq", "a", "b", "c", "ab", "ae", "asd"]
lista.sort(key=sort_por_tamnho)
print(lista)

lista = [5 ,6 , 1, 4, 0, 2]
lista.reverse()
print(lista)

produtos = [["carro", "R$ 1000.00"], ["cadeira", "R$ 300.00"], ["moto", "R$ 20.000"], ['Geladeira', "R$2.000"],
            ["armario", "R$1.500"]]

for produto, valor in produtos:
    print(produto, valor)

nomes = ('Joao', 'Carlos', 'Jose')
dic = dict.fromkeys(nomes, 10)
print(dic)