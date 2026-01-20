
# EXEMPLO 3
from sqlalchemy import create_engine, text
import pandas as pd


def mostrar_resultados(resultados):
    # Visulaliza os resultados
    for item in resultados:
        print(f"Produto: {item[0]},Data da Venda: {item[1]},\
                Categoria: {item[2]}, Loja: {item[3]},\
                Valor: {item[4]}, Quantidade: {item[5]}")
        

def conecta_banco(query, host, user, password, database):
    # URL de conexão com o banco, usando SQLAlchemy e PyMySQL
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    # Estabelece a conexão
    with engine.connect() as conexao:
        # 'text(consulta)' transforma a string da consulta em um objeto compatível com SQLAlchemy.
        # 'conexao.execute' executa essa consulta no banco de dados.
        result = conexao.execute(text(query))

        return result


# ------------------------------------  --------------  Início do código principal
# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_exemplo_aula_01'

# Query: "Linguagem SQL para selecionar todos os registros da tabela vendas"
consulta = "SELECT * FROM vendas WHERE Categoria = 'Eletrônicos'"

resultados = conecta_banco(consulta, host, user, password, database)

# Transformando em DataFrame do Pandas
# df_vendas_eletronicos = pd.DataFrame(resultados.mappings().all())
# print(df_vendas_eletronicos)

mostrar_resultados(resultados)






