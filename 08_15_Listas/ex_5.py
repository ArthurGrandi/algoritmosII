"""
5. Faça um algoritmo que lê duas listas A e B com 5 elementos cada. Construir uma lista C, sendo este a junção das duas outras listas, ou seja, a lista C deverá conter 10 elementos. Mostre no final a lista C.
"""


l1 = []
l2 = []
l3 = []
N = 5

for i in range(0,N):
    l1.append(int(input(f"L1 - valor indice {i}: ")))
    
for i in range(0,N):
    l2.append(int(input(f"L2 - valor indice {i}: ")))

#l3 = l1 + l2

for i in range(N):
    l3.append(l1[i])
for i in range(N):
    l3.append(l2[i])
print(l3)