# 1) (2,0 pontos) Faça um algoritmo que preencha um variável (array, lista, tupla ou conjunto) com 8 números inteiros, calcule e mostre as duas variáveis (array, lista, tupla ou conjunto) resultantes. A primeira variável deve conter os números positivos e o segundo, os números negativos informados pelo usuário. Cada variável de resultado terá, no máximo, oito posições, que poderão ou não ser utilizadas. No caso do valor 0, este não deverá ser incluído nas variáveis de resultado.

import numpy as np

print("\nQuestão 1)")

Lista = np.zeros(8)

NumPositivo = []
NumNegativo = []
Zero = 0
Zeros = []

Tamanho = 8

for i in range(Tamanho):
    Lista[i] = int(input(f"\nQual número você deseja preencher na posição V[{i}]? \n"))

for i in range(Tamanho):
    if (Lista[i] > Zero):
        NumPositivo.append(Lista[i])
    elif (Lista[i] < Zero):
        NumNegativo.append(Lista[i])

print(f"Lista original: {Lista}\n")
print(f"Numeros positivos: {NumPositivo}\n")
print(f"Numeros negativos: {NumNegativo}")
