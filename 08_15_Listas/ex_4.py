"""
4. Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo inverso da segunda lista.
"""

#N = (int(input("Insira quantos numeros serão verificados: \n")))
#
#L = []
#X = []
#Z = []
#
#for i in range (N):
#    L.append (int(input("Insira um numero: \n")))
#    X.append (int(input("Insira um numero: \n")))
#print(L,X)
#
#for i in range (N):
#    Z.append (L[i] * X[N-1-i])
#print(Z)

l1 = []
l2 = []
l3 = []

N = 5
for i in range(0,N):
    l1.append(int(input(f"L1 - valor indice {i}: ")))
    
for i in range (0,N):
    l2.append(int(input(f"L2 - valor indice {i}: ")))