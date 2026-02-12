import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Conectando ao dados
try:
    print('Obtendo dados...')

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')   # 'utf-8', 'iso-8859-1', latin1, cp1252

    # Padronizando nome da região
    df_ocorrencias.loc[df_ocorrencias['regiao'].str.contains('Grande Niter', na=False), 'regiao'] = 'Interior'
    print(df_ocorrencias['regiao'].unique())


    # significa que haverá uma quebra de linha
    df_ocorrencias = df_ocorrencias[
        (df_ocorrencias['ano'] >= 2003) & (df_ocorrencias['ano'] <= 2026)
    ]

    # Filtragem por região
    df_ocorrencias = df_ocorrencias[df_ocorrencias['regiao'] == 'Grande Niterói']

    # Delimitando as variáveis
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Agrupando e quantificando
    # df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()

    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados {e}')


# Obter informações do padrão de roubos de veículos
try:
    print('Obtendo informações do padrão de roubos de veículos')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # medidads de tendência central
    media = np.mean(array_roubo_veiculo)
    mediana = np.median(array_roubo_veiculo)
    distancia_media_mediana = (media - mediana) / mediana


    print(f'\nMédia: {media:.3f}')
    print(f'Mediana: {mediana}')
    print(f'Distância Média e Mediana: {distancia_media_mediana:.3f}')

except Exception as e:
    print(f'Erro ao obter informações... {e}')


# Obtendo medidas estatísticas
try:

    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print('\nMedidas de Posição:')
    print(30*'=')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    # menores
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # maiores
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMenores')
    print(30*'=')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo'))
    
    print('\nMaiores')
    print(30*'=')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))


    # Mdidas de Dispersão
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude_total = maximo - minimo

    print('\nPrintando Medidas de Dispersão:')
    print(30*'=')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude_total}')


    # Intervalo interquartil
    iqr = q3 - q1
    

    # Limite Inferior
    limite_inferior = q1 - (1.5 * iqr)

    # Limite superior
    limite_superior = q3 + (1.5 * iqr)

    print('\nMedidas de Dispersão')
    print(30*'=')
    print(f'IQR: {iqr}')
    print(f'Limite Inferior {limite_inferior}')
    print(f'Limite Superior {limite_superior}')


    # Outliers Inferiores:
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # Outliers superiores:
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nOutliers Inferiores:')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não há outliers inferiores')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))


    print('\nOutliers Superiores:')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não há outliers superiores')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))
    

except Exception as e:
    print(f'Erro ao obter medidas estatísticas {e}')


# Medidas de Dispersão
try:
    print('Obtendo medidas de dispersão...')

    # Variância: Observar a dispersão dos dados
    # Observa-se em relação a média
    # É a média dos quadrados das diferenças entre cada valor e a média
    # O resultado da variância está elevado ao quadrado

    # variância
    variancia = np.var(array_roubo_veiculo)

    # Distância entre a variância e a média
    distancia_variancia_media = variancia / (media ** 2) * 100

    # Desvio Padrão
    # Observa-se também em relação a média
    # O desvio padrão é a Raiz Quadrada da Variância
    # Apresenta os dados. O quanto cada valor está se afastando da média, 
    # tanto para mais ou para menos
    desvio_padrao = np.std(array_roubo_veiculo)

    # Coeficiente de Variação
    # É a magnitude do desvio padrão em relação a média
    coef_variacao = desvio_padrao / media


    print(f'Variância: {variancia}')
    print(f'Distância Variância p/ Média: {distancia_variancia_media}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coeficiente de Variação: {coef_variacao}')
    
except Exception as e:
    print(f'Erro ao calcular medidas de dispersão: {e}')


# Medidas de Distribuição
try:
    print('Calculando medidas de distribuição...')
    # Assimetria
    # Descreve se a distribuição é simétrica ou assimétrica
    # Indica como os dados estão distribuídos em torno do centro.
    # Concentração em qual lado?

    # Pontos de Observação:
    # -0.5 a 0.5 => Mais simétrica
    #  Entre 0.5 e 1 => Assimetria Moderada
    #  Acima de 1 => Assimetria Alta
    assimetria = df_roubo_veiculo['roubo_veiculo'].skew()
    print(f'Assimetria: {assimetria}')

    # Curtose
    curtose = df_roubo_veiculo['roubo_veiculo'].kurtosis()
    print(f'Curtose: {curtose}')

except Exception as e:
    print(f'Erro ao calcular medidas de distribuição: {e}')


# Visualizando os dados
try:
    print('Visualizando os Dados')
    import matplotlib.pyplot as plt

    plt.subplots(2, 2, figsize=(16, 7))
    
    # POSIÇÃO 1
    # Boxplot
    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)



    # POSIÇÃO 2
    # Plotagem do Histograma
    plt.subplot(2, 2, 2)
    plt.hist(array_roubo_veiculo, bins=198, edgecolor='black')
    plt.title('Frequência dos roubos')
    
    # ---------------------------------------------------------------
    # Printar no terminal as faixas do histograma
    contagens, limites = np.histogram(array_roubo_veiculo, bins=158)
    print('\nFaixas do histograma:\n')
    for i in range(len(contagens)):
        print(
            f'Faixa {i+1}: '
            f'{limites[i]:.0f} até {limites[i+1]:.0f} roubos '
            f'=> {contagens[i]} municípios'
        )
    # ---------------------------------------------------------------
    


    # POSIÇÃO 3
    # Plotando as medidas estatísticas
    plt.subplot(2, 2, 3)
    plt.text(0.1, 0.9, f'Média: {media}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor Valor: {minimo}', fontsize=12)
    plt.text(0.1, 0.5, f'Limite Inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite Superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Máximo: {maximo}', fontsize=12)
        
    plt.text(0.6, 0.9, f'Amplitude: {amplitude_total}', fontsize=12)
    plt.text(0.6, 0.8, f'IQR: {iqr}', fontsize=12)

    # POSIÇÃO 4
    # Gráfico de Barras - Ranking dos outliers superiores
    plt.subplot(2, 2, 4)
    # Ordenando para exibição de todos os outliers superiores
    # df_roubo_veiculo_outliers_superiores_ordenados = (
    #     df_roubo_veiculo_outliers_superiores.sort_values(
    #         by='roubo_veiculo', ascending=True
    #     )
    # )
    
    # Ordenando para exibição dos 10 maiores outliers superiores
    df_roubo_veiculo_outliers_superiores_ordenados = (
        df_roubo_veiculo_outliers_superiores
            .sort_values(by='roubo_veiculo', ascending=False)
            .head(10)
            .sort_values(by='roubo_veiculo', ascending=True)
    )

    # Plotando o gráfico de barras horizontais
    plt.barh(
        df_roubo_veiculo_outliers_superiores_ordenados['munic'],
        df_roubo_veiculo_outliers_superiores_ordenados['roubo_veiculo'],
    )

    plt.title('Ranking dos Municípios com outliers superiores')


    plt.show()

except Exception as e:
    print(f'Erro na plotagem do painéml {e}')