# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np

# Carrega a base de dados a partir do arquivo CSV
df_planilha_moveis = pd.read_csv('planilha_moveis.csv')

# Exibe as primeiras linhas para conferência dos dados
print(df_planilha_moveis.head())

# Cria a coluna de Total de Vendas (R$)
# Total de Vendas = quantidade vendida × preço do produto
df_planilha_moveis['Total de Vendas (R$)'] = (
    df_planilha_moveis['Vendidos'] * df_planilha_moveis['Preco']
)

# Exibe algumas colunas para conferência do cálculo
print()
print(df_planilha_moveis[['Produto', 'Total de Vendas (R$)']].head())

# Converte a coluna Total de Vendas em um array NumPy
array_total_vendas = np.array(df_planilha_moveis['Total de Vendas (R$)'])

# Calcula os quartis usando NumPy
q1 = np.quantile(array_total_vendas, 0.25)
q2 = np.quantile(array_total_vendas, 0.50)  # Mediana
q3 = np.quantile(array_total_vendas, 0.75)

# Exibe os resultados
print(f'\nPrimeiro quartil (Q1): {q1:.2f}')
print(f'Segundo quartil (Q2 - Mediana): {q2:.2f}')
print(f'Terceiro quartil (Q3): {q3:.2f}')
