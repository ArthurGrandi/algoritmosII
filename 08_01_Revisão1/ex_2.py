"""
2. A prefeitura de uma cidade fez uma pesquisa com 100 pessoas, coletando dados sobre o salário e o	número de filhos. A prefeitura deseja saber:

a. A média do salário dessas pessoas
b. A média do número de filhos
c. O maior salário
d. A porcentagem de pessoas com salários até R$ 1500,00
"""
mediaSalario = 0
salario = 0
mediaFilhos = 0
filhos = 0
maiorSalario = 0
salarioInferior = 0
cont = 0

while cont < 3:
    salario = float(input("Insira seu salário: "))
    filhos = float(input("Insira seu numero de filhos: "))
    mediaSalario = mediaSalario + salario
    mediaFilhos = mediaFilhos + filhos

    if maiorSalario < salario:
        maiorSalario = salario
    if salario <= 1500:
        salarioInferior = salarioInferior + 1
    cont = cont + 1        

print(mediaSalario / 3)
print(mediaFilhos / 3)
print(salarioInferior / 3 * 100, "%")


"""
print("\nExercício 2:\n")

n = 1
s = 0
f = 0
p = 0

print("Média do Salário e número de filhos entre 100 pessoas.\n")

for i in range(5):
    print("Pessoa", n, ":")
    salario = float(input("Salário: "))
    s += salario
    filhos = float(input("Qtd. de filhos: "))
    f += filhos
print("")

if i == 0:
    maior = salario
else:
    if salario > maior:
        maior = salario
if salario <= 1500:
    p += 1

n += 1

n -= 1
s = s/n
f = f/n
p = (p/n)*100

print(f"Média salárial: R${s}")
print(f"Média da qtd. de filhos: {f}")
print(f"Maior salário: R${maior}")
print(f"Porcentagem de pessoas com salários até R$ 1500: {p}%\n")
"""
