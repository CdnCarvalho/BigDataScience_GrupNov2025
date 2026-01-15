import pandas as pd
import numpy as np 

# -----------------------------------------------------------
# Lendo um arquivo Excel com o método read_excel (deve apontar para o arquivo real)
df = pd.read_excel('vendas_eletronicos.xlsx')

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas da planilha Excel:")
print(df.head(10))


# Delimitando as váriáveis
df_produtos = df[['Produto', 'Faturamento Total (R$)']]

# Agrupando os produtos e somando o faturamento total
df_produtos = df_produtos.groupby('Produto').sum('Faturamento Total (R$)').reset_index()

# Mostrando o DataFrame ordenado pela coluna de faturamento
print(df_produtos.sort_values(by='Faturamento Total (R$)', ascending=True))


#  ------------------ Calculando Estatística -------------------------------
# Criar um array numpy
array_faturamento = np.array(df['Faturamento Total (R$)'])

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