def exibir_nome():
    print("Hello")

def exibir_nome2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_nome3(nome="Antonio"):
    print(f"Seja bem vindo {nome}")

exibir_nome()
exibir_nome2("Michel")
exibir_nome3()
exibir_nome3(nome="Chappie")