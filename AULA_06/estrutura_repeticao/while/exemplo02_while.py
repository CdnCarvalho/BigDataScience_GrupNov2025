# Exemplo 02 - Estrutura de repetição com While "Enquanto"
contador = 0
while contador < 5:
    num = int(input("\nDigite um número: "))
    dobro = num * 2
    triplo = num * 3
    quadruplo = num * 4
    
    print(f'O número é {num}, o dobro é {dobro}, o triplo é {triplo} e o quádruplo é {quadruplo}')
    contador = contador + 1