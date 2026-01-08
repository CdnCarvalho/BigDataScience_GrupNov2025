import pandas as pd

# Criando um dicionário com os dados. As chaves representam os
# nomes das colunas e os valores são listas com os dados.
data = {
    'Nome': ['Maria', 'João', 'Isabela'],
    'Idade': [20, 42, 39],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.65, 1.74, 1.81]
}

# Criando um DataFrame a partir do dicionário 'data'.
# O DataFrame organiza os dados em uma tabela.
df = pd.DataFrame(data)

# Exibindo o DataFrame completo com todas as colunas:
# Nome, Idade, Gênero # e Altura
print(f'\n {df}')
 
print(30*'=')

print('Exibindo Idade: ')
print(df['Idade'])

print('\nExibindo Altura: ')
print(df['Altura'])

print('Exibindo Nome: ')
print(df['Nome'])
