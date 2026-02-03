import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # demilitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo_veiculo por munic
    # df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()  # modo antigo

    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()  # Versão mais nova do pandas


    # Exemplo de como somar duas variáveis quantitativa do ponto de vista de uma qualitativa (munic)
    # df_roubo_e_furto_veiculos = (
    #     df_ocorrencias.groupby('munic', as_index=False)
    #     .agg({
    #         'roubo_veiculo': 'sum',
    #         'furto_veiculo': 'sum'
    #     })
    # )

    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# obter informações sobre padrão de roubo_veiculo
try:
    print('Obtendo informações sobre padrão de roubo de veículos...')

    # array é uma estrutura de dados que armazena uma coleção de dados
    # e computacionalmente é mais eficiente para calcular estatísticas
    # Faz parte da biblioteca numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # média de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    # mediana de roubo_veiculo
    # divide a distribuição em duas partes iguais (50% dos dados abaixo e 50% acima)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # distânicia
    distancia = abs((media_roubo_veiculo-mediana_roubo_veiculo)/mediana_roubo_veiculo)

    # Medidas de tendência central
    # Se a média for muito diferente da mediana, distribuição é assimétrica. Não tende a haver um padrão
    # e pode ser que existam outliers (valores discrepantes)
    # Se a média for próxima (25%) a mediana, distribuição é simétrica. Tende a haver um padrão
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia}')


    # Quartis
    # Método padrão é o weibull 
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull') # Q1 é 25% 
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull') # Q2 é 50% (mediana)
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull') # Q3 é 75%

    # # medidas de posição (ou de dispersão)
    # print('\nMedidas de posição: ')
    # print(30*'-')
    # print(f'Q1: {q1}')
    # print(f'Q2: {q2}')
    # print(f'Q3: {q3}')


    # MENORES ROUBOS
    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo abaixo q1
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # MAIORES ROUBOS
    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo acima q3
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMunicípios com qtdes menores de roubo de veículos: ')
    print(30*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))

    print('\nMunicípios com qtdes maiores de roubo de veículos: ')
    print(30*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))


    # ------------------------ II - PARTE (ANTES DE ACHAR OS OUTLIERS) ------------------------
    # Medidas de dispersão
    # Amplitude total
    # Maior valor - menor valor
    # Quanto mais próximo de zero, maior a homogeinidade dos dados
    # Se for igual a zero, todos os valores são iguais
    # Quanto masi próximo do máximo, maior a dispersão dos dados ou heterogeneidade
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)


    # IQR (Intervalo interquartil)
    # q3 - q1
    # é a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. Max e min estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # quanto mais próximo de zero, mais homogêneo são os dados
    # quanto mais próximo do q3, mais heterogêneo são os dados
    iqr = q3 - q1

    # limite superior
    # vai identificar os outliers acima de q3
    limite_superior = q3 + (1.5 * iqr)

    # limite inferior
    # vai identificar os outliers abaixo de q1
    limite_inferior = q1 - (1.5 * iqr)


    # medidas de posição (ou de dispersão)
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
    

    # ---------------- ACHANDO OS OUTLIERS ---------------
    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo abaixo q1
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo acima q3
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nMunicípios com outliers inferiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))


    print('\nMunicípios com outliers superiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()


# Medidas de Dispersão
try:
    print('Calculando medidas de dispersão...')

    # Variância
    # É uma medida para obsersar a dispersão dos dados 
    # Observa-se em relação a média
    # É a média dos quadrados das diferenças entre cada valor e a média
    # O resultado da variância etá elevado ao quadrado

    # Interpretação
    # Quanto maior a variância, maior é o afastamento dos valores em relação à média.
    # Neste caso, a variância elevada indica alta dispersão dos dados.
    variancia = np.var(array_roubo_veiculo)


    # Distância da variância para a média
        # Distância <= |10%| : Baixa dispersão dos dados em relação a média
        # Distância > |10%| e distância < |25%|: Dispersão moderada dos dados em relação a média
        # Distâcia >= |25%|: Alta dispersão dos dados em relação a média
    distancia_var_media = variancia / (media_roubo_veiculo ** 2)

    # Desvio padrão é a raiz quadrada da variância
    # Desvio padrão é a normalização da variância, por isso mais fácil de interpretar
    # Apresentar o quanto os dados estão afastados da média (para mais ou para menos). Valor absoluto
    desvio_padrao = np.std(array_roubo_veiculo)

    # Coeficiente de variação
    # É a magnitude do desvio padrão em realção a média
    coef_variacao = desvio_padrao / media_roubo_veiculo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Dist. var x média: {distancia_var_media}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coef. variação: {coef_variacao}')

except Exception as e:
    print(f'Erro ao calcular as medidas de dispersão: {e}')
    exit()



# visualizar os dados
try:
    print('Visualizando os dados...')

    # matplotlib é uma biblioteca para visualização de dados
    # site é https://matplotlib.org/
    # pip install matplotlib

    plt.subplots(2,2, figsize=(16,7))
    plt.suptitle('Análise de roubo de veículos no RJ')



    # --- POSIÇÃO 1: bloxplot sem outliers
    plt.subplot(2,2,1)
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)  # showfliers=False retira os outliers
    plt.title('Boxplot com outliers')



    # --- POSIÇÃO 2: Colunas com os municípios de menores roubos
    plt.subplot(2,2,2)
    # Ordenar os municípios com menores roubos do menor para o maior
    df_roubo_veiculo_menores_ordered = (
        df_roubo_veiculo_menores
            .sort_values(by='roubo_veiculo', ascending=True)
    )

    # Gráfico de colunas
    plt.bar(
        df_roubo_veiculo_menores_ordered['munic'],
        df_roubo_veiculo_menores_ordered['roubo_veiculo']
    )

    plt.title('Municípios com menores roubos de veículos')
    plt.xticks(rotation=90)
    plt.xticks([])  # desativar os rótulos do eixo x para melhor visualização




    # --- POSIÇÃO 3: Ranking das cidades outliers superiores
    plt.subplot(2,2,3)

    # Todos ou ou Top 10 mais abixo
    # Ordenar (Todos os outliers)
    df_roubo_veiculo_outliers_superiores_ordered = ( 
        df_roubo_veiculo_outliers_superiores.sort_values(
            by='roubo_veiculo', ascending=True
        )        
    )

    # Ordenar, filtrar top 10 e reordenar para o gráfico horizontal
    df_roubo_veiculo_outliers_superiores_ordered = (
        df_roubo_veiculo_outliers_superiores
            .sort_values(by='roubo_veiculo', ascending=False) # primeiro ordena do maior para o menor
            .head(10)  # pega os 10 primeiros
            .sort_values(by='roubo_veiculo', ascending=True)  # ordena do menor para o maior para melhor exibição
    )

    # Monstando o gráfico de barrs
    plt.barh(
        df_roubo_veiculo_outliers_superiores_ordered['munic'], 
        df_roubo_veiculo_outliers_superiores_ordered['roubo_veiculo']
    )
    
    plt.title('Ranking dos municípios com outliers superiores')



    # --- POSIÇÃO 4: Medidas descritivas
    plt.subplot(2,2,4)

    plt.text(0.0, 0.9, f'Média: {media_roubo_veiculo}', fontsize=12)
    plt.text(0.0, 0.8, f'Mediana: {mediana_roubo_veiculo}', fontsize=12)
    plt.text(0.0, 0.7, f'Distância: {distancia}', fontsize=12)
    plt.text(0.0, 0.6,f'Menor valor: {minimo}', fontsize=12)
    plt.text(0.0, 0.5,f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.0, 0.4,f'Q1: {q1}', fontsize=12)
    plt.text(0.0, 0.3,f'Q3: {q3}', fontsize=12)
    plt.text(0.0, 0.2,f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.0, 0.1,f'Maior valor: {maximo}', fontsize=12)
    plt.text(0.0, 0.0,f'Amplitude Total: {amplitude}', fontsize=12)

    # Desvio padrão, distância, coeficiente de variação e variância
    plt.text(0.5, 0.9, f'Desvio Padrão: {desvio_padrao}', fontsize=12)
    plt.text(0.5, 0.8, f'Variância: {variancia}', fontsize=12)
    plt.text(0.5, 0.7, f'Coeficiente de Variação: {coef_variacao}', fontsize=12)
    plt.text(0.5, 0.6, f'Dist. Var x Média: {distancia_var_media}', fontsize=12)

    # desativar os eixos
    plt.axis('off')

    # ajsutar o layout
    plt.tight_layout()

    # exibir o painel
    plt.show()
    
except Exception as e:
    print(f'Erro ao descrever os dados: {e}')
    exit()