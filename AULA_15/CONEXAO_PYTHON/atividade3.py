# EXEMPLO – Consulta de Clientes com Ensino Superior
from sqlalchemy import create_engine, text
import pandas as pd

# Função para mostrar resultados
def mostrar_resultados(resultados):
    # Visualiza os resultados
    for item in resultados:
        print(
            f"Nome: {item[0]} {item[1]}, "
            f"Gênero: {item[2]}, "
            f"Estado Civil: {item[3]}, "
            f"Filhos: {item[4]}, "
            f"Escolaridade: {item[5]}"
        )

# Função conecta
def conecta_banco(query, host, user, password, database):
    # URL de conexão com o banco
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    # Estabelece a conexão
    with engine.connect() as conexao:
        result = conexao.execute(text(query))
        return result


# --------------------------- Início do código principal ------------------
# Variáveis de conexão
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_exemplo_aula_01'

# Consulta SQL (os alunos trocarão apenas este trecho)
consulta = """
SELECT Primeiro_Nome, Sobrenome, Genero, Estado_Civil, Num_Filhos, Nivel_Escolar
FROM cadastro_clientes
WHERE Nivel_Escolar = 'Superior Completo'
  AND Estado_Civil = 'C'
  AND Num_Filhos > 2
"""

resultados = conecta_banco(consulta, host, user, password, database)

# df_clientes = pd.DataFrame(resultados.mappings().all())
# print(df_clientes)

mostrar_resultados(resultados)
