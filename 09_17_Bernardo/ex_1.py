import numpy as np

# perguntar ao usuário quantas posições terá seu array

arraySize = int(input("Quantas posições você deseja no seu array? \n"))

# inicializa o array

vetor = np.zeros(arraySize)

# perguntar o que ele quer em cada posição

for i in range(arraySize):
    vetor[i] = float(input(f"Qual valor você deseja inserir na posição { i + 1}? "))

# pedir ao usuário qual posição do array ele deseja imprimir

seePosition = int(input("Qual posição você deseja visualizar? "))

print(vetor[seePosition - 1])