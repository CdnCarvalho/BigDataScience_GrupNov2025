# # ATIVIDADE

# --------------------------------------------------------------------------------
# # Mostre o nome do cliente, cidade, data e valor de cada pedido realizado.
# tb_pedidos.csv e clientes no MySQL

# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv() # Carrega as variáveis no arquivo dot.env

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')
# -------------------------------------------------------------


# Instalação:  pip install sqlalchemy pymysql pandas
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

# Configurações do banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_atividade_pedidos_aula02'

# Cria o engine (conexão)
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


# Obter dados do banco
try:

    # Leitura das tabelas diretamente para DataFrames 
    df_clientes = pd.read_sql('clientes', con=engine)  # banco
    print('\nClientes:')
    print(df_clientes)
    
    df_pedidos = pd.read_csv('tb_pedidos.csv')  # csv
    print('\nPedidos:')
    print(df_pedidos)

except Exception as e:
    print(f'Erro ao conectar ou consultar o banco: {e}')


# Padronização dos dados
try:
    df_relacionado = pd.merge(
        df_clientes, df_pedidos,
        left_on='codigo_cliente', right_on='cliente_codigo'
    )

    print('\nDataFrame Relacionado:')
    print(df_relacionado)

    # Exibir código pedido, nome cliente, cidade, data pedido e valor
    print('\nDataFrame Relacionado (Nome do Cliente e Data do Pedido, Valor):')
    print(df_relacionado[['codigo_pedido', 'nome', 'cidade', 'data_pedido', 'valor']])
    
    # MOSTRAR DEPOIS: DELIMITAR AS VARIÁVEIS
    df_relacionado = df_relacionado[['codigo_pedido', 'nome', 'cidade', 'data_pedido', 'valor']]

    # Ordenado por data do pedido decrescente
    print('\nOrdenado por Data (Decrescente):')
    print(df_relacionado.sort_values(by='data_pedido', ascending=False))


    # Separar por Categoria - Exemplo: Cidade Curitiba
    df_curitiba = df_relacionado[df_relacionado['cidade'] == 'Curitiba']
    print('\nDataFrame - Cidade de Curitiba:')
    print(df_curitiba)

    # Obtendo os dados onde a cidade é 'Curitiba' ou 'São Paulo'
    df_filtrado_sp_coritiba = df_relacionado[
        (df_relacionado['cidade'] == 'Curitiba') |
        (df_relacionado['cidade'] == 'Sao Paulo')
    ]

    print('\nDataFrame Curitiba ou São Paulo:')
    print(df_filtrado_sp_coritiba)

except Exception as e:
    print(f'Erro na padronização as informações: {e}')


# Obtendo Medidas de tendência central
try:
    # Converter a coluna valor para array numpy
    array_valores = np.array(df_relacionado['valor'])

    # Cálculo da média e mediana
    media = np.mean(array_valores)
    mediana = np.median(array_valores)

    # Cálculo da distância relativa
    distancia_media_mediana = (media - mediana) / mediana

    print('\nMedidas de Tendência Central:')
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Distância (Média - Mediana) / Mediana: {distancia_media_mediana:.4f}')

    # Média
    # A média representa o valor médio gasto pelos Clientes, 
    # considerando todos os pedidos realizados, o gasto médio ficou em torno de R$ 51,77.
    # No entanto, a média pode ser influenciada por pedidos com valores mais altos,
    # como produtos mais caros ou múltiplos pedidos.

    # Mediana
    # indica o valor central da distribuição, ou seja:
    # Metade dos clientes efetuaram pedidos no valor até R$ 43,67,

    # Distância Relativa
    # O valor (0,1855) indica que a média é aproximadamente 18,55% maior que a mediana.
    # A distribuição dos pedidos apresenta assimetria à direita.
    # Existem alguns clientes que pagaram valores mais altos.

except Exception as e:
    print(f'Erro no cálculo das medidas estatísticas: {e}')


# Medidas de posição estatística - Quartis
try:
    # Cálculo dos quartis
    q1 = np.quantile(array_valores, .25)   # 1º Quartil (25%)
    q2 = np.quantile(array_valores, .50)   # 2º Quartil (Mediana)
    q3 = np.quantile(array_valores, .75)   # 3º Quartil (75%)

    print('\nMedidas de Posição Estatística (Quartis):')
    print(f'1º Quartil 25%: {q1:.2f}')  # 25% dos usuários gastaram até esse valor
    print(f'2º Quartil 50%: {q2:.2f}')  # valor central dos gastos
    print(f'3º Quartil 75%: {q3:.2f}')  # 75% dos usuários gastaram até esse valor, e apenas 25% gastaram acima

except Exception as e:
    print(f'Erro no cálculo dos quartis: {e}')
