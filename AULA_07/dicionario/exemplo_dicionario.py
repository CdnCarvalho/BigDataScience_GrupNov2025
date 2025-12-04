notas = {}
notas["Matemática"] = 8.5
notas["Português"] = 7.0
notas["História"] = 9.2

print(notas)

print(notas["Português"])  # nota de português
notas["Matemática"] = 9.0  # alterando a nota de matemática
notas["Ciências"] = 8.0    # adicionando a nota de ciências
del notas["História"]   # removendo a nota de história

# ------------------------------------------------------------------------
# dicionario = {} - Cria vazio
# dicionario["chave"] = valor - Adiciona/Modifica
# print(dicionario["chave"]) - Acessa valor
# del dicionario["chave"] - Remove item
# dicionario.clear() - Limpa tudo
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Lista para armazenar os livros
livros = []

# Cadastro de 3 livros
for i in range(3):
    print(f"\nCadastro do {i+1}º livro:")

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    genero = input("Gênero: ")
    paginas = int(input("Número de páginas: "))

    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'genero': genero,
        'paginas': paginas
    }

    livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Mostra todos os livros
print("\n--- TODOS OS LIVROS CADASTRADOS ---")
for livro in livros:
    print(livro)
# ------------------------------------------------------------------------



# ------------------------------------------------------------------------
# DICIONÁRIO PARA ARMAZENAR 5 NÚMEROS COM CHAVES PERSONALIZADAS
valores = {}

# Leitura dos números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    valores[f"numero{i+1}"] = numero

# Mostrando os dados
print("\nNúmeros no dicionário:", valores)

# Acessando um número pela chave
print("Número com chave 'numero3':", valores['numero3'])

# Alterando o valor da chave 'numero3'
valores['numero3'] = 77
print("Dicionário após alteração:", valores)

# Adicionando um novo número
valores['numero6'] = 55
print("Dicionário com novo número:", valores)

# Removendo uma chave
del valores['numero2']
print("Dicionário após remoção:", valores)

# Apaga todas as chaves
valores.clear()

# Pegando a primeira chave e o primeiro valor
# O método list() converte em tupla
primeira_chave = list(valores.items())[0]
print(primeira_chave)

# Enumerate impprime os índices na primeira variável e as
# chaves, valores ou ítens "o par chave valor" na segunda variável
for i, c in enumerate(valores.keys()):
    print(i, c)
