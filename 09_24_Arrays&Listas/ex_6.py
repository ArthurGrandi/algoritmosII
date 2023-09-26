# Arrays e Listas:

# 6 - Escreva um programa para encontrar todos os números pares em uma lista.

print("\nExercicio No 6\n")

Lista = []
NumeroPar = []
IndicePar = []

tamanho = int(input(f"Quantos valores voce deseja armazernar na lista? \n\n"))

for i in range(tamanho):
    Lista.append(int(input(f"Qual valor voce deseja armazenar na posicao V[{i}]? \n\n")))
    
for i in range(tamanho):
    if (Lista[i] == 2 % 0):
        NumeroPar = Lista[i]
        IndicePar = [i]
    
print(Lista)
print(f"\n Os Numeros pares encontrados nessa lists são: {NumeroPar}\n")