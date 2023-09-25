# Arrays e Listas:

# 1 - Crie um array/lista de números inteiros e encontre o maior valor.

import numpy as np

vetor = np.zeros(5)

for i in range(5):
    vetor[i] = int(input(f"Qual número você deseja preencher na posição V[{i}]? "))
    
maiorvalor = 0

for i in range(5):
    if (vetor[i] > maiorvalor):
        maiorvalor = vetor[i]

print(maiorvalor)