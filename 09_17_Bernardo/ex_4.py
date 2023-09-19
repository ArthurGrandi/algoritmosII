#Faça um algoritmo que lê 5 valores para uma variável do tipo vetor e determine o maior e o menor valor armazenado no vetor.

import numpy as np

array = np.zeros(5)
    
for i in range(5):
    array[i] = float(input(f"Qual valor você deseja armazenar na posição V[{i}]? "))
    
max = 0
min = 0

for i in range(5):
    if (i == 0):
        max = array[i]
        min = array[i]
    elif (array[i] > max):
        max = array[i]
    elif (array[i] < min):
        min = array[i]
        
print("Maior valor:", max)
print("Menor valor:", min)