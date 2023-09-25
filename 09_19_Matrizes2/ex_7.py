# Faça um algoritmo que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:

# a. o total de faltas do campeonato;
# b. o time que fez mais faltas;
# c. o time que fez menos faltas;

jogos = [
    ['Brasil', 'Italia', [10,9]],
    ['Brasil', 'Espanha', [5,7]],
    ['Italia', 'Espanha', [7,8]]
]

paises = []
faltas = []
for l in range(len(jogos)):
    for c in range(len(jogos)-1):
        paises.append(jogos[l][c])
        faltas.append(jogos[l][2][c])

print(paises)
print(faltas)

print(f"total de faltas: {sum(faltas)}")

matriz = [[],[]]

for i in range(len(paises)):
    if paises[i] not in matriz[0]:
        matriz[0].append(paises[i])
        matriz[1].append(faltas[i])
    else:
        for j in range(len(matriz[0])):
            if matriz[0][j] == paises[i]:
                matriz[1][j]+=faltas[i] 

print(matriz)