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

# --------------- ------------- Outros Métodos ------------ -------------------
# Mostra os nomes dos produtos e preços
print(df[['Produto', 'Preço por Unidade (R$)']].value_counts())

# Quantas vezes cada valor aparece
print(df['Preço por Unidade (R$)'].value_counts())

# Retorna o nº que é a moda
print(df['Preço por Unidade (R$)'].value_counts().index[0])  

# Retorna o número de vezes que o valor mais frequente aparece
print(df['Preço por Unidade (R$)'].value_counts().iloc[0])

# Retorna o índice da moda e a moda
print(df['Preço por Unidade (R$)'].mode())  

# Mostra max, min, média, counts, desvio padrão std, quartis
print(df.describe())
