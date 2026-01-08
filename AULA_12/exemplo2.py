import pandas as pd

# Criando uma lista de quantidades em estoque para diferentes produtos
produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera', 'Notebook']
qtds_estoque = [16, 28, 19, 13, 26, 9]


estoque = pd.Series(qtds_estoque, index=produtos)

# Exibindo a série
print("Série Estoque de Produtos:")
print(estoque)

# Selecionando um valor específico pelo índice
print("\nQuantidade de notebooks em estoque:")
print(estoque['Notebook'])

# # Selecionando múltiplos valores
print("\nEstoque de Notebook e Câmera:")
print(estoque[['Notebook', 'Câmera']].values)  # Mostra apenas os valores
print(estoque[['Notebook', 'Câmera']])  # Mostra com os índices

# Filtrando produtos com estoque abaixo de 20
print("\nProdutos com estoque abaixo de 20 unidades:")
print(estoque[estoque < 20])

# Filtrando por índices "que são textos"
print('\nProdutos no estoque, que iniciam com Smart')
print(estoque[estoque.index.str.startswith('Smart')])  # Inicia com Smart
print(estoque[estoque.index.str.contains('Smart')])  # Contém Smart
print(estoque[estoque.index.str.endswith('phone')])  # Finaliza dom phone


# --------------------------------------------------------------------------- Operação aritmética: 
# Aumentar estoque em 5 unidades
print("\nAumentando o estoque em 5 unidades para todos os produtos:")
print(estoque + 5)

# Incluindo um valor nulo para simular a falta de dados
estoque['Headphone'] = None  # Em casos reais, é melhor prática é usar da seguinte maneira estoque.loc['Headphone'] = None
print("\nEstoque com um valor nulo (Headphone):")
print(estoque)

# Operações Aritméticas entre Séries (Criando outra série com preços dos produtos)
precos = pd.Series([3500, 2500, 1200, 900, 1500, 2600], index=produtos)

# # Calculando o valor total do estoque (preço * quantidade)
print("\nValor total do estoque por produto (preço * quantidade):")
print(precos * estoque)
