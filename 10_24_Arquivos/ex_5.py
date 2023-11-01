#Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deverá conter o maior número; e a última, o menor.

# Ler o conteúdo do arquivo "pares.txt" e armazená-lo em uma lista
with open("pares.txt", "r") as file:
    linhas = [int(line.strip()) for line in file.readlines()]

# Inverter a ordem das linhas
linhas = reversed(linhas)

# Escrever o conteúdo invertido no arquivo "pares_invertido.txt"
with open("pares_invertido.txt", "w") as file_invertido:
    for numero in linhas:
        file_invertido.write(str(numero) + "\n")

print("Arquivo 'pares_invertido.txt' criado com sucesso. A primeira linha contém o maior número e a última contém o menor.")