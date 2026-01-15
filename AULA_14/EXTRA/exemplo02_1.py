import pandas as pd

# Lendo um arquivo Excel com o método read_excel (deve apontar para o arquivo real)
df = pd.read_excel('vendas_eletronicos.xlsx')

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas da planilha Excel:")
print(df.head(30))

# Valor máximo de faturamento total
print("\nMaior valor de faturamento total:")
print(df['Faturamento Total (R$)'].max())
print(df.loc[df['Faturamento Total (R$)'].idxmax(), 'Produto'])  # Mostra apenas o nome do produto de maior valor
print(df.loc[df['Faturamento Total (R$)'].idxmax()])  # Mostra todas as informações da linha do maior valor

# Valor menor de faturamento
print("\nMenor valor de faturamento:")
print(df['Faturamento Total (R$)'].min())
print(df.loc[df['Faturamento Total (R$)'].idxmin(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df.loc[df['Faturamento Total (R$)'].idxmin()])  # Mostra todas as informações da linha do menor valor

# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(df['Unidades Vendidas'].sum())

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(df['Preço por Unidade (R$)'].mean())

# Produtos com faturamento acima da média
print("\nProdutos acima da média:")
media = df['Faturamento Total (R$)'].mean()
print(df[df['Faturamento Total (R$)'] >= media])


df_produtos = df[['Produto', 'Faturamento Total (R$)']]

df_produtos = df_produtos.groupby('Produto').sum('Faturamento Total (R$)').reset_index()

# df_produtos = df_produtos.sort_values(by='Faturamento Total (R$)', ascending=False)
print(df_produtos.sort_values(by='Faturamento Total (R$)', ascending=True))


# agrupar por produtos
# df_produtos = df_roupas.groupby(['Produto']).sum('Faturamento Total (R$)').reset_index()

# --------------- ------------- Outros Métodos ------------ -------------------
# # Mostra os nomes dos produtos e preços
# print(df[['Produto', 'Preço por Unidade (R$)']].value_counts())

# # Conta as vezes que cada valor aparece
# print(df['Preço por Unidade (R$)'].value_counts())

# # Moda - Retorna quem é a Moda
# print(df['Preço por Unidade (R$)'].value_counts().index[0])  

# # Retorna o número de vezes que o valor mais frequente aparece
# print(df['Preço por Unidade (R$)'].value_counts().iloc[0])

# # Moda com o índice
# print(df['Preço por Unidade (R$)'].mode())  

# # Mostra max, min, média, counts, desvio padrão std, quartis
# print(df.describe())
