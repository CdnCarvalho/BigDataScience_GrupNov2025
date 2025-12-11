# Funções

# -------------------------------------------------------- Função Simples p/ somar dois números
# PARÂMTROS: Função para Somar
def soma(x, y):
    # global s  # Caso queira manipular a variável S do lado de fora
    s = x + y
    print(s)
    return s  # Para retornar o valor de S para o programa principal


n1 = int(input('Informe o número: '))
n2 = int(input('Informe o número: '))

soma(n1, n2)
print(f'Imprime o valor de S depois da chamada da soma {s}')  # Para introduzir o return



# --------------------------------------------------------# PARÂMTROS: Função para identificar o maior número
def maior_numero(a, b):
    if a > b:
        print(f"O maior número é: {a}")
        return a
    elif b > a:
        print(f"O maior número é: {b}")
        return b
    else:
        print("Os dois números são iguais.")


# Programa principal
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

maior = maior_numero(n1, n2)


# -------------------------------------------------------- # PARÂMTROS: 3 pares de números fixos
# 3 pares de números informado pelo usuário
def somar_numeros(a, b):
    s = a + b
    print(s)
    return s


for i in range(3):
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))
    tot = somar_numeros(n1, n2)
    print(f'O total da soma dos dois números é: {tot}')