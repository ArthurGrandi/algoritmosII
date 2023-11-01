"""
Crie uma sub-rotina que receba como parâmetro uma lista V contendo 25 elementos de números inteiros e substitua todos os valores negativos de V por 0. A lista deverá ser retornada para quem realizou a chamada desta função.
"""


def substituiNegativos(V: list):
    for i in range( len(V) ):
        if V[i]<0: #item valor negativo
            V[i] = 0  #item recebe zero
    
    return V 

#################

lista = [1,-2,3,-4,5]
alterada = substituiNegativos(lista)
print(alterada)