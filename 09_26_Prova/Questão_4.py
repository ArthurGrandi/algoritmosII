# 4) (2,0 pontos) Faça um algoritmo que preencha uma matriz 6 x 6 com números inteiros, execute as trocas especificadas a seguir e mostre a matriz resultante:
# ● A linha de índice 1 com a linha de índice 4;
# ● A coluna de índice 3 com a coluna de índice 5;

matriz = [[],[],[],[],[],[]]

for i in range(6):
    for j in range(6):
        matriz[i].append(int(input(f"Insira o valor ({i+1},{j+1}) da matriz: ")))

print("")

for i in range(6):
    print(matriz[i])

linha1 = []
linha4 = []
coluna3 = []
coluna5 = []

for i in range(6):
    linha1.append(matriz[1][i])
    linha4.append(matriz[4][i])

matriz[1] = linha4
matriz[4] = linha1

for i in range(6):
    coluna3.append(matriz[i][3])
    coluna5.append(matriz[i][5])

for i in range(6):
    matriz[i][3] = coluna5[i]
    matriz[i][5] = coluna3[i]

print("")
for i in range(6):
    print(matriz[i])