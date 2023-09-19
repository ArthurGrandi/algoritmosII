"""
Exercícios vetores(sem utilizar os métodos especiais):

1. Faça um algoritmo que lê 10 valores para uma variável do tipo vetor de nome x e mostra os 10 valores armazenados na estrutura.
"""

import numpy as np

print("\nExercício 1:\n")

N = 10
x = np.zeros(N)

for i in range(N):
    x[i] = input(f"Informe o {i+1}º valor: ")

print("")

for i in range(N):
    print(f"O {i+1}º valor é {x[i]}")
