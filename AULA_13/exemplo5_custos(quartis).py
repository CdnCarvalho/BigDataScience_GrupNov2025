# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np
import os

# Carrega a base de dados a partir do arquivo CSV
os.system('cls')
df_planilha_custos = pd.read_csv('planilha_de_custos.csv')
print(df_planilha_custos.head())

# Cria a coluna de Custo Total (R$)
# O imposto é calculado diretamente na expressão, sem gerar coluna intermediária
df_planilha_custos['Custo Total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] +
    df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)'] / 100 +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
)

# Exibe algumas colunas para conferência do cálculo
print()
print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head())

# Converte a coluna Custo Total em um array NumPy
array_custo_total = np.array(df_planilha_custos['Custo Total (R$)'])

# Calcula os quartis usando NumPy
q1 = np.quantile(array_custo_total, 0.25)
q2 = np.quantile(array_custo_total, 0.50)  # Mediana
q3 = np.quantile(array_custo_total, 0.75)

# Exibe os resultados
print(f'\nPrimeiro quartil (Q1): {q1:.2f}')  # 25% dos produtos têm custo total até R$ 1.667,77
print(f'Segundo quartil (Q2 - Mediana): {q2:.2f}')  # Metade dos produtos custa até R$ 3.133,31
print(f'Terceiro quartil (Q3): {q3:.2f}')  # 75% dos produtos custam até R$ 4.479,05
# Produtos mais caros e estratégicos, Maior impacto no caixa
# Normalmente exigem: Margem maior, Controle de estoque, Planejamento de vendas

# Os Quatis:
# Os custos não são homogêneos. 
# Os quartis ajudam a: Identificar faixas de custo, Definir políticas de preço, 
# Separar produtos de baixo, médio e alto risco
# Quartis transformam números em decisões.
