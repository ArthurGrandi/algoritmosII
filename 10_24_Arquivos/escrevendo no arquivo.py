arquivo = open ("aula.txt", "r")

linhas = arquivo.readline()

for linha in arquivo.readlines():
    print(linha)

arquivo.close