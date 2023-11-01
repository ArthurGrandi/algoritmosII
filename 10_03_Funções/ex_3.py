"""
Elabore um algoritmo que receba as 3 notas de um aluno e uma letra. Se a letra for “A”, deve-se chamar uma sub-rotina que deverá calcular a média aritmética das notas dos alunos; Se a letra for “P”, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média calculada deverá ser devolvida ao programa principal para, então, ser mostrada.
"""

#definir funcao - nome, parenteses, parametros
def aritmetica(a: float, b: float, c: float):
    global media
    media = (a+b+c)/3
    print(media)

def ponderada(a: float, b: float, c: float, p1:float, p2:float, p3:float):
    media = (a*p1 + b*p2 + c*p3) / (p1+p2+p3)
    print(media)

###############################################################
#A L G O R I T M O        P R I N C I P A L
#Entrada de 3 notas
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
#Entrada de opção (A / P)
opcao = input("Informe o tipo de média (A/P):")

if opcao=="A": #se for "A", calcula média, rotina aritmetica()
    aritmetica(n1, n2, n3,)
elif opcao=="P": #senão ("P"), calcula a média, rotina ponderada()
    ponderada(n1, n2, n3,5.0,3.0,2.0)
else:
    print("Opção inválida")


print (f"Com a média {media}, voce foi reprovado")