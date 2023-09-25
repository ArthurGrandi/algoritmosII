# 3) (2,0 pontos) Elabore um programa que preencha uma estrutura (array, lista, tupla ou conjunto), com 18 elementos calcule e mostre:
# a) O maior valor armazenado na estrutura e a sua respectiva posição;
# b) O menor valor armazenado na estrutura e a sua respectiva posição;

maiorvalor = 0
menorvalor = 0
maiorindice = 0
menorindice = 0

Lista = []

tamanho = 18

for i in range(tamanho):
    Lista.append(int(input(f"Qual valor você deseja armazenar na posição V[{i}]? ")))
    
for i in range(tamanho):
    if(Lista[i] > maiorvalor):
        maiorvalor = Lista[i]
        maiorindice = [i]
    elif(Lista[i] < menorvalor):
        menorvalor = Lista[i]
        menorindice = [i]
        
print(f"O maior valor é {maiorvalor} e esta armazenado no indice {maiorindice}!")
print(f"O menor valor é {menorvalor} e esta armazenado no indice {menorindice}!")