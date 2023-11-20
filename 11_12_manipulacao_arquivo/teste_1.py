import csv

with open ("/workspaces/algoritmosII/11_12_manipulacao_arquivo/Official Stats.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter = ",")
    print(arquivo)