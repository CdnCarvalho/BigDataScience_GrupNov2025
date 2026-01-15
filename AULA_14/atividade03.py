import pandas as pd 
import numpy as np


# Atividade 03 CSV do Kaggle
df_chocolate = pd.read_csv('chocolate sales.csv')
print(df_chocolate)

# imprimindo os 10 primeiros registros
print(df_chocolate.head(10))

# Transformando em array numpy
array_chocolate = np.array(df_chocolate['Boxes Shipped'])
print(array_chocolate)

# Calcular Média, mediana
media_vendas = np.mean(array_chocolate)
mediana_vendas = np.median(array_chocolate)

# Quartis
q1 = np.percentile(array_chocolate, 25)
q2 = np.percentile(array_chocolate, 50)
q3 = np.percentile(array_chocolate, 75) 

print(f'\nMédia das vendas: {media_vendas:.2f}')
print(f'Mediana das vendas: {mediana_vendas}')
print(f'1º Quartil: {q1}')
print(f'2º Quartil: {q2}') 
print(f'3º Quartil: {q3}')


# ---------------------------------------------------------------------------
# EXEMPLO ----- PARTE II - LIMPANDO A COLUNA AMOUNT
# ---------------------------------------------------------------------------
# Aplicando na Séries dos Valores "Amount" 
df_chocolate['Amount']  = (
    df_chocolate['Amount']
    .str.replace('$', '')
    .str.replace(',', '')
    .astype(float)   
)

# Transformando em array numpy
array_vlchocolate = np.array(df_chocolate['Amount'])

# Calcular Média, mediana
media_vlvendas = np.mean(array_vlchocolate)
mediana_vlvendas = np.median(array_vlchocolate)     
# Quartis
q1 = np.percentile(array_vlchocolate, 25)
q2 = np.percentile(array_vlchocolate, 50)
q3 = np.percentile(array_vlchocolate, 75)   

print(f'\nMédia das vendas: {media_vlvendas:.2f}')
print(f'Mediana das vendas: {mediana_vlvendas}')
print(f'1º Quartil: {q1}')
print(f'2º Quartil: {q2}') 
print(f'3º Quartil: {q3}')

# Mostrar os 10 maiores ascendentes
# print(df_chocolate.head(10).sort_values(by='Amount', ascending=False))
# Conta as vendas por vendedor, ordena todos e mostra os 5 primeiros
# print(df_chocolate['Sales Person'].value_counts().sort_values(ascending=False).head(5))