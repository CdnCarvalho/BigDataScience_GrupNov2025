# tb_emprestimos.csv e tb_usuarios no MySQL

from sqlalchemy import create_engine
import pandas as pd
import numpy as np


# Configurações do banco de dados
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_exemplo_biblioteca_aula02'


# Criação da conexão (engine)
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)


# Leitura das tabelas do MySQL
try:
    # Leitura das tabelas diretamente para DataFrames
    df_usuarios = pd.read_sql('tb_usuarios', con=engine)

    # Leitura dos arquivos externos
    df_emprestimos = pd.read_csv('tb_emprestimos.csv')

except Exception as e:
    print(f'Erro ao acessar o banco de dados: {e}')


# Relacionando os dataframes
try:
    # Relacinando com Merge
    df_emprestimos_usuarios = pd.merge(df_usuarios, df_emprestimos, on='id_usuario')
    
    print("\nEmprestimos pelos Usuários:")
    print(df_emprestimos_usuarios[['id_emprestimo', 'nome', 'cidade', 'data_emprestimo', 'valor']])

        # Filtrar usuários da cidade Curitiba
    df_cidade = df_emprestimos_usuarios[
        df_emprestimos_usuarios['cidade'] == 'Rio de Janeiro'
    ]

    print('\nEmpréstimos - Rio de Janeiro:')
    print(df_cidade.sort_values(by='valor', ascending=False))

except Exception as e:
    print(f'Erro ao processar as informações: {e}')


# Medidas de Tendência Central
try:
    # Converter a coluna valor para array numpy
    array_valores = np.array(df_emprestimos_usuarios['valor'])

    # Cálculo da média e mediana
    media = np.mean(array_valores)
    mediana = np.median(array_valores)

    # Distância entre média e mediana
    distancia = (media - mediana) / mediana

    print('\nMedidas de Tendência Central:')
    print(f'Média: {media:.2f}')  # valor médio dos empréstimos realizados. Indica quanto, em média, os usuários gastam
    print(f'Mediana: {mediana:.2f}')  # É o valor central da distribuição, metade dos empréstimos estão abaixo de ...
    print(f'Distância (Média - Mediana): {distancia:.4f}')

    # Distancia
    # O valor negativo muito próximo de zero indica que a média é ligeiramente menor, 
    # que a mediana, o que sugere uma distribuição praticamente simétrica dos valores dos empréstimos.

    # Os valores emprestímos apresentam equilíbrio na distribuição, 
    # sem indícios relevantes de valores extremos. 
    # Isso indica, que os usuários possuem um padrão de gasto bastante homogêneo, 
    # com pouca variação entre os valores pagos

except Exception as e:
    print(f'Erro no cálculo das medidas de tendência central: {e}')


# Medidas de Posição Estatística 
try:
    # Cálculo dos quartis
    q1 = np.quantile(array_valores, .25)
    q2 = np.quantile(array_valores, .50)  # Mediana
    q3 = np.quantile(array_valores, .75)

    print('\nMedidas de Posição Estatística (Quartis):')
    print(f'Q1: {q1:.2f}')  # Indica que 25% dos empréstimos possuem valor até 13,81
    print(f'Q2: {q2:.2f}')
    print(f'Q3: {q3:.2f}') # Indica que 75% dos empréstimos possuem valor até 21.56 o os 25% restantes correspondem aos empréstimos de maior valor. Os mais caros.

except Exception as e:
    print(f'Erro no cálculo das medidas de posição estatística: {e}')

