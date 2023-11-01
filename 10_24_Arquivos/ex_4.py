# Utilize os arquivos pares.txt e impares.txt gerados através do código-fonte, apresentado nos slides. Faça a leitura destes dois arquivos 
# e crie um só arquivo denominado de pareseimpares.txtcom base em todas as linhas dos dois arquivos lidos e para preservar a ordem numérica.

with open("pares.txt", "r") as file_pares:
    pares = [int(line.strip()) for line in file_pares.readlines()]

with open("impares.txt", "r") as file_impares:
    impares = [int(line.strip()) for line in file_impares.readlines()]

# Combine as listas e ordene-as
resultado = sorted(pares + impares)

# Escrever o resultado no arquivo "pareseimpares.txt"
with open("pareseimpares.txt", "w") as file_resultado:
    for numero in resultado:
        file_resultado.write(str(numero) + "\n")

print("Arquivo 'pareseimpares.txt' criado com sucesso.")