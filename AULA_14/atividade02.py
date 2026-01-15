import pandas as pd
import numpy as np


# ------------------------------------------------------------------
# Passo 1: Carregando a planilha de vendas de uma loja de roupas
df_roupas = pd.read_excel('vendas_roupas.xlsx')

# Passo 2: Exibindo as 10 primeiras linhas da planilha
print("\nAs primeiras 10 linhas da planilha:")
print(df_roupas.head(5))


# Delimitando as váriáveis
df_roupas_delimitada = df_roupas[['Produto', 'Faturamento Total (R$)']]

# Agrupando os produtos e somando o faturamento total
df_roupas_delimitada = df_roupas_delimitada.groupby('Produto').sum('Faturamento Total (R$)').reset_index()

# Mostrando o DataFrame ordenado pela coluna de faturamento
print(df_roupas_delimitada.sort_values(by='Faturamento Total (R$)', ascending=True))


#  ------------------ Calculando Estatística -------------------------------
# Criar um array numpy
array_faturamento = np.array(df_roupas_delimitada['Faturamento Total (R$)'])

media = np.mean(array_faturamento)
mediana = np.median(array_faturamento)

# Calcular os quartis
q1 = np.quantile(array_faturamento, 0.25)
q2 = np.quantile(array_faturamento, 0.50)
q3 = np.quantile(array_faturamento, 0.75)

print("\nImprimindo as Medidas:")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Quartil 1 (Q1): {q1}")
print(f"Quartil 2 (Q2): {q2}")
print(f"Quartil 3 (Q3): {q3}")

