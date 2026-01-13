import pandas as pd

# Passo 1: Carregando a planilha de vendas de uma loja de roupas
df_roupas = pd.read_excel('vendas_roupas.xlsx')

# Passo 2: Exibindo as 10 primeiras linhas da planilha
print("\nAs primeiras 10 linhas da planilha:")
print(df_roupas.head(5))

# Passo 3: Análise de dados

# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(df_roupas['Unidades Vendidas'].sum())

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(df_roupas['Preço por Unidade (R$)'].mean())

# Maior valor de faturamento total
print("\nMaior valor de faturamento total:")
print(df_roupas['Faturamento Total (R$)'].max())
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmax(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmax()])  # Mostra todas as informações da linha do menor valor

# Menor faturamento total
print("\nMenor valor de Faturamento total:")
print(df_roupas['Faturamento Total (R$)'].min())
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmin(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmin()])  # Mostra todas as informações da linha do menor valor

# Menor nível de satisfação
print("\nProdutos com menores níveis de satisfação:")
print(df_roupas[df_roupas['Satisfação'] == 'Baixo'])



# ---------------------------------------- Outros Métodos --------------------------

# Produtos com faturamento acima da média
print("\nProdutos acima da média de faturamento:")
media = df_roupas['Faturamento Total (R$)'].mean()

print(df_roupas.loc[
    df_roupas['Faturamento Total (R$)'] >= media,
    ['Produto', 'Faturamento Total (R$)']
])


# Mostra os nomes dos produtos e seus preços
print("\nProdutos e preços:")
print(df_roupas[['Produto', 'Preço por Unidade (R$)']].value_counts())

# Quantas vezes cada preço aparece
print("\nFrequência dos preços:")
print(df_roupas['Preço por Unidade (R$)'].value_counts())

# Retorna o valor mais frequente (moda)
print("\nModa do preço por unidade:")
print(df_roupas['Preço por Unidade (R$)'].value_counts().index[0])

# Retorna quantas vezes o valor mais frequente aparece
print("\nFrequência da moda:")
print(df_roupas['Preço por Unidade (R$)'].value_counts().iloc[0])

# Retorna o número que é a moda usando o método específico
print("\nModa (usando mode):")
print(df_roupas['Preço por Unidade (R$)'].mode())

# Resumo estatístico (média, desvio padrão, quartis, etc.)
print("\nResumo estatístico:")
print(df_roupas.describe())
