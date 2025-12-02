
# --------------------------------------------------------------------------------
# ATIVIDADE 03 - Caixa Registradora
total = 0

valor = input('Informe o valor do produto (ou digite "fim" para encerrar): ')

while valor != "fim":
    if valor.replace('.', '').isdigit():   # verifica se é número válido
        valor = float(valor)
        print(valor)
        total += valor
    else:
        print("Entrada inválida! Digite um número ou 'fim'.")
    
    valor = input('Informe o valor do próximo produto (ou digite "fim"): ')

print("Total da compra: R$", total)


# -------------------------------------------------------------------------------
# ATIVIDADE 04 - Controle de Horas Trabalhadas
print("=== Controle de Horas Trabalhadas ===")
print("Digite as horas de cada dia ou 'fim' para encerrar.\n")

total_horas = 0
dias = 0

entrada = input("Horas trabalhadas hoje: ")

while entrada.lower() != "fim":
    # validação: número com no máximo um ponto
    if entrada.replace('.', '', 1).isdigit():
        horas = float(entrada)
        total_horas += horas
        dias += 1
    else:
        print("Entrada inválida. Digite apenas números ou 'fim'.")
    
    entrada = input("Horas trabalhadas hoje: ")

# evita divisão por zero caso o aluno finalize sem digitar horas
if dias > 0:
    media = total_horas / dias
    print("\n=== RELATÓRIO FINAL ===")
    print(f"Total de horas: {total_horas}")
    print(f"Média por dia: {media:.2f}")
else:
    print("Nenhuma hora foi registrada.")
