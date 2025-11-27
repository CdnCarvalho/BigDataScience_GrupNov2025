# Gabarito – Introdução ao while
# Exercícios iniciais para praticar a estrutura de repetição while em Python.

# ------------------------------------------------------------------
# Exercício 1 – Contagem simples
# Enunciado: Mostre os números de 1 a 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# Começamos com i = 1. Enquanto i for menor ou igual a 10, imprimimos i e somamos 1.
# O laço pára quando i ultrapassa 10.

# ------------------------------------------------------------------
# Exercício 2 – Mensagem repetida
# Enunciado: Exiba a mensagem "Estudando Python!" 5 vezes.
contador = 0
while contador < 5:
    print("Estudando Python!")
    contador += 1

# O while repete a mensagem, enquanto contador for menor que 5.
# Usamos += 1, para ir somando até atingir 5 repetições.

# ------------------------------------------------------------------
# Exercício 3 – Tabuada personalizada
# Enunciado: Peça um número e mostre sua tabuada até 10.
numero = int(input("Digite um número: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

# A lógica da tabuada é a mesma, apenas a estrutura de repetição muda.
# O número digitado é multiplicado por i, que vai de 1 até 10.

# ------------------------------------------------------------------
# Exercício 4 – Coleta de dados
# Enunciado: Peça o nome de 3 pessoas e mostre a lista.
i = 1
while i <= 3:
    nome = input(f"Digite o nome da pessoa {i}: ")
    print(f"Nome {i}: {nome}")
    i += 1

# Aqui controlamos a quantidade de repetições com i, começando de 1 até 3.
# O nome da pessoa é exibido após cada entrada.

# ------------------------------------------------------------------
# Exercício 5 – Soma de valores
# Enunciado: Some 5 números digitados pelo usuário.
soma = 0
contador = 0

while contador < 5:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1

print(f"A soma dos números é {soma}")
# A soma é acumulada a cada entrada, até atingir 5 números.
