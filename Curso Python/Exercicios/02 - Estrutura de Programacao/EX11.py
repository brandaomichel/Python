for numero in range(3, 31):
    e_primo = True

    for num_teste in range(2, numero):
        if numero % num_teste == 0:
            e_primo = False
            break

    if (e_primo):
        print("E primo", numero)
    else:
        print("O numero nao e primo", numero)