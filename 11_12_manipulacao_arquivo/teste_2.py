import csv

with open ("/workspaces/algoritmosII/11_12_manipulacao_arquivo/Official Stats.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            print("Valor: " + str(linha))
