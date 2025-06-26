import csv

#with open("pessoas.csv", 'w') as arquivo:
#    escritorCsv = csv.writer(arquivo, delimiter=',')
#    escritorCsv.writerow(["id", "nome", "profissao"])
#    escritorCsv.writerow(["1", "Michel", "Analista"])
#    escritorCsv.writerow(["2", "Juliana", "Analista"])
#    escritorCsv.writerow(["3", "Maria", "Professora"])
#    escritorCsv.writerow(["4", "Fatimaa", "Tecnica"])

linhas = [["id", "nome", "profissao"], ["1", "Michel", "Analista"], ["2", "Juliana", "Analista"]]

# with open('pessoas2.csv', 'w') as file:
#     escritorCsv = csv.writer(file)
#      escritorCsv.writerows(linhas)

with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for i in leitor:
        print(i)