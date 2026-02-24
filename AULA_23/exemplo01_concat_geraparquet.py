# import pandas as pd
from datetime import datetime
import gc  # Garbage Collector
import os
import polars as pl


# ENDERECO_DADOS = r'../dados/'
ENDERECO_DADOS = r'C:/DADOS/'
ENDERECO_DADOS_PARQUET = r'./PARQUET/'

try:
    print('Obtendo dados')
    inicio = datetime.now()


    df_bolsa_familia = None
    # Lista para receber CSVs, que serão processados
    lista_arquivos = []
    # Lista de todos os arquivos, que virão da pasta
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)


    # Pegando os arquivos CSVs do diretório
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    print(lista_arquivos)


    # Leitura dos arquivos
    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}...')

        # Leitura de cada um dos dataframes
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        # Concatenação dos Dataframes
        # Verifica se o DataFrame df_bolsa_familia está vazio,
        # Se estiver vazio, "é que o Loop está na primeira execução", 
        # Então o df_dados é atribuído ao df_bolsa_familia.
        # Caso contrário, Se for diferente de None, acontece a concatenação,
        # pois neste caso, já teremos, pelo menos 1 dataframe no df_bolsa_familia atribuido.
        # Concatenação de dataframes
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            print(f'Concatenando o arquivo {arquivo} ao DataFrame df_bolsa_familia...')
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        # Remover df_dados após o uso para liberar memória
        del df
        
        print(df_bolsa_familia.head())
        print(f'Arquivo {arquivo} processados com sucesso!')

except Exception as e:
    print(f'Erro ao concatenar os dataframes: {e}')


try:
    # Converte a coluna 'VALOR PARCELA' para o tipo float
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA')
        .str.replace(',', '.')
        .cast(pl.Float64)
    )

    print('\nDados dos DataFrames concatenados com sucesso!')
    print('Incinando a gravação do arquivo Parquet...')

    # # Criar a pasta bronze, se não existir
    # os.makedirs('../bronze', exist_ok=True)

    # Gravar o arquivo parquet
    # df_bolsa_familia.write_parquet('../bronze/bolsa_familia.parquet')
    df_bolsa_familia.write_parquet('./PARQUET/bolsa_familia.parquet')

    print('\nArquio Parquet gravado com sucesso!')   
    print(df_bolsa_familia.shape)   # qtd linhas e colunas    
    print(df_bolsa_familia.columns)  # nome das colunas
    print(df_bolsa_familia.dtypes)  # tipo de dados de cada coluna
    
    del df_bolsa_familia  # Deletar df_bolsa_familia da memória

    # Coletar resíduos da memória
    gc.collect()

    fim = datetime.now()

    print(f'Tempo de execução: {fim - inicio}')
    print('Gravação do arquivo Parquet realizada com sucesso!')

except Exception as e:
    print(f'Erro ao processar os dataframes: {e}')


# # Lendo os dados do parquet
# try:
#     print('\nIniciando leitura do arquivo parquet...')

#     # Pega o tempo inicial
#     inicio =  datetime.now()

#     df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
#     print(df_bolsa_familia.head())
#     print(df_bolsa_familia.columns)

#     # Pega o tempo final
#     fim = datetime.now()

#     print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
#     print('\nArquivo parquet lido com sucesso!')

# except Exception as e:
#     print(f'Erro ao ler os dados do parquet: {e}')
