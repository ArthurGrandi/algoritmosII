arquivo = open("aula.txt", "w")

for linha in range(1,101):
    arquivo.write(f"Linha {linha}\n")

arquivo.close