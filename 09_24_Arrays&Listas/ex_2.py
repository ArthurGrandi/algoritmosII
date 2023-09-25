# Arrays e Listas:

# 2 - Escreva um programa para somar todos os elementos de uma lista.

vetor = []
somatotal = 0

tamanho = int(input(f"Quantos valores voce deseja armazenar na lista? "))

for i in range(tamanho):
    valor = int(input(f"Qual valor você deseja armazenar na posição V[{i}]? "))
    vetor.append(valor)

for i in range(tamanho):
    somatotal += vetor[i]
    
print(somatotal)