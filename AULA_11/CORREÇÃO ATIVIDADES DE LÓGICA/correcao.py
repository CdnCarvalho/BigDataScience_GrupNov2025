# ATIVIDADE
# NOTAS DAS PROVAS E PROVA OPTATIVA
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


# -----------------------------------------------------
# Ordenar os números em ordem crescente
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 <= n2 and n1 <= n3:
    menor = n1
    if n2 <= n3:
        meio = n2
        maior = n3
    else:
        meio = n3
        maior = n2

elif n2 <= n1 and n2 <= n3:
    menor = n2
    if n1 <= n3:
        meio = n1
        maior = n3
    else:
        meio = n3
        maior = n1

else:
    menor = n3
    if n1 <= n2:
        meio = n1
        maior = n2
    else:
        meio = n2
        maior = n1

print("Os números em ordem crescente são:", menor, meio, maior)