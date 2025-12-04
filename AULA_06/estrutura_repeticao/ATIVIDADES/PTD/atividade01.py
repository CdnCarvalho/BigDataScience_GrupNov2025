print(30*"=")
print("Análise de Desempenho Escolar")
print(30*"=")

for aluno in range(10):
    print(f"\n--- Estudante {aluno + 1} ---")

    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    n4 = float(input("Digite a 4ª nota: "))

    media = (n1 + n2 + n3 + n4) / 4
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")


# --------------------------------------------------------------
# ########### MELHORANDO A ATIVIDADE ##############
print(40*"=")
print("Análise de Desempenho Escolar Melhorado")
print(40*"=")

# SUGESTÃO DO PROFESSOR
# qtd = int(input("Notas para quantos alunos? "))
# for aluno in range(qtd): 
for aluno in range(10):
    print(f"\n--- Estudante {aluno + 1} ---")

    soma_notas = 0

    # segundo FOR coleta das 4 notas
    for n in range(4):
        nota = float(input(f"Digite a {n}ª nota: "))
        soma_notas += nota

    media = soma_notas / 4
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")



# ----------------------------------------------------
# QUANDO NÃO SABEMOS O NÚMERO DE REPETIÇÕES
# ----------------------------------------------------
print(40*"=")
print("Análise de Desempenho Escolar Melhorado")
print(40*"=")

contador = 1   # apenas para numerar os estudantes
continuar = "N"   # começa assumindo que queremos iniciar

while continuar.upper() != "S":
    print(f"\n--- Estudante {contador} ---")

    soma_notas = 0

    # Coleta das 4 notas
    for n in range(4):
        nota = float(input(f"Digite a {n + 1}ª nota: "))
        soma_notas += nota

    media = soma_notas / 4
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    # Pergunta se deseja encerrar
    continuar = input("\nDeseja encerrar o programa? (S/N): ")
    contador += 1

print("\nPrograma encerrado.")
