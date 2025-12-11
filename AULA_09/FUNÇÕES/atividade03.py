# Funções para cada operação
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


# Programa principal
print("=== Calculadora de 4 Operações ===")
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Chamando as funções
resultado_soma = somar(x, y)
resultado_sub = subtrair(x, y)
resultado_mult = multiplicar(x, y)
resultado_div = dividir(x, y)

# Exibindo resultados
print("\n--- RESULTADOS ---")
print(f"A soma entre {x} e {y} resulta em:  {resultado_soma}")
print(f"A subtração entre {x} e {y} resulta em:  {resultado_sub}")
print(f"A multiplicação entre {x} e {y} resulta em:  {resultado_mult}")
print(f"A divisão entre {x} e {y} resulta em:  {resultado_div}")
