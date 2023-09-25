# Faça um programa que leia um vetor(lista) de 5 posições e uma matriz de 5x 5 calcule e mostre o resultado da multiplicação do primeiro elemento do vetor, por toda a primeira linha da matriz, do segundo item do vetor por toda a segunda linha da matriz e assim sucessivamente.

# Vetor V
# 1 2 3 4 5

# Matriz M
# 1 2 3 4 5
# 6 7 8 9 1
# 2 3 4 5 6
# 7 8 9 1 2
# 3 4 5 6 7

# Matriz Resultado
# 1 2 3 4 5
# 12 14 16 18 2
# 6 9 12 15 18
# 28 32 36 4 8
# 15 20 25 30 35

N = 5
lista = []
M = [[],[],[],[],[]]

for i in range(N):
    lista.append(int(input(f"Informe o {i+1}o valor: ")))

for i, l in enumerate(M):
    for c in range(len(M)):
        l.append(int(input(f"Informe {i},{c}: ")))

R = []
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(lista[l] * M[l][c])
    R.append(linha)

print(lista)
print(M)
print(R)