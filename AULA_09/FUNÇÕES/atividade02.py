# Criar um programa que leia a altura e o peso de N pessoas e mostre seu IMC com a respectiva classificação.
# O cálculo do IMC deverá ser realizado através de uma função que receberá os valores de entrada necessários para o cálculo.
# 
# Fórmula --> IMC = PESO / (ALTURA * ALTURA)

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc <= 16.9:
        classificacao = 'Muito abaixo do peso'
    elif imc <= 18.4:
        classificacao = 'Abaixo do peso'
    elif imc <= 24.9:
        classificacao = 'Peso Normal'
    elif imc <= 29.9:
        classificacao = 'Acima do Peso'
    elif imc <= 34.9:
        classificacao = 'Obesidade Grau 1'
    elif imc <= 40:
        classificacao = 'Obesidade Grau 2'
    else:
        classificacao = 'Obesidade Grau 3'

    print('\nRESULTADO:')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')
    print('-' * 30)
    

# principal
qtd = int(input('Quantidade de pessoas? '))

for i in range(qtd):
    print(30*'=')
    print(f'PESSOA {i+1}')
    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    # Aqui a função cuida de tudo:
    calcula_imc(peso, altura)


# ################################################
# Usando Match Case
def calcula_imc(p, a):
    # Cálculo do IMC
    imc = p / (a ** 2)

    # Classificação usando match/case
    match imc:
        case imc if imc < 17:
            classificacao = 'Muito abaixo do peso'
        case imc if imc < 18.5:
            classificacao = 'Abaixo do peso'
        case imc if imc < 25:
            classificacao = 'Peso normal'
        case imc if imc < 30:
            classificacao = 'Acima do peso'
        case imc if imc < 35:
            classificacao = 'Obesidade grau 1'
        case imc if imc < 40:
            classificacao = 'Obesidade grau 2'
        case _:
            classificacao = 'Obesidade grau 3'

    # Impressão (tudo acontece aqui)
    print(30*'=')
    print('RESULTADO:')
    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')


# Programa principal
qtd = int(input('Quantidade de pessoas? '))

for i in range(qtd):
    print(f'\nPESSOA {i+1}')
    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    # Agora só chamamos a função; ela faz tudo dentro dela
    calcula_imc(peso, altura)

