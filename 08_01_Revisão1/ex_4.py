"""
4. Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas. 

Exemplo: Nome = RAFAEL
Resultado gerado pelo programa: 
R
RA
RAF
RAFA
RAFAE
RAFAEL
"""

print("\nExercício 4:\n")

nome = input("Digite o seu nome: ").upper()

for i in range(1, len(nome)+1):
	print(nome[:i])
