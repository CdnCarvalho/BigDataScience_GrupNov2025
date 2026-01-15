import pandas as pd 
import numpy as np

# Carrega a base de dados
df_chocolate = pd.read_csv('chocolate sales.csv')
print(df_chocolate.head())

# Tratando a coluna Amount (removendo símbolo e separador de milhar)
df_chocolate['Amount'] = (
    df_chocolate['Amount']
    .str.replace('$', '')
    .str.replace(',', '')
    .astype(float)
)

# Cria a coluna Value per Box (valor médio por caixa)
df_chocolate['Value per Box'] = (
    df_chocolate['Amount'] / df_chocolate['Boxes Shipped']
).round(2)

# Conferência das informações
print()
print(df_chocolate.head())

# Converte a coluna em array NumPy
array_value_per_box = np.array(df_chocolate['Value per Box'])

# Média e mediana
media_valor_caixa = np.mean(array_value_per_box)
mediana_valor_caixa = np.median(array_value_per_box)

# Quartis
q1 = np.quantile(array_value_per_box, .25)
q2 = np.quantile(array_value_per_box, .50)
q3 = np.quantile(array_value_per_box, .75)

# Exibe os resultados
print(f'\nMédia do valor por caixa: {media_valor_caixa:.2f}')
print(f'Mediana do valor por caixa: {mediana_valor_caixa:.2f}')
print(f'1º Quartil: {q1:.2f}')
print(f'2º Quartil: {q2:.2f}')
print(f'3º Quartil: {q3:.2f}')
