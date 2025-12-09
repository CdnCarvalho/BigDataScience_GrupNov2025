# Funções
# Funções são blocos de códigos, que só serão executados,
# se forem chamados.
# Tradicionalmente as funções têm nome. Exceto as lâmbidas.
# Uma função em Python precisa ser declarada.
# Para se declarar uma função, precisa iniciar
# a declaração com a palavra reservada "def":
# Exemplo para uma função de nome saudacao: 
# def saudacao():
#   print('Olá mundo')

# ------------------------------------------------
# SINTAXE: Função para saudação
def saudacao():
    print('Olá, boa noite!')

saudacao()


# --------------------------------------------------
# PARÂMETRO: Nome na saudação
def saudacao2(nome):
    print(f'Olá, {nome}!')

saudacao2('João')


# ---------------------------------------------------
# PARÂMTROS: Função para Somar
def soma(x, y):
    # global s  # Caso queira manipular a variável S do lado de fora
    s = x + y
    print(s)

n1 = int(input('Informe o número: '))
n2 = int(input('Informe o número: '))

soma(n1, n2)
print(f'Imprime o valor de S depois da chamada da soma {s}')  # Para introduzir o return


# --------------------------------------------------------
# PARÂMETROS: 3 pares de números informado pelo usuário
def somar_numeros(a, b):
    s = a + b
    print(s)


for i in range(3):
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))
    somar_numeros(n1, n2)
