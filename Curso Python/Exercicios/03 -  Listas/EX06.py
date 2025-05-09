objetov = {"teclado": "digitar",
           "mouse": "clicar"}

obj = input("Qual obejto desaja acessa: telclado ou mouse? ")

if obj in objetov:
    print(f'A funcao desse obejto e: {objetov[obj]}')
else:
    print("Objeto nao existe")