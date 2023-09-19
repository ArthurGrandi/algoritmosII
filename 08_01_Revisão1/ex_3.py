"""
3. Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas. 

Exemplo: Nome = Lidiane
Resultado gerado pelo programa: ENAIDIL
"""

print("\nExercício 3:\n")

nome = input("Digite o seu nome: ").upper()
invertido = nome[::-1]
    
print("Nome invertido em letras maiúsculas:", invertido)
