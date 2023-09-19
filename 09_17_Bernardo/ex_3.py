# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine o somatório de todos os valores armazenados no vetor.

import numpy as np

array = np.zeros(5)

for i in range(5):
    array[i] = float(input(f"Digite o valor que deseja armazenar na posição V[{i}]? "))
    
somatorio = 0

for i in range(5):
    somatorio =  somatorio + array[i]
    
print(somatorio)

