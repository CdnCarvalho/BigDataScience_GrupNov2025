# Gabarito – Introdução ao for
# Conjunto de exercícios iniciais para praticar a estrutura de repetição for em Python.

# ------------------------------------------------------------------
# Exercício 1 – Contagem simples
# Enunciado: Mostre os números de 1 a 10.

for i in range(1, 11):
    print(i)

# O range(1, 11) gera os números de 1 até 10 (o último não é incluído).
# Cada número é mostrado um por linha no terminal.

# ------------------------------------------------------------------
# Exercício 2 – Mensagem repetida
# Enunciado: Exiba a mensagem "Estudando Python!" 5 vezes.

for _ in range(5):
    print("Estudando Python!")

# Usamos _ quando não precisamos do número da repetição.
# O range(5) executa a repetição 5 vezes (de 0 a 4 internamente).

# ------------------------------------------------------------------
# Exercício 3 – Tabuada personalizada
# Enunciado: Peça um número e mostre sua tabuada até 10.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# O aluno aprende a combinar entrada (input) com repetição e cálculo.
# O range(1, 11) gera os valores de 1 a 10, multiplicando pelo número digitado.

# ------------------------------------------------------------------
# Exercício 4 – Coleta de dados
# Enunciado: Peça o nome de 3 pessoas e mostre a lista.
for i in range(3):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    print(f"Nome {i + 1}: {nome}")

# i + 1 serve para exibir 1, 2, 3 no lugar de 0, 1, 2.

# ------------------------------------------------------------------
# Exercício 5 – Soma de valores
# Enunciado: Some 5 números digitados pelo usuário.

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

print(f"A soma dos números é {soma}")
# A soma é exibida ao final da execução.
