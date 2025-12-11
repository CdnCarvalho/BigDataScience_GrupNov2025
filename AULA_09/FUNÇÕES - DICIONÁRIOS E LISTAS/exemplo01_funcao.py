# Função
def cadastrar_aluno(qtd_alunos):
    """
    Solicita nome e 3 notas de um aluno,
    retorna um dicionário com nome, lista de notas e média.
    """
    print("\n--- Cadastro dos alunos ---")
    for n in range(qtd_alunos):
        print(30*'=')
        nome = input("Nome do aluno: ")
        notas = []
        
        for n in range(1, 4):
            nota = float(input(f"Nota {n}: "))
            notas.append(nota)
        
        media = sum(notas) / len(notas)

        aluno = {
            "nome": nome,
            "notas": notas,
            "media": round(media, 2)
        }

        print(aluno)
        alunos.append(aluno)



def mostrar_alunos(lista_alunos):
    """
    Recebe uma lista de dicionários de alunos
    e imprime os dados formatados.
    """
    print("\n--- Dados dos alunos ---")
    for a in lista_alunos:
        print(f"Nome: {a['nome']}")
        print(f"Notas: {a['notas']}")
        print(f"Média: {a['media']:.2f}")
        print("-" * 20)


# --- Programa principal ---
# Lista para armazenar os alunos
alunos = []
qtd_alunos = int(input('Quantos alunos quer cadastrar? '))
cadastrar_aluno(qtd_alunos)
mostrar_alunos(alunos)
