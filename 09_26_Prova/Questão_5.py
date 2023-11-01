# 5) (2,0 pontos) Faça um programa que leia um vetor de 3 posições e uma matriz de 3 x 3 calcule e mostre o resultado da multiplicação do primeiro item do vetor, por toda a primeira coluna da matriz, do segundo item do vetor por toda a segunda coluna da matriz e assim sucessivamente e armazene os resultados linha a linha na matriz resultado.

# Vetor V
# 1 2 3

# Matriz M
# 1 5 8
# 5 2 0
# -1 -5 2

# Matriz Resultado
# 1 5 -1
# 10 4 -10
# 24 0 15

import numpy as np

print("\nQuestão 5) \n")

TamanhoLista = 3
Lista = []
Matriz = [[], [], []]

for i in range(TamanhoLista):
    Lista.append(int(input(f"Informe o {i+1}º valor do vetor: ")))

for i in range(TamanhoLista):
    for c in range(TamanhoLista):
        Matriz[i].append(int(input(f"Informe o elemento {i + 1},{c + 1} da matriz: ")))

MatrizResultado = []

for c in range(TamanhoLista):
    linha = []
    for l in range(TamanhoLista):
        linha.append(Lista[l] * Matriz[l][c])
    MatrizResultado.append(linha)

print(f"Vetor: {Lista}")
print("")
print(f"Matriz: {Matriz}")
print("")
print(f"Resultado: {MatrizResultado}")