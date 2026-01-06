import random

def gerar_numeros(ini, fin, qtd):
    lst_num = [random.randint(ini, fin) for i in range(qtd)]
    print("Números gerados:", lst_num)
    return lst_num


# função para somar
def somar(n1, n2):
    return n1 + n2


# função para subtrair
def subtrair(n1, n2):
    return n1 - n2


# função para multiplicar
def multiplicar(n1, n2):
    return n1 * n2


# função para dividir
def dividir(n1, n2):
    return n1 / n2


# --------- PROGRAMA PRINCIPAL ---------

lista = gerar_numeros(1, 10, 2)

n1 = lista[0]
n2 = lista[1]

# Chamadas das funções
resultado_soma = somar(n1, n2)
resultado_sub = subtrair(n1, n2)
resultado_mult = multiplicar(n1, n2)
resultado_div = dividir(n1, n2)

# Exibição final
print(f"A soma entre {n1} e {n2} é: {resultado_soma}")
print(f"A subtração entre {n1} e {n2} é: {resultado_sub}")
print(f"A multiplicação entre {n1} e {n2} é: {resultado_mult}")
print(f"A divisão entre {n1} e {n2} é: {resultado_div}")
