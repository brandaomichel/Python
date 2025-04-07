tab = int(input("Informe qual tabuada desejada: "))
n = 0

for i in range(1,11):
    result = i * tab
    print(f"{tab} X {i} = {result}")
