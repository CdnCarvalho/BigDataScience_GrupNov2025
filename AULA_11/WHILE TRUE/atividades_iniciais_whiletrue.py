# Gabarito – Estrutura while True simulando do while
# Exercícios para introdução ao uso de while True como alternativa ao do while (que não existe em Python)

# ------------------------------------------------------------------
# Exercício 1 – Contagem simples
# Enunciado: Mostre os números de 1 a 10.
# Executa pelo menos uma vez e usa break para parar a repetição
# quando i ultrapassa 10.
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break


# ------------------------------------------------------------------
# Exercício 2 – Mensagem repetida
# Enunciado: Exiba a mensagem "Estudando Python!" 5 vezes.
# A estrutura garante que o bloco será executado ao menos uma vez e para
# após 5 repetições.
contador = 0
while True:
    print("Estudando Python!")
    contador += 1
    if contador == 5:
        break


# ------------------------------------------------------------------
# Exercício 3 – Tabuada personalizada
# Enunciado: Peça um número e mostre sua tabuada até 10.
# Mesmo padrão: tabuada é exibida com while True e controle do final com break.
numero = int(input("Digite um número: "))

i = 1
while True:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
    if i > 10:
        break


# ------------------------------------------------------------------
# Exercício 4 – Coleta de dados
# Enunciado: Peça o nome de 3 pessoas e mostre a lista.
# Aqui o loop roda 3 vezes, controlado com contador e break ao final.
i = 1
while True:
    nome = input(f"Digite o nome da pessoa {i}: ")
    print(f"Nome {i}: {nome}")
    i += 1
    if i > 3:
        break


# ------------------------------------------------------------------
# Exercício 5 – Soma de valores
# Enunciado: Some 5 números digitados pelo usuário.
# Soma 5 números, repetindo a entrada até atingir o número desejado de interações.
soma = 0
contador = 0

while True:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1
    if contador == 5:
        break

print(f"A soma dos números é {soma}")