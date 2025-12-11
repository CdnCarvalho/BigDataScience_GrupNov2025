def verificar_par(a):
    if a % 2 == 0:
        print(f'{a} é par')
    else:
        print(f'{a} é impar')


n1 = int(input('Informe um número: '))
verificar_par(n1)
# ---------------------- // ------------------------------



# Dobro, triplo e Quadrado
def calcular(x):
    dobro = x * 2
    triplo = x * 3
    quadrado = x * x

    return dobro, triplo, quadrado

numero = int(input('informe o número: '))
d, t, q = calcular(numero)
print(f'O dobro é {d}, o triplo é {t} e o quadrado é {q}')