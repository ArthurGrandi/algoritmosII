"""
Exercícios vetores(sem utilizar os métodos especiais):

4. Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine o maior e o menor valor armazenado no vetor.
"""
import numpy as np

print("\nExercício 4:\n")

n = 5
x = np.zeros(n)

for i in range(n):
    x[i] = input(f"Informe o {i+1}º valor: ")

if i == 0:
    maior = x[i]
    menor = x[i]
else:
    if x[i] > maior:
        maior = x[i]
if x[i] < menor:
    menor = x[i]


print(f"\nO maior valor é {maior}")
print(f"O menor valor é {menor}\n")
