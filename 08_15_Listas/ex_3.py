"""
3. Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.
"""

l1 = []
l2 = []
l3 = []

for i in range(0,5):
    l1.append(int(input(f"L1 - valor indice {i}: ")))
    
for i in range(0,5):
    l2.append(int(input(f"L2 - valor indice {i}: ")))
    
print(l1)
print(l2)

for i in range(0,5):
    l3.append(l1[i] + l2[i])
    
print(l3)