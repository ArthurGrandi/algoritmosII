tam = 5
lista = []
listainversa = []

for i in range (0,tam):
    lista.append(int(input(f"Digite um número para a lista {i}: ")))
    
print("Lista:", lista)

for i in range (0,tam):
    lista.append(lista[i] * -1)
    
lista.reverse()

listainversa = lista

print(listainversa)