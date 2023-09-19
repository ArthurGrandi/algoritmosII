"""
1. Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e mostre os 10 valores armazenados.
"""

Lista = []

for i in range(0,10):
    Lista.append(int(input("numero: ")))
print(Lista)

for i in range(10):
    print(Lista[i])