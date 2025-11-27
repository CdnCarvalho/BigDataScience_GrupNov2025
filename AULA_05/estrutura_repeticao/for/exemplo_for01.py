# COMANDO FOR 
# O comando for é uma estrutura de repetição em Python.
# Ele é usado para executar um bloco de código várias vezes, de forma controlada.
# Normalmente, usamos o for junto com a função range(), que gera uma sequência de números.

# ************** EXPLICANDO A ESTRUTURA FOR ABAIXO: ***********************
# for i in range(3):

####  for: palavra-chave que inicia a repetição
####  i: variável de controle que assume valores a cada repetição
####  in: conecta o for com a sequência a ser repetida
####  range(3): função que gera a sequência (neste caso: 0, 1, 2)
####  : (dois-pontos): obrigatório ao final da linha que inicia o for
####  OBS: O bloco que será repetido vem logo abaixo, com INDENTAÇÃO!


# ************** INDENTAÇÃO (Recuo Obrigatório no Python) *****************
# Python **não usa chaves {}, nem begin/end como em outras linguagens p/
# informar o que está dentro ou fora da estrutura For.
# O que define o bloco de código a ser repetido é o recuo (IDENTAÇÃO).

# EXEMPLO:
# for i in range(3):
#     print(i)  # <- esta linha está dentro do for, pois está indentada
# print("fim")  # <- esta linha está fora do for


# ---------------------------------------------------------------------------------------
# EXEMPLOS PRÁTICOS - ESTRUTURA DE REPETIÇÃO FOR
# ----------------------------------------------------------------------------------------
# Exemplo 1 – Repetição simples com mensagem
for n in range(5):  # repete o bloco abaixo 5 vezes (valores de 0 até 4)
    print("olá mundo")  # exibe a mensagem "olá mundo" a cada repetição

# ----------------------------------------------------------------------------------------
# Exemplo 2 – Contando de 0 até 4
for n in range(5):  # n vai assumir os valores 0, 1, 2, 3 e 4
    print(n)  # mostra o valor atual de n


# ----------------------------------------------------------------------------------------
# Exemplo 3 – Contando de 5 até 19
for i in range(5, 20):  # i começa em 5 e vai até 19 (o 20 não é incluído)
    print(i)  # mostra o valor atual de i


# ----------------------------------------------------------------------------------------
# Exemplo 4 – Contagem pulando de 5 em 5
for j in range(5, 50, 5):  # começa em 5, vai até 49, pulando de 5 em 5
    print(j)  # mostra os valores: 5, 10, 15, ..., até 45


# ----------------------------------------------------------------------------------------
# Exemplo 5 – Contagem com valores definidos pelo usuário
inicio = int(input("Informe o inicio da contagem: "))  # recebe o valor inicial da contagem
fim = int(input("informe o final da contagem: "))     # recebe o valor final da contagem

for u in range(inicio, fim):  # usa os valores fornecidos para definir o início e fim
    print(u)  # mostra cada número da contagem personalizada


# ----------------------------------------------------------------------------------------
# Exemplo 6 – Repetindo uma ação para 3 pessoas
for n in range(3):  # repete o bloco 3 vezes (para 3 pessoas)
    print(f'\npessoa {n + 1}')  # mostra qual pessoa está sendo tratada (1, 2 ou 3)
    nome = input("Informe o nome: ")  # recebe o nome da pessoa
    print(f'O nome da pessoa é: {nome}.')  # mostra o nome digitado


# ----------------------------------------------------------------------------------------
# Exemplo 7 – Somando valores informados pelo usuário
soma = 0.  # inicializa a variável soma com valor 0.0

for num in range(5):  # repete 5 vezes
    numero = float(input("Digite um número: "))  # recebe um número real (float) do usuário
    soma += numero  # adiciona o número digitado à variável soma (acumulador)

print(f'O total é de {soma}')  # mostra o valor total somado
