# Criar a lista com a média dos alunos
# Números: NÃO há a necessidade de aspas " ". 
# Estas são utilizadas somente em textos/string
medias_alunos = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5, 4.5, 10.0]

# exibir lista de médias
print(medias_alunos)

# definição de constantes
MEDIA_APROVACAO = 7.0
MEDIA_REPROVACAO = 5.0

# Percorrer o conjunto (lista) de médias
for media in medias_alunos:
    if media >= MEDIA_APROVACAO:
        print(f"A média é {media}. Aprovado!")
    elif media >= MEDIA_REPROVACAO and media < MEDIA_APROVACAO:
        print(f"A média é {media}. Em recuperação.")
    else:
        print(f"A média é {media}. Reprovado! :(")