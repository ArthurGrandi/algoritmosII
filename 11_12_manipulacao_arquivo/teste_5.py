import pandas as pd

# Carregar o arquivo CSV
caminho_arquivo = "/workspaces/algoritmosII/11_12_manipulacao_arquivo/Official Stats.csv"
df = pd.read_csv(caminho_arquivo)

# Função para apresentar informações básicas do arquivo
def mostrar_linhas_colunas():
    print(f"Número de linhas do documento original: {len(df)}")
    print("Nomes das colunas:")
    print(df.columns)
    return df

# Função para criar um arquivo parcial com base em uma filtragem de dados
def busca_parcial():
    coluna_filtro = input("Escolha entre uma das colunas:\n1. HP\n2. Tamanho\n3. Tipo\n4. Alinhamento\n5. Classe de Armadura\n6. Locomoção\n7. Línguas\n8. Nível de Dificuldade\n")

    # Converta coluna_filtro para inteiro
    coluna_filtro = int(coluna_filtro)

    # Funções específicas de filtragem
    if coluna_filtro == 1:
        df_filtrado = df[['Name', 'HP']]
    elif coluna_filtro == 2:
        df_filtrado = df[['Name', 'Size']]
    elif coluna_filtro == 3:
        df_filtrado = df[['Name', 'Type']]
    elif coluna_filtro == 4:
        df_filtrado = df[['Name', 'Align.']]
    elif coluna_filtro == 5:
        df_filtrado = df[['Name', 'AC']]
    elif coluna_filtro == 6:
        df_filtrado = df[['Name', 'Speeds']]
    elif coluna_filtro == 7:
        df_filtrado = df[['Name', 'Languages']]
    elif coluna_filtro == 8:
        df_filtrado = df[['Name', 'CR']]
    else:
        print("--------------------\nEscolha uma opção válida!")
        return

    nome_arquivo_parcial = input("Informe o nome para o arquivo parcial: ")
    df_filtrado.to_csv(f"{nome_arquivo_parcial}.csv", index=False)


# Função para criar um arquivo de resumo com a soma das linhas para colunas específicas
def resumo_total():
    # Colunas desejadas
    colunas_desejadas = ['AC', 'HP', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'CR']

    # Criar um DataFrame com as somas das linhas para as colunas desejadas
    resumo_df = pd.DataFrame(df[colunas_desejadas].sum(), columns=['Soma']).reset_index()
    resumo_df.columns = ['Coluna', 'Soma']

    # Informar o nome para o arquivo de resumo
    nome_arquivo_resumo = input("Informe o nome para o arquivo de resumo: ")

    # Salvar o arquivo de resumo em formato CSV
    resumo_df.to_csv(f"{nome_arquivo_resumo}.csv", index=False)

    print("Arquivo de resumo criado com sucesso!")

# Função para apresentar dados estatísticos
def mostrar_estatisticas():
    estatisticas = df.describe()
    print("Dados estatísticos:")
    print(estatisticas)

# Função para realizar busca de dados
def busca_geral():
    termo_busca = input("Informe o termo de busca: ")
    resultado_busca = df[df.apply(lambda row: any(str(termo_busca).lower() in str(cell).lower() for cell in row), axis=1)]
    nome_arquivo_parcial = input("Informe o nome para o arquivo: ")
    resultado_busca.to_csv(f"{nome_arquivo_parcial}.csv", index=False)

# Função para realizar busca específica
def busca_especifica():
    coluna_filtro = input("Escolha entre uma das colunas:\n1. Nome\n2. HP\n3. Tamanho\n4. Tipo\n5. Alinhamento\n6. Classe de Armadura\n7. Locomoção\n8. Línguas\n9. Nível de Dificuldade\n")
    
    # Mapeamento entre opções e nomes de colunas
    colunas = {
        '1': 'Name',
        '2': 'HP',
        '3': 'Size',
        '4': 'Type',
        '5': 'Align',
        '6': 'AC',
        '7': 'Speeds',
        '8': 'Languages',
        '9': 'CR'
    }
    
    # Verifica se a opção inserida é válida
    if coluna_filtro not in colunas:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return
    
    # Obtém o nome da coluna com base na opção escolhida
    coluna_escolhida = colunas[coluna_filtro]
    
    termo_busca = input(f"Informe o termo de busca para a coluna '{coluna_escolhida}': ")
    
    # Realiza a busca exata apenas na coluna escolhida (HP, AC, CR)
    if coluna_escolhida in ['HP', 'AC', 'CR']:
        resultado_busca = df[df[coluna_escolhida].astype(str) == termo_busca]
    else:
        resultado_busca = df[df[coluna_escolhida].apply(lambda cell: str(termo_busca).lower() in str(cell).lower())]
    
    nome_arquivo_parcial = input("Informe o nome para o arquivo: ")
    
    # Salva o resultado da busca em um arquivo CSV
    resultado_busca.to_csv(f"{nome_arquivo_parcial}.csv", index=False, na_rep="None")

# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Apresentar informações do arquivo")
    print("2. Criar arquivo parcial")
    print("3. Criar arquivo de resumo")
    print("4. Apresentar dados estatísticos")
    print("5. Realizar busca de dados")
    print("6. Realizar busca específica")
    print("0. Sair")

    escolha = input("Escolha a operação desejada (0 a 6): ")

    print("--------------------")

    if escolha == '1':
        mostrar_linhas_colunas()
    elif escolha == '2':
        busca_parcial()
    elif escolha == '3':
        resumo_total()
    elif escolha == '4':
        mostrar_estatisticas()
    elif escolha == '5':
        busca_geral()
    elif escolha == '6':
        busca_especifica()
    elif escolha == '0':
        print("Programa encerrado.")
        break
    else:
        print("Escolha inválida. Tente novamente.")