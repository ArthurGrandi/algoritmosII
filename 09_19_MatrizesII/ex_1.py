# Faça um algoritmo que receba um valor N correspondente ao tamanho de duas matrizes quadradas de ordem N (MNxN). Leia os valores inteiros para preencher todas as posições de cada uma das matrizes, e calcule a SOMA das matrizes.

# ENTRADAS
# Valor de N ; Valor de M;
# Numeros inteiros

N = int(input("Informe N: "))

m1 = [] # Lista
mR = []

# Leitura de valores em uma matriz
for l in range (0, N, 1): # 0, 1 ,2
    # Ler as linhas da tabela
    linha = []
    for c in range(N):
        # Ler colunas da linha
        linha.append(int(input(f"informe posição: {l},{c}: ")))
    # Adiciona a linha na m1
    m1.append(linha)
    
m2 = []

# Leitura de valores em uma matriz
for l in range (0, N, 1): # 0, 1 ,2
    # Ler as linhas da tabela
    linha = []
    for c in range(N):
        # Ler colunas da linha
        linha.append(int(input(f"informe posição: {l},{c}: ")))
    # Adiciona a linha na m1
    m2.append(linha)

print(m1) 
print(m2)

mR = []
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(m1[l][c]+m2[l][c])
    mR.append(linha)
print(mR)

# SAÍDAS
# Mtriz MxN
# Soma das matrizes
