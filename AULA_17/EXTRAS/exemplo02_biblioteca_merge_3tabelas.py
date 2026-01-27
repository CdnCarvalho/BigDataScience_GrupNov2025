from sqlalchemy import create_engine
import pandas as pd


# Configurações do banco de dados
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_exemplo_biblioteca_aula02'


# Criação da conexão (engine)
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}')


#  Obtendo os dados 
try:
    # Banco de dados
    df_livros = pd.read_sql('tb_livros', con=engine)
    print(df_livros)
    df_usuarios = pd.read_sql('tb_usuarios', con=engine)

    # Arquivos externos
    df_emprestimos = pd.read_csv('tb_emprestimos.csv')
    df_itens = pd.read_csv('tb_itens_emprestimos.csv', sep=';')

except Exception as e:
    print(f'Erro ao acessar o banco de dados: {e}')


# Relacionando
try:
    # Relacionando os dataframes - Usando o método Merge
    df_completo = pd.merge(df_itens, df_emprestimos, on='id_emprestimo')
    df_completo = pd.merge(df_completo, df_usuarios, on='id_usuario')
    df_completo = pd.merge(df_completo, df_livros, on='id_livro')


    # Delimitando as variáveis
    df_resumo = df_completo[['id_emprestimo', 'nome', 'cidade','titulo', 'data_emprestimo', 'valor']]
    print(df_resumo)

    # Agrupamento dos dados
    df_resumo = (
        df_resumo
        .groupby(['nome', 'data_emprestimo', 'titulo'])
        .sum(['valor'])
        .reset_index()
    )

    # # Renomeação das colunas
    df_resumo.rename(columns={
        'nome': 'nome_usuario',
        'valor_emprestimo': 'total_emprestado'
    }, inplace=True)


    # Exibição do resultado final
    print(df_resumo)

except Exception as e:
    print(f'Erro ao acessar o banco de dados: {e}')
    