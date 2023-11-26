import pandas as pd

# Carregar o arquivo CSV
caminho_arquivo = "/workspaces/Arthur_Grandi_TF/arthur_grand_TF/Official Stats.csv"
df = pd.read_csv(caminho_arquivo)

# Função para apresentar informações básicas do arquivo
def mostrar_linhas_colunas():
    print(f"Número de linhas do documento original: {len(df)}")
    print("Nomes das colunas:")
    print(df.columns)
    return df

# Função para criar um arquivo parcial com base em uma filtragem de dados
def busca_parcial():
    coluna_filtro = input("Escolha entre uma das colunas:\n1. HP\n2. Tamanho\n3. Tipo\n")

    # Converta coluna_filtro para inteiro
    coluna_filtro = int(coluna_filtro)

    # Funções específicas de filtragem
    if coluna_filtro == 1:
        df_filtrado = df[['Name', 'HP']]
        novo_df = pd.DataFrame(df_filtrado)
        nome_arquivo_parcial = input("Informe o nome para o arquivo parcial: ")
        novo_df.to_csv(f"{nome_arquivo_parcial}.csv", index=False)

    elif coluna_filtro == 2:
        df_filtrado = df[['Name', 'Size']]
        nome_arquivo_parcial = input("Informe o nome para o arquivo parcial: ")
        df_filtrado.to_csv(f"{nome_arquivo_parcial}.csv", index=False)

    elif coluna_filtro == 3:
        df_filtrado = df[['Name', 'Type']]
        nome_arquivo_parcial = input("Informe o nome para o arquivo parcial: ")
        df_filtrado.to_csv(f"{nome_arquivo_parcial}.csv", index=False)
    else:
        print("Escolha uma opção válida!")

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

# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Apresentar informações do arquivo")
    print("2. Criar arquivo parcial")
    print("3. Criar arquivo de resumo")
    print("4. Apresentar dados estatísticos")
    print("5. Realizar busca de dados")
    print("0. Sair")

    escolha = input("Escolha a operação desejada (0 a 8): ")

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
    elif escolha == '0':
        print("Programa encerrado.")
        break
    else:
        print("Escolha inválida. Tente novamente.")
