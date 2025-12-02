# ATIVIDADE
# Notas dos alunos
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
optativa = float(input("Digite Optativa: "))

if optativa != -1 and optativa > n1 or optativa > n2:
    if n2 < n1:
        n2 = optativa
    else:
        n1 = optativa

media = (n1 + n2) / 2

match media:
    case m if m >= 6:
        print(f"Aluno Aprovado com média {media}")
    case m if 3 <= m < 6:
        print(f"Aluno em Recuperação com média {media}")
    case _:
        print(f"Aluno Reprovado com média {media}")