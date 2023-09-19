"""
Exercícios vetores(sem utilizar os métodos especiais):

5. Faça um algoritmo que lê 10 valores para uma variável do tipo vetor e mostre qual a posição está armazenado o maior e o menor valor no vetor.
"""

import numpy as np

print("\nExercício 5:\n")

n = 10
x = np.zeros(n)

for i in range(n):
    x[i] = input(f"Informe o {i+1}º valor: ")

    if i == 0:
        maior = x[i]
        maiorLoc = i
        menor = x[i]
        menorLoc = i
else:
    if x[i] > maior:
        maior = x[i]
        maiorLoc = i
    if x[i] < menor:
        menor = x[i]
        menorLoc = i


print(
    f"\nO maior valor ({maior}) está localizado na {maiorLoc+1}ª posição ({maiorLoc} no vetor).")
print(
    f"O menor valor ({menor}) está localizado na {menorLoc+1}ª posição ({menorLoc} no vetor).\n")
