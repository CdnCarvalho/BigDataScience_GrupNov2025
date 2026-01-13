# Importa a biblioteca Pandas para manipulação de dados e a biblioteca NumPy para operações matemáticas e estatísticas
import pandas as pd
import numpy as np

# Carrega o arquivo Excel com os dados de vendas para um DataFrame (estrutura de dados similar a uma tabela)
df = pd.read_excel('vendas_roupas.xlsx')

# Exibe o conteúdo do DataFrame para visualização geral dos dados
print(df)

# Seleciona a coluna 'Categoria' do DataFrame, que contém as categorias dos produtos
categoria = df['Categoria']

# Seleciona a coluna 'Quantidade Vendida', que contém as quantidades vendidas para cada produto
quantidade_vendida = df['Unidades Vendidas']

# Exibe a coluna 'Quantidade Vendida' para análise visual dos valores de quantidade vendida
print(quantidade_vendida)

# Exibe a coluna 'Categoria' para análise das categorias dos produtos
print(categoria)

# Calcula a média das quantidades vendidas e armazena o resultado na variável 'media'
media = np.mean(quantidade_vendida)

# Calcula a mediana das quantidades vendidas e armazena o resultado na variável 'mediana'
mediana = np.median(quantidade_vendida)

# Exibe a média das quantidades vendidas
print(f'Média: {media}')

# Exibe a mediana das quantidades vendidas
print(f'Mediana: {mediana}')

# Organiza o DataFrame em ordem crescente de 'Quantidade Vendida'
quantidadevdd_organizada = df.sort_values(by='Unidades Vendidas', ascending=True)

# Seleciona a coluna 'Quantidade Vendida' do DataFrame organizado
quantidade_vedida = quantidadevdd_organizada['Unidades Vendidas']

# Exibe os valores da coluna 'Quantidade Vendida' já organizados em ordem crescente
print(quantidade_vedida.values)


# Qual valor mais aparece na amostra?
# qual a quantidade mais comum, e não necessariamente a maior em
# impacto financeiro ou volume total.
# Identificar padrões de compra
# ex: “a maioria dos produtos vende entre 6 e 8 unidades”;
# Planejamento de estoque
# ex: ter mais produtos que vendem em quantidades mais comuns;
moda = df['Unidades Vendidas'].mode()
print('Dos clientes que compraram mais, comparam:')
print(moda)


# Conta quantas vezes, cada valor apareceu na coluna 'Unidades Vendidas'
frequencias = df['Unidades Vendidas'].value_counts()

# Exibe a quantidade de vezes que cada valor como DataFrame.
# O índice da Série é: 8, 6, 7, 9, 10 (Que são os valores únicos).
print('Frequência dos valores:')
print(frequencias)

# Só as modas com suas contagens:
moda = df['Unidades Vendidas'].mode()
print('\nModas e suas frequências:')
for valor in moda:
    print(f'Valor: {valor}, Apareceu: {frequencias[valor]} vezes')