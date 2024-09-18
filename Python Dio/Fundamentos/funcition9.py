salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_au = lista.copy()
    lista_au.append(3)
    
    print(f'Lista auxiliar {lista_au}')
    salario += bonus
    return salario

lista = [1]
novo_sal = salario_bonus(500, lista)
print(novo_sal)
print(lista)
