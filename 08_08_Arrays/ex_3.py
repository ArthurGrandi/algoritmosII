"""
Exercícios vetores(sem utilizar os métodos especiais):

3. Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine a média de todos os valores armazenados no vetor.
"""

import numpy as np

print("\nExercício 3:\n")

n = 5
x = np.zeros(n)
soma = 0

for i in range(n):
    x[i] = input(f"Informe o {i+1}º valor: ")
    soma += x[i]

media = soma/n

print(f"\nA média dos {n} valores é igual a {media}.\n")
