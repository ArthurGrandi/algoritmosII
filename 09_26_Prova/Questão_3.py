#3) (2,0 pontos) Faça um algoritmo com 100 valores armazenados em uma variável x (array, lista, tupla ou conjunto). Calcular e mostrar no final:
# ● a quantidade de valores pares armazenados em x.
# ● e a média dos valores impares armazenados em x.

import numpy as np

print("\nQuestão 3) \n")

Lista = np.zeros(10)
Tamanho = 10
NumPares = []
NumImpares = []
Impares = 0

for i in range(Tamanho):
    Lista[i] = int(input(f"Qual número você deseja preencher na posição V[{i}]? \n"))
    if (Lista[i] % 2 == 0):
      NumPares.append(Lista[i])
    else:
      NumImpares.append(Lista[i])

QuantiaPares = len(NumPares)
QuantiaImpares = len(NumImpares)

for i in range(QuantiaImpares):
  Impares += NumImpares[i]

MediaImpares = Impares / QuantiaImpares

print(f"\nA quantidade de valores pares armazenados é: { QuantiaPares }!\n")
print(f"A média dos valores impares armazenados é {MediaImpares}!")