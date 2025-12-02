# Exemplo 02 - Estrutura de repetição com While "Enquanto"
contador = 0

while contador < 5:
    num = int(input("\nDigite um número: "))
    dobro = num * 2
    triplo = num * 3
    quadruplo = num * 4

    print(f'O número é {num}, o dobro é {dobro}, o triplo é {triplo} e o quádruplo é {quadruplo}')
    contador = contador + 1



# ----------------------------------------------------------------------
# #########  Exemplo 03 - While Vendas de Imóveis
print("=== Controle de Vendas de Imóveis ===")

soma = 0
quantidade = 0
continuar = "N"

maior = 0
menor = 0

while continuar != "S":
    valor = float(input("Informe o valor do imóvel vendido: R$ "))
    
    soma += valor
    quantidade += 1

    # Define o menor e o maior valor na primeira entrada
    if quantidade == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    continuar = input("Deseja encerrar o registro? (S/N): ")[0].upper()

media = soma / quantidade

print("\n=== RESUMO DO MÊS ===")
print("Quantidade de imóveis vendidos:", quantidade)
print("Soma total das vendas: R$", soma)
print("Valor médio dos imóveis: R$", media)
print("Imóvel mais caro vendido: R$", maior)
print("Imóvel mais barato vendido: R$", menor)



# ----------------------------------------------------------------------
# EXEMPLO 04 - WHILE (VERIFICAÇÃO DE ENTRADA)
print("=== Cadastro simples de valores ===")
print("Digite um valor numérico ou 'sair' para encerrar.\n")

entrada = input("Informe um valor: ")
total = 0

while entrada.lower() != "sair":

    # validação: permite apenas números com no máximo 1 ponto
    if entrada.replace('.', '', 1).isdigit():
        numero = float(entrada)
        print(f"Você digitou o número: {numero}")
        total += numero
    else:
        print("Entrada inválida. Digite apenas números ou 'sair'.")

    entrada = input("Informe um valor: ")

print("Programa encerrado.")
print(f"Total de valores digitados: {total}")
