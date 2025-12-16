def somar_pares(a, b):
    # se algum número for ímpar, força um erro
    if a % 2 != 0 or b % 2 != 0:
        # int("erro")  # gera ValueError automaticamente
        print('Erro!!!: Não deve informar números ímpares!')
        return 'Não calculado'
    
    return a + b


print("=== Soma de números Pares ===")

# Leitura de 3 pares de números
for i in range(3):
    print(f"\nPar {i+1}")

    try:
        n1 = int(input("Digite o primeiro número par: "))
        n2 = int(input("Digite o segundo número par: "))

        resultado = somar_pares(n1, n2)
        print(f"Soma do {i+1}º par : {resultado}")

    except ValueError:
        print("Erro: apenas números PARES são permitidos.")