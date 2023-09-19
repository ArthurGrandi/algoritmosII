"""
2. Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x. Após completar toda a leitura da lista, verificar se cada valor armazenado na lista é par ou ímpar. Se for par, fazer com que o valor seja atualizado para o resultado da multiplicação do valor contido pelo índice. Se for impar fazer com que a lista receba o valor do seu próprio índice.
"""

x = []

for i in range(0, 10):
    x.append(int(input("numero: ")))
print(x)

for i in range(10):
    if x[i] % 2 == 0:  # par
        x[i] = x[i]*i
    else:
        x[i] = i

print(x)
