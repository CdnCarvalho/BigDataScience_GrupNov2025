# -------------------------------------------------
# ########### SEQUÊNICA DE FIBONACCI BÁSICA ###########
primeiro = 0
segundo = 1
proximo = primeiro + segundo

print(primeiro)
print(segundo)

while proximo <= 100:
    print(proximo)
    primeiro = segundo
    segundo = proximo
    proximo = primeiro + segundo
    # 0 1 1 2 3 5 8 13 21 34 55 89 esta sequencia é a sequencia de fibocacci


# -------------------------------------------------
# ########### SEQUÊNICA DE FIBONACCI ENXUTA
primeiro = 0
segundo = 1

while primeiro <= 100:
    print(primeiro)
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo