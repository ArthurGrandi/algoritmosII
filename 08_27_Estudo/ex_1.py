# nome = str(input("Diga seu nome: "))
# print("Olá", nome, "!") 
# indicar o indice dos numero armazenados

Vetor = []
par = []
impar = []
indiceP = []
indiceI = []

numero_de_valores = int(input("Digite quantos valores vocês deseja armazenar: "))

for i in range (numero_de_valores):
    Vetor.append (int(input("Digite os valores que queres armazenar: ")))

print(Vetor)

for i in range (numero_de_valores):
    if Vetor[i] % 2 == 0:
        par.append (Vetor[i])
        indiceP.append (i)
    else:
        impar.append (Vetor[i])
        indiceI.append (i)
        
print(par, indiceP)
print(impar, indiceI)
print(par, impar)
