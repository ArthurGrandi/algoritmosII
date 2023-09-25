"""
1. Faça um programa que solicite valores inteiros fornecidos pelo usuário até ele informar o valor 0 (zero). 

Em seguida, identifique e exiba quantos números ímpares e os pares foram fornecidos, sem considerar o valor 0.
"""

print("\nExercício 1:\n")

contP = 0
contI = 0

while True:
    Valores = int(input("Digite quantos valores quiser, para parar digite 0: "))
    if Valores == 0:
        break
    elif Valores % 2 == 0:
        contP = contP + 1
    else:
        contI = contI + 1

print("\nA quantidade de numeros pares é: ",contP, "\n\nA quantidade de numeros impares é: ",contI)



#print("\nExercício 1:\n")
#print("Informe números para saber quais são pares e quais são ímpares. (digite 0 para parar)")

#n = 1
#par = 0
#impar = 0

#while True:
#    print(f"Insira o {n}º número: ")
#    inp = input()

#    try:
#        inp = int(inp)
#        n += 1
#        print("")
#        if inp == 0:
#            break
#        elif inp % 2 == 0:
#            par = par+1
#        else:
#            impar = impar+1

#    except ValueError:
#        print("Por favor insira um número válido.\n")

#print("Pares:", par)
#print("Ímpares:", impar)
#print("")

