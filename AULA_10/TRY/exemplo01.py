# ----------------------------------------------------------- Except - Exemplo 01 (Explicação 1: Letras ao invés de números)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios
    print(f"\nMédia produzida por funcionário: {media_por_funcionario:.2f}")
except ValueError:
    print(f"\nErro: informe apenas números válidos.")




# ----------------------------------------------------------- Except Else - Exemplo 02  Letras ao invés de números)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios

except ValueError:
    print("\nErro: informe apenas números válidos.")
else:
    print(f"\nMédia de produção por funcionário: {media_por_funcionario:.2f}")



# ----------------------------------------------------------- Multiplas Exceções - Except, Else e Finally - Exemplo 03 ( Letras, divisão por zero)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios

except ValueError:
    print("\nErro: informe apenas números válidos.")
except ZeroDivisionError:
    print("\nErro: não há funcionários ativos para calcular a média.")
else:
    print(f"\nMédia de produção por funcionário: {media_por_funcionario:.2f}")
finally:
    print("\nRelatório finalizado.")



# ----------------------------------------------------------- Multiplas exceções em parênteses - Exemplo 04 (Letras, divisão por zero, KeyboardInterrupt)
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios

except (ValueError, TypeError):
    print("\nErro: informe apenas números.")
except ZeroDivisionError:
    print("\nErro: não há funcionários ativos para calcular a média.")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"\nErro inesperado: {e}")
else:
    print(f"\nMédia de produção por funcionário: {media_por_funcionario:.2f}")
finally:
    print("\nRelatório finalizado.")



# ----------------------------------------------------------- except Exception - Exemplo 05 (Capturando o erro genérico {e})
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input("Informe o total produzido no mês: "))
    funcionarios = int(input("Informe a quantidade de funcionários ativos: "))

    media_por_funcionario = total_produzido / funcionarios

except Exception as e:
    print(f"\nErro inesperado: {e}")
else:
    print(f"\nMédia de produção por funcionário: {media_por_funcionario:.2f}")
finally:
    print("\nRelatório finalizado.")