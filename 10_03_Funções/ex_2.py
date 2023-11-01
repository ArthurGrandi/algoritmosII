"""
Faça um algoritmo contendo uma sub-rotina que receba dois números positivos inteiros por parâmetro e retorne a soma dos N números inteiros existentes entre eles, incluindo na soma os dois números informados.
"""
def somaNums(x: int, y: int):
    res = 0
    for i in range(x, y+1):
        res = res + i

    return res


#############
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

soma = somaNums(a, b)

print(soma)