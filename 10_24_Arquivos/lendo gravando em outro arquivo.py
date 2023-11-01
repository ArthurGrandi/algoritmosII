#lendo de um arquivo e gravando em outro arquivo
with open("multiplos_de_4.txt", "w") as multiplos4:
    with open("pares.txt", "r") as pares:
        for l in pares.readlines():
            if int(l) % 4 == 0:
                multiplos4.write(f"{l}\n")