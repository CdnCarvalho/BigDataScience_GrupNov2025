
import pandas as pd

# Criando o dicionário com os dados da tabela
dados = {
    "Código do Produto": [1, 3, 4, 6],
    "Produto": ["Notebook", "Tablet", "Smartwatch", "Fone de Ouvido"],
    "Unidades Vendidas": [120, 210, 150, 175],
    "Cor": ["Preto", "Azul", "Preto", "Vermelho"],
    "Preço por Unidade (R$)": [3500.00, 1200.50, 900.75, 200.50],
    "Satisfação": ["Alto", "Médio", "Alto", "Médio"]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)
