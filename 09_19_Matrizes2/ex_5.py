# Faça um algoritmo que lê uma matriz M2X2 que calcula e mostra o resultado do determinante desta matriz.

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