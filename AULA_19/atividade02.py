import pandas as pd
import numpy as np

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando somente as variáveis necessárias
    df_estelionato = df_ocorrencias[['mes_ano', 'munic', 'estelionato']]

    # Totalizar estelionato por mês/ano
    # df_estelionato = (df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index())
    df_estelionato = df_estelionato.groupby(['mes_ano', 'munic'], as_index=False)['estelionato'].sum()
    print(df_estelionato.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# obter informações sobre padrão de estelionato
try:
    print('Obtendo informações sobre padrão de estelionato...')

    # Converter para array numpy
    array_estelionato = np.array(df_estelionato['estelionato'])

    # Média e mediana
    media = np.mean(array_estelionato)
    mediana = np.median(array_estelionato)

    # Distância relativa entre média e mediana
    distancia = abs((media - mediana) / mediana)

    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de estelionatos: {media}')
    print(f'Mediana de estelionatos: {mediana}')
    print(f'Distância entre média e mediana: {distancia}')


    # Quartis (Weibull)
    q1 = np.quantile(array_estelionato, 0.25, method='weibull')
    q2 = np.quantile(array_estelionato, 0.50, method='weibull')
    q3 = np.quantile(array_estelionato, 0.75, method='weibull')

    # print('\nMedidas de posição: ')
    # print(30*'-')
    # print('Q1 (25%): ',q1)
    # print('Q2 (50%): ',q2)
    # print('Q3 (75%): ',q3)

    # Mairores e menores estelionatos
    # Maiores e menores valores (baseados nos quartis)
    print('\nMeses/Ano com menores quantidades de estelionato:')
    print(30*'-')
    df_estelionato_menores = df_estelionato[df_estelionato['estelionato'] < q1]
    print(df_estelionato_menores.sort_values(by='estelionato'))

    print('\nMeses/Ano com maiores quantidades de estelionato:')
    print(30*'-')
    df_estelionato_maiores = df_estelionato[df_estelionato['estelionato'] > q3]
    print(df_estelionato_maiores.sort_values(by='estelionato', ascending=False))


    # ------------------------ II - PARTE ------------------------
    # Medidas de dispersão
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)


    # IQR
    iqr = q3 - q1


    # Cálculo dos limites para outliers
    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    print('\nMedidas de posição: ')
    print(30*'-')
    print('Mínimo: ', minimo)
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print('Máximo: ', maximo)


    # ---------------- ACHANDO OS OUTLIERS ----------------
    df_outliers_inferiores = df_estelionato[df_estelionato['estelionato'] < limite_inferior]
    df_outliers_superiores = df_estelionato[df_estelionato['estelionato'] > limite_superior]

    print('\nMeses/Ano com outliers inferiores: ')
    print(30*'-')
    if len(df_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_outliers_inferiores.sort_values(by='estelionato'))

    print('\nMeses/Ano com outliers superiores: ')
    print(30*'-')
    if len(df_outliers_superiores) == 0:
        print('Não existem outliers superiores!')
    else:
        print(df_outliers_superiores.sort_values(by='estelionato', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de estelionato: {e}')
    exit()


# ---------------- EXTRA: NÃO PRECISA PASSAR ------------------------
try:
   
    # MES_ANO - MAIOR
    mes_maior = df_estelionato.loc[
        df_estelionato['estelionato'].idxmax()
    ]

    print('\nMAIOR estelionatos:')
    print(mes_maior)



    # MES_ANO - MENOR
    mes_menor = df_estelionato.loc[
        df_estelionato['estelionato'].idxmin()
    ]

    print('\nMENOR estelionatos:')
    print(mes_menor)



    # ---- ------ PARA CLASSIFICAR 2º, 3º MAIOR ou MENOR ....
    # SEGUNDO MAIOR
    segundo_maior_valor = np.partition(array_estelionato, -2)[-2]  # Pega somente o valor

    # Usa o valor como filtro para localizar mês/ano correspondente
    df_segundo_maior = df_estelionato[
        df_estelionato['estelionato'] == segundo_maior_valor  # Pega a linha correspondente
    ]
    
    print('\n2º Maior valor de estelionato:')
    print(df_segundo_maior)

    
    # SEGUNDO MENOR
    segundo_menor_valor = np.partition(array_estelionato, 1)[1]  # Pega somente o valor

    df_segundo_menor = df_estelionato[
        df_estelionato['estelionato'] == segundo_menor_valor  # Pega a linha correspondente
    ]

    print('\n2º Menor valor de estelionato:')
    print(df_segundo_menor)

except Exception as e:
    print(f'Erro {e}')
