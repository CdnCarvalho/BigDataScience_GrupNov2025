# ATIVIDADE 01 - DICIONÁRIO AMIGOS
amigos = {}  # Dicionário vazio

# Adicionando amigos com suas idades
amigos["João"] = 20
amigos["Maria"] = 22
amigos["Carlos"] = 19

print("Idade de Maria:", amigos["Maria"])  # Acessa pelo nome

# Mudando a idade
amigos["Carlos"] = 20

# Adicionando novo amigo
amigos["Ana"] = 21

# Removendo um amigo
del amigos["João"]

print("Todos os amigos:", amigos)
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# ATIVIDADE 02 - DICIONÁRIO PRODUTOS
produtos = {}

# Adicionando produtos
produtos["Arroz"] = 25.90
produtos["Feijão"] = 8.50
produtos["Leite"] = 5.80
print(produtos)  # Mostra todos os produtos do dicionário

# Consultando preço
print("Preço do Arroz:", produtos["Arroz"])

# Promoção no Leite
produtos["Leite"] = 4.00

# Novo produto
produtos["Açúcar"] = 6.30

# Removendo o Feijão
del produtos["Feijão"]

print("Lista de compras:")
print(produtos)
# ----------------------------------------------------------------


# ----------------------------------------------------------
# ATIVIDADE 03 - LISTA DE CANDIDATOS
candidatos = []

# Coleta dos dados
for i in range(5):
    print(f"\nCadastro do {i+1}º candidato:")

    nome = input("Nome completo: ")
    idade = int(input("idade: "))
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    formacao = input("Formação acadêmica: ")

    candidato = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone,
        'email': email,
        'formacao': formacao
    }

    candidatos.append(candidato)
    print("Cadastro realizado com sucesso.")

# Exibe todos os candidatos
print("\nLista de candidatos:")
for c in candidatos:
    print(c)
# ----------------------------------------------------------


# ----------------------------------------------------------
# Lista para armazenar os atletas classificados
atletas_classificados = []

# Tempo máximo para classificação (em segundos)
tempo_maximo = 12.0

print("=" * 50)
print("SELEÇÃO DE ATLETAS - CORRIDA 100 METROS")
print("=" * 50)

# Avaliação de 5 atletas
for i in range(5):
    print(f"\n--- Atleta {i+1} ---")
    nome = input("Nome do atleta: ")
    tempo = float(input(f"Tempo de {nome} nos 100m (segundos): "))
    categoria = input("Categoria (Infantil/Juvenil/Adulto): ")

    # Verifica se o tempo é bom para classificação
    if tempo <= tempo_maximo:
        atleta = {
            'nome': nome,
            'tempo': tempo,
            'categoria': categoria
        }
        atletas_classificados.append(atleta)
        print("Classificado!")
    else:
        print("Não classificado.")

# Exibindo atletas classificados
print("\nAtletas classificados:")
for a in atletas_classificados:
    print(f"{a['nome']} - {a['tempo']}s - {a['categoria']}")