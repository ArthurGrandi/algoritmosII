#Faça um algoritmo que lê 10 valores para uma variável do tipo vetor e mostre qual a posição está armazenado o maior e o menor valor no vetor.

import numpy as np

array = np.zeros(10)

for i in range(10):
    array[i] = float(input(f"Qual valor deseja armazenar na posição V[{i}]? "))
    
maxindex = 0
minindex = 0
    
for i in range(10):
    if (i == 0):
        maxindex = i
        minindex = i
    elif (array[i] > array[maxindex]):
        maxindex = i
    elif (array[i] < array[minindex]):
        minindex = i
        
print(f"O indice com o maior valor armazenado é: {maxindex}")
print(f"O indice com o menor valor armazenado é: {minindex}")