# Faça um algoritmo que lê uma matriz M5X5 e crie 2 vetores(listas) SL (soma das linhas) e SC (soma das colunas) com 5 posições cada. Adicionar aos vetores o resultado da soma das linhas e das colunas da matriz, no final mostrar os dois vetores.

import numpy as np

N = 2

M1 = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        M1[l][c] = int(input(f"Informe valor para lin {l}, col {c}:"))

diag1 = M1[0][0] * M1[1][1]
diag2 = M1[0][1] * M1[1][0]

det = diag1 - diag2
print(det)