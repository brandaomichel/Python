a = 0
for i in range (1):
    awser = input('Telefonou para a vítima?')
    if awser == 's':
        a += 1
    awser = input('Esteve no local do crime?')
    if awser == 's':
        a += 1
    awser = input('Mora perto da vítima?')
    if awser == 's':
        a += 1
    awser = input('Devia para a vítima?')
    if awser == 's':
        a += 1
    awser = input('Já trabalhou com a vítima?')
    if awser == 's':
        a += 1

if a == 2:
    print('Suspeita')
elif a >= 3 and a <= 4:
    print('Cúmplice')
elif a == 5:
    print('Assassino')
else:
    print('Inocente')