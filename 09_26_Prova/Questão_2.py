# 2) (2,0 pontos) Faça um algoritmo que armazene 25 valores em uma variável (array, lista, tupla ou conjunto). O algoritmo deverá armazenar em uma nova variável os valores na ordem inversa e com o sinal inverso. Exemplo:
    
# Vetor V
# 1 -2 4 2 3
# Vetor Resultado
# - 3 -2 -4 2 -1

import numpy as np

print("\nQuestão 2)\n")

Lista = []
Lista_Inversa = []

Tamanho = 25

for i in range(Tamanho):
    Lista.append(float(input(f"Qual número você deseja preencher na posição V[{i}]? \n")))
    Lista[i] = Lista[i] * -1

Lista.reverse()

Lista_Inversa = Lista

print(Lista_Inversa)