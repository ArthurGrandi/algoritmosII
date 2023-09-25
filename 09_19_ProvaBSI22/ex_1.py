# 1) (2,0 pontos) Faça um algoritmo que lê valores para duas (2) estruturas (array, lista, tupla ou conjunto) A e B com 3 elementos cada. Após apresente os valores lidos na ordem inversa. Exemplo.


#ENTRADA
# Valores da lista A e B

ListaA = []
ListaB = []

for i in range(3):
    valor = int(input(f"Qual valor você deseja preencher na posisção V[{i}] da lista A? "))
    ListaA.append(valor)
    
for i in range(3):
    valor = int(input(f"Qual valor você deseja preencher na posisção V[{i}] da lista B? "))
    ListaB.append(valor)
    
ListaA.reverse()
ListaB.reverse()

print(f"A lista A invertida ficou: {ListaA}")
print(f"A lista B invertida ficou: {ListaB}")

#PROCESSAMENTO
# Inverter os valores lidos



#SAÍDA
# Listas invertidas


