import csv

with open ("C:\\Users\arthu\Downloads\tabela_monstros.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter = ",")
    print(arquivo)