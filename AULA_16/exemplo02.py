# # Instalação (se ainda não tiver instalado)
# # pip install sqlalchemy pymysql pandas

# from sqlalchemy import create_engine, text
# import pandas as pd

# # Configurações do banco
# host = 'localhost'
# user = 'root'
# password = '123456'
# database = 'abril2025_mod02_biblioteca'


# # Função para conectar e buscar tabelas do MySQL
# def busca_dados_sql(tabela):
#     try:
#         engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
#         with engine.connect() as conexao:
#             query = f"SELECT * FROM {tabela}"
#             df = pd.read_sql(text(query), conexao)
#             return df
#     except Exception as e:
#         print(f'Erro ao conectar ao banco: {e}')
#         return pd.DataFrame()  # Retorna DataFrame vazio em caso de erro


# # Lê os dados SQL
# df_livros = busca_dados_sql('tb_livros')
# df_usuarios = busca_dados_sql('tb_usuarios')


# # Lê os dados dos aquivos CSV (importados externamente)
# # Se for arquivo do excel: pd.read_excel()
# df_emprestimos = pd.read_csv('tb_emprestimos.csv')  
# df_itens = pd.read_csv('tb_itens_emprestados.csv', sep='\t')

# # para ver os nomes das colunas como estão escritos os caracteres
# # print("Colunas de df_itens:", df_itens.columns.tolist())
# # print("Colunas de df_emprestimos:", df_emprestimos.columns.tolist())


# # Relaciona os dados no Python
# # Uso do Merge 
# df_completo = pd.merge(df_itens, df_emprestimos, on='id_emprestimo')
# df_completo = pd.merge(df_completo, df_usuarios, on='id_usuario')
# df_completo = pd.merge(df_completo, df_livros, on='id_livro')

# # Exibe uma visão final com nome do usuário, data e valor total dos livros
# df_resumo = df_completo.groupby(['nome', 'data_emprestimo'])['valor_emprestimo'].sum().reset_index()
# df_resumo.rename(columns={
#     'nome': 'nome_usuario',
#     'valor_emprestimo': 'total_emprestado'
# }, inplace=True)

# print(df_resumo)


from sqlalchemy import create_engine
import pandas as pd

# ==============================
# Configurações do banco de dados
# ==============================
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_exemplo_biblioteca_aula02'

# ==============================
# Criação da conexão (engine)
# ==============================
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

# ==============================
# Leitura das tabelas do MySQL
# ==============================
try:
    df_livros = pd.read_sql('tb_livros', con=engine)
    df_usuarios = pd.read_sql('tb_usuarios', con=engine)
except Exception as e:
    print(f'Erro ao acessar o banco de dados: {e}')
    df_livros = pd.DataFrame()
    df_usuarios = pd.DataFrame()

# ==============================
# Leitura dos arquivos externos
# ==============================
df_emprestimos = pd.read_csv('tb_emprestimos.csv')
df_itens = pd.read_csv('tb_itens_emprestimos.csv', sep=';')
# df_itens = pd.read_csv('tb_itens_emprestados.csv', sep='\t')

# print(df_emprestimos.head())
# print(df_itens.head())

# ==============================
# Relacionamento dos dados (JOIN)
# ==============================
df_completo = pd.merge(df_itens, df_emprestimos, on='id_emprestimo')
df_completo = pd.merge(df_completo, df_usuarios, on='id_usuario')
df_completo = pd.merge(df_completo, df_livros, on='id_livro')

# ==============================
# Agrupamento dos dados
# ==============================
df_resumo = (
    df_completo
    .groupby(['nome', 'data_emprestimo'])['valor_emprestimo']
    .sum()
    .reset_index()
)

# ==============================
# Renomeação das colunas
# ==============================
df_resumo.rename(columns={
    'nome': 'nome_usuario',
    'valor_emprestimo': 'total_emprestado'
}, inplace=True)

# ==============================
# Exibição do resultado final
# ==============================
print(df_resumo)

