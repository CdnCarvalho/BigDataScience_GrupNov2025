# EXEMPLO 01
# Sistema simples para aplicar desconto em compras acima de R$ 250,00

# Entrada do valor da compra
valor = float(input("Informe o valor da compra: R$ "))

# Verificação da condição para aplicar o desconto
if valor > 250:
    desconto = valor * 0.16  # Calcula 16% de desconto
    valor_final = valor - desconto
    print(f"Desconto de 16% aplicado. Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor a pagar: R$ {valor:.2f}")


# 
# EXEMPLO 02
# Sistema para verificar se um pedido pode ser enviado

# Entrada de dados
estoque = int(input("Informe a quantidade em estoque: "))
solicitado = int(input("Informe a quantidade solicitada no pedido: "))
peso = float(input("Informe o peso total do pedido (em kg): "))

# Verificação das duas condições ao mesmo tempo (AND)
if estoque >= solicitado and peso <= 50:
    print("Pedido liberado para envio.")
else:
    print("Pedido não pode ser enviado. Verifique a quantidade em estoque e/ou o peso do pedido.")


#
# EXEMPLO 03
# Sistema para verificar se um cooperado/a tem acesso ao benefício

# Entrada de dados
tempo_filiacao = int(input("Informe o tempo de filiação (em anos): "))
valor_movimentado = float(input("Informe o valor movimentado nos últimos 6 meses (em R$): "))

# Verificação de pelo menos uma condição verdadeira (OR)
if tempo_filiacao > 3 or valor_movimentado > 5000:
    print("Você tem direito ao benefício especial da cooperativa.")
else:
    print("Você ainda não atende aos critérios para o benefício.")
