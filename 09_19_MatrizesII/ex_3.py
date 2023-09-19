# Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a variável “a” (do tipo simples, pode ser: inteiro, float). Multiplicar cada valor contido na matriz pelo valor da variável e colocar os resultados num vetor(lista) V com 16 elementos. Mostre no final o vetor(lista).

matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]


for l in range (4):
    for c in range(4):
        matriz[l][c] = int(input(f"informe o valor para a posição {l},{c}: ")) 
       
a = int(input("Informe o multiplicador: "))

lista = []

for l in range (4):
    for c in range(4):
        lista.append(a * matriz[l][c])

print(lista)