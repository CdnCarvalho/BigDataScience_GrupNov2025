import pandas as pd

# Dicionário de dados. As chaves do dicionário são os nomes das colunas e os valores das chaves são as listas com os dados.
data = {
    'Nome': ['Maria', 'João', 'Isabela'],
    'Idade': [20, 42, 39],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.65, 1.74, 1.81]
}

# Criando um DataFrame a partir do dicionário 'data'. O DataFrame organiza os dados em uma estrutura tabular.
df = pd.DataFrame(data)

# Exibindo o DataFrame
print(df)
 
# print(30*'=')
# print('Exibindo os Nomes: ')
# print(df['Nome'])

# ----------------------------------- ATIVIDADE ----------------------------------
# -----------------------------
# Variáveis qualitativas
# -----------------------------
# Qualitativa nominal
print("Qualitativa Nominal:")
print(df['Nome'])
print(df['Genero'])


# -----------------------------
# Variáveis quantitativas
# -----------------------------
# Quantitativa discreta
print("\nQuantitativa Discreta:")
print(df['Idade'])

# Quantitativa contínua
print("\nQuantitativa Contínua:")
print(df['Altura'])