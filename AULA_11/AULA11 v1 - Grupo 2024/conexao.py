import pandas as pd

from sqlalchemy import create_engine, text

host = 'localhost:3306'
user = 'root'
password = '123456'
database = 'meu_banco_de_dados'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df = pd.read_sql('minha_tabela', con=engine)

print(df.tail(60))

df['coluna2'] = df['coluna2'].str.replace('\r', '').str.replace(',', '.')

# Converter para float, tratando erros
df['coluna2'] = pd.to_numeric(df['coluna2'], errors='coerce')

# Filtrar produtos caros
produtos_caros = df[df['coluna2'] > 10]


query = '''UPDATE minha_tabela SET coluna1 = REPLACE(coluna1, '"', '');'''
with engine.connect() as connection:
    connection.execute(text(query))

query = 'SELECT * FROM minha_tabela;'
df = pd.read_sql(query, engine)

print(30*'===')
print(df)