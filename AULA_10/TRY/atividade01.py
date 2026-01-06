# Função para somar dois números
def somar(a, b):
    return a + b


print("=== Soma os Números ===")

# Loop para 3 repetições
for i in range(3):
    print(f"\n--- Operação {i+1} ---")

    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

    except ValueError:
        print("Erro: informe apenas números.")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    else:
        # Executa somente se NÃO ocorrer erro
        resultado = somar(n1, n2)
        print(f"Soma dos valores: {resultado}")

    finally:
        # Executa sempre, com erro ou sem erro
        print("Operação finalizada.")

print("\nPrograma encerrado.")



# -------------------------------------------------- Soma apenas,
#  se ambos os números forem pares
def somar_pares(a, b):
    if a % 2 != 0 or b % 2 != 0:
        return "Não calculado: números ímpares informados"
    
    return a + b


print("=== Soma de números pares ===")

for i in range(3):
    print(f"\nPar {i+1}")

    try:
        n1 = int(input("Digite o primeiro número par: "))
        n2 = int(input("Digite o segundo número par: "))

    except ValueError:
        print("Erro: informe apenas números inteiros.")
    except KeyboardInterrupt:
        print("Erro: operação interrompida pelo usuário.")

    else:
        resultado = somar_pares(n1, n2)
        print(f"Resultado do {i+1}º par: {resultado}")

    finally:
        print("Operação encerrada.")
