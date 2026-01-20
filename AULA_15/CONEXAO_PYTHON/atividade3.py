from sqlalchemy import create_engine, text

# Dados de conexão
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_exemplo_aula_01'

# Query para buscar produtos com estoque inferior a 2000
query = "SELECT Pais, Produto, Porto, Quantidade FROM importados WHERE Quantidade < 500;"

# Conectando ao banco de dados
try:
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    conexao = engine.connect()
    print("Conectado ao banco de dados com sucesso!")

    # Executando a consulta
    resultados = conexao.execute(text(query))

    # Verificando os resultados
    if resultados.rowcount > 0:
        print("Produtos com estoque baixo:")
        for resultado in resultados:
            print(f"País: {resultado[0]}, Produto: {resultado[1]}, "
                  f"Porto: {resultado[2]}, Estoque: {resultado[3]}")
    else:
        print("Nenhum produto com estoque baixo.")

    # Fechando a conexão
    conexao.close()

except Exception as e:
    print(f"Erro: {e}")