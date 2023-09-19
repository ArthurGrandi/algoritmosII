# Faça um algoritmo que leia a idade de uma pessoa e a expresse em dias

"""
Entradas - idade em anos
Processamento - multiplicar os anos por 365
Saidas - idade expressa em dias
"""

#ENTRADAS
anos = int(input("informe a idade em anos: "))                 

#PROCESSAMENTOS - atribuições de valor, operações aritméticas
dias = anos * 365

if (dias > 10000):
    print("Voce ja viveu mais que 10.000 dias")
else:
    print("jovem")

#SAIDAS
print(f"A idade corresponde a {dias} dias")
print("A idade corresponde a ", dias, " dias")