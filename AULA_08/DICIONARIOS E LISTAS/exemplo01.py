# Lista para armazenar os alunos
alunos = []

for i in range(3):
    print(f"\n--- Aluno {i+1} ---")
    nome = input("Nome do aluno: ")

    # Recebe 3 notas e guarda dentro de uma lista
    notas = []
    for n in range(3):
        nota = float(input(f"Nota {n+1}: "))
        notas.append(nota)

    # Calcula a média
    media = sum(notas) / 3

    # Dicionário do aluno
    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media
    }

    alunos.append(aluno)

# Exibição dos alunos cadastrados
print("\n--- Dados dos alunos ---")
for a in alunos:
    print(f"Nome: {a['nome']}")
    print(f"Notas: {a['notas']}")
    print(f"Média: {a['media']:.2f}")
    print("-" * 20)
