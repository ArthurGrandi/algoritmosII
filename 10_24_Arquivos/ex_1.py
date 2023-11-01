# Faça um programa que crie um arquivo texto e que salve seu nome neste arquivo (o nome deve ser  informado via terminal).

nome = input("Digite o seu nome:")

with open("10_24_Arquivos/nome.txt", "w") as Banana:
    Banana.write(nome)

print(f"O Nome {nome}, foi salvo no arquivo 'nome.txt'")