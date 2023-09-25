# 2) (2,0 pontos) Faça um programa que faça a leitura e armazene 10 valores inteiros em uma estrutura (array, lista, tupla ou conjunto). Mostre quais os valores armazenados são menores ou iguais a 0 e suas respectivas posições. O programa deverá informar se não houver nenhum número armazenado nessa condição.

Lista = []

tamanho = 10

Menorqzero = []
imenorqzero = []

for i in range(tamanho):
    Lista.append(int(input(f"Qual valor deseja armazenar na posição V[{i}]: ")))
    
for i in range(tamanho):
    if (Lista[i] <= 0):
        Menorqzero.append(Lista[i])
        imenorqzero.append(i)
        
for i in range(tamanho):
    if not Menorqzero:
        print("Não tem números iguais ou menores que zero!")
        break
    else:
        print("valor: ", Menorqzero[i], "indice: ", imenorqzero[i], "\n")