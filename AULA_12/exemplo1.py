import pandas as pd

# Criando uma lista de quantidades em estoque para diferentes produtos
produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera', 'Notebook']
qtds_estoque = [16, 28, 19, 13, 26, 9]

# ------------------------------------------------------------ Séries do Pandas (padrão)
serie_produto = pd.Series(produtos)
serie_qtds = pd.Series(qtds_estoque)
print(serie_produto)
# print(serie_qtds)


print('\n',30*"=")
# Selecionando conteúdo da série
print(f'Série produto na posição 3:  {serie_produto[2]}')  # Selecionando um índice da série
print(serie_produto[[2, 3]])  # Selecionando dois (índice e valor) da série
print(serie_produto[[2, 3]].values)  # Selecionando os valores dos índices

# Filtragem
print(serie_qtds[serie_qtds < 20])  # Filtragem numéricas Séries
print(serie_produto[serie_produto == 'Notebook'])  # Filtragem lógica textos e números em Séries
print(serie_produto[serie_produto.str.startswith('Smart')])  # Filtragem de texto em Séries (inicia com)
print(serie_produto[serie_produto.str.contains('Smart')])  # Filtragem de texto em Séries (em qualquer parte)
print(serie_produto[serie_produto.str.endswith('phone')])  # Filtragem de texto em Séries (finaliza com)

# Operações
serie_qtds = serie_qtds + 10  # aumentando todos os valores nas séries
print(serie_qtds)

serie_qtds[serie_qtds > 30] += 10  # aumenta onde a quantidade é maior que 30
print(serie_qtds)

# Não precisa falar, apenas se um aluno perguntar
# serie_qtds[serie_produto == 'Notebook'] += 50  # aumenta na série a quantidade, no mesmo índice notebook
# print(serie_qtds)

# Operação aritimética entre duas séries
serie_preco = [2999, 1290, 600, 100, 160, 3189]
serie_total_produto = serie_qtds * serie_preco
print(serie_total_produto)

# Estatística:
print(f"\n{30 * '='}")
print(f"Maior valor: {serie_total_produto.max()}")
print(f"Menor valor: {serie_total_produto.min()}")
print(f"Média: {serie_total_produto.mean():.2f}")
print(f"Total: {serie_total_produto.sum()}")


