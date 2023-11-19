 - Apresentar um relatório com o número de linhas do documento original, e os nomes das colunas, que descrevem os dados;

# - Criar um arquivo parcial, com nome informado pelo usuário, que armazenará os dados correspondentes a uma filtragem de dados. Para este arquivo, também deverá ser possível chamar a função de relatório anterior.

# - Criar arquivo de Resumo - Deverá apresentar dados agrupados, com totalizadores.

# - Apresentar dados estatísticos sobre o arquivo, pode ser gerado média, moda, desvio padrão, entre outros.

# - Realizar uma busca de dados no(s) arquivo(s).


# arquivo = open ("trab_alg/Official Stats.csv", "r")
# for linha in arquivo.readlines():
#     print(linha)
# arquivo.close

import pandas as pd

# Função para carregar os dados do arquivo CSV
def carregar_dados(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

# Função para exibir informações básicas sobre os dados
def relatorio_inicial(dados):
    print(f"Número de linhas do documento original: {len(dados)}")
    print("Nomes das colunas:")
    print(dados.columns)

# Função para criar um arquivo parcial com filtragem de dados
def criar_arquivo_parcial(dados, nome_arquivo_parcial):
    # Exibir as colunas disponíveis para escolha
    print("Colunas disponíveis:")
    print(dados.columns)
    
    # Solicitar ao usuário que escolha uma coluna
    coluna_escolhida = input("Escolha uma coluna para filtragem: ")
    
    filtro = input("Informe o filtro para os dados: ")
    
    # Verificar se a coluna escolhida existe
    if coluna_escolhida in dados.columns:
        dados_filtrados = dados[dados[coluna_escolhida].astype(str).str.contains(filtro, case=False)]
        dados_filtrados.to_csv(nome_arquivo_parcial, index=False)
        relatorio_inicial(dados_filtrados)
    else:
        print(f"A coluna '{coluna_escolhida}' não existe no conjunto de dados.")

# Função para criar um arquivo de resumo
def criar_arquivo_resumo(dados, nome_arquivo_resumo):
    resumo = dados.groupby('Nome_da_coluna').size().reset_index(name='Contagem')
    resumo.to_csv(nome_arquivo_resumo, index=False)
    print("Arquivo de resumo criado com sucesso.")
    print(resumo)

# Função para exibir dados estatísticos
def dados_estatisticos(dados):
    estatisticas = dados.describe()
    print("Dados estatísticos:")
    print(estatisticas)

# Função para realizar uma busca de dados
def busca_de_dados(dados):
    termo_busca = input("Informe o termo de busca: ")
    resultados_busca = dados[dados['Nome_da_coluna'].str.contains(termo_busca, case=False)]
    print("Resultados da busca:")
    print(resultados_busca)

# Função principal que exibe o menu e chama as funções correspondentes
def main():
    caminho_arquivo = "trab_alg/Official Stats.csv"
    dados = carregar_dados(caminho_arquivo)

    while True:
        print("\nMenu Principal:")
        print("1. Relatório Inicial")
        print("2. Criar Arquivo Parcial")
        print("3. Criar Arquivo de Resumo")
        print("4. Dados Estatísticos")
        print("5. Busca de Dados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_inicial(dados)
        elif opcao == "2":
            nome_arquivo_parcial = input("Informe o nome do arquivo parcial: ")
            criar_arquivo_parcial(dados, nome_arquivo_parcial)
        elif opcao == "3":
            nome_arquivo_resumo = input("Informe o nome do arquivo de resumo: ")
            criar_arquivo_resumo(dados, nome_arquivo_resumo)
        elif opcao == "4":
            dados_estatisticos(dados)
        elif opcao == "5":
            busca_de_dados(dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
