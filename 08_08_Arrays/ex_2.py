"""
Exercícios vetores(sem utilizar os métodos especiais):

2. Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine o somatório de todos os valores armazenados no vetor.
"""
import numpy as np

print("\nExercício 2:\n")

N = 5
X = np.zeros(N)
Soma = 0

for i in range(N):
    X[i] = input(f"Informe o {i+1}º valor: ")
    Soma += X[i]

print(f"\nA soma dos {N} valores é igual a {Soma}.\n")
