# pip install pandas sqlalchemy pymysql

from sqlalchemy import create_engine, text
import pandas as pd

host = 'localhost'
user = 'root'
password = '123456'
database = 'meu_banco_de_dados'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# df = pd.read_sql('minha_tabela', engine)
# print(df.head())

with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT * FROM minha_tabela"))
    for linha in resultado:
        print(linha)


# Para Inserir
inserir_sql = """
INSERT INTO minha_tabela (coluna1, coluna2, coluna3) VALUES
('Arroz (5 kg)', '25,00', 120),
('Feijão (1 kg)', '10,00', 80),
('Macarrão (500 g)', '5,00', 150),
('Óleo de soja (900 ml)', '7,50', 70),
('Açúcar (1 kg)', '4,00', 100),
('Sal (1 kg)', '2,00', 200)
"""

with engine.connect() as conexao:
    conexao.execute(text(inserir_sql))
    conexao.commit()  # Importante para aplicar as mudanças no banco

# não precisa do commit no final
with engine.begin() as conexao:
    conexao.execute(text("INSERT INTO ..."))  # commit automático ao final