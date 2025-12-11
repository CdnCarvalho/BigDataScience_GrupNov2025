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


# ------------------------------------------------------------ PROGRAMA PRINCIPAL
lista = gerar_numeros(1, 10, 2)
print("\nValores escolhidos para as operações:")
print(f"Primeiro número: {lista[0]}")
print(f"Segundo número : {lista[1]}")

print()
print(40*'=')
print('Escolha uma operação: ')
print(40*'=')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')


# match case
opcao = int(input('\nDigite a opção desejada: '))

print(40*'=')
print("\nResultado da operação:")
print(40*'=')

match opcao:
    case 1:
        print(f"Somando {lista[0]} + {lista[1]} = {somar(lista[0], lista[1])}")
    case 2:
        print(f"Subtraindo {lista[0]} - {lista[1]} = {subtrair(lista[0], lista[1])}")
    case 3:
        print(f"Multiplicando {lista[0]} * {lista[1]} = {multiplicar(lista[0], lista[1])}")
    case 4:
        print(f"Dividindo {lista[0]} / {lista[1]} = {dividir(lista[0], lista[1])}")
    case _:
        print("Opção inválida. Tente novamente.")

print('Fim do programa.')
