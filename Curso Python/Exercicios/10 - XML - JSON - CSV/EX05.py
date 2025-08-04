import csv

def escreve_arquivo():
    with open('exercicio5.csv', 'w') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=',')
        escritor_csv.writerow(['Nome', 'Parentesco'])
        escritor_csv.writerow(["Pedro", "Avo"])
        escritor_csv.writerow(["Maria", "AvO"])
        escritor_csv.writerow(["Jose", "Pai"])
        escritor_csv.writerow(["Ana", "Mae"])
        escritor_csv.writerow(["Paulo", "Irmao"])

def ler_arquivo():
    with open('exercicio5.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            print(linha)
escreve_arquivo()
ler_arquivo()