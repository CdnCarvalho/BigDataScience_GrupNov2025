# # ATIVIDADE
# # Mostre o nome do cliente e a data de cada pedido realizado.

# # Instalação (se ainda não tiver instalado)
# # pip install sqlalchemy pymysql pandas

# from sqlalchemy import create_engine, text
# import pandas as pd

# # Configurações do banco
# host = 'localhost'
# user = 'root'
# password = '123456'
# database = 'abril2025_mod02_pedido'

# # Cria a conexão com o MySQL
# try:
#     with engine.connect() as conexao:
        
#         # df_clientes = pd.read_sql('tb_clientes', con=engine)
#         engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
        
#         # Consulta e leitura da tabela de clientes
#         query_clientes = "SELECT * FROM tb_clientes"
#         df_clientes = pd.read_sql(text(query_clientes), conexao)

#         # Consulta e leitura da tabela de pedidos
#         query_pedidos = "SELECT * FROM tb_pedidos"
#         df_pedidos = pd.read_sql(text(query_pedidos), conexao)

# except Exception as e:
#     print(f'Erro ao conectar ao banco: {e}')
#     # df_clientes = pd.DataFrame()
#     # df_pedidos = pd.DataFrame()

# # Leitura dos arquivos CSV (produtos e itens)
# df_produtos = pd.read_csv('tb_produtos.csv')
# df_itens = pd.read_csv('tb_itens.csv')

# # Relacionamento entre clientes e pedidos (JOIN)
# df_relacionado = pd.merge(df_clientes, df_pedidos, left_on='cod_cliente', right_on='cliente_codigo')

# # Exibe apenas nome do cliente e data do pedido
# print(df_relacionado[['nome', 'data_pedido']])

# --------------------------------------------------------------------------------
# # Mostre o nome do cliente e a data de cada pedido realizado.

# # Instalação (se ainda não tiver instalado)
# # pip install sqlalchemy pymysql pandas
from sqlalchemy import create_engine
import pandas as pd

# Configurações do banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'abril2025_mod02_pedido'

# Cria o engine (conexão)
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

try:
    # Leitura das tabelas diretamente para DataFrames
    df_clientes = pd.read_sql('tb_clientes', con=engine)
    df_pedidos = pd.read_sql('tb_pedidos', con=engine)

except Exception as e:
    print(f'Erro ao conectar ou consultar o banco: {e}')
    df_clientes = pd.DataFrame()
    df_pedidos = pd.DataFrame()

# Relacionamento entre clientes e pedidos (JOIN)
df_relacionado = pd.merge(
    df_clientes,
    df_pedidos,
    left_on='cod_cliente',
    right_on='cliente_codigo'
)

# Exibe nome do cliente e data do pedido
print(df_relacionado[['nome', 'data_pedido']])
