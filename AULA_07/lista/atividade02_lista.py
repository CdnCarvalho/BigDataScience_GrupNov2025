# Lista para armazenar as notas dos 5 estudantes
notas = []

# Coletando as notas dos estudantes
for i in range(5):
    nota = float(input(f"Digite a nota do {i+1}º estudante: "))
    notas.append(nota)

# Processando as notas e verificando a média
for i in range(5):
    media = notas[i]
    if media > 7:
        print(f"Estudante {i+1}: Média {media} - Aprovado!")
    else:
        print(f"Estudante {i+1}: Média {media} - Reprovado!")