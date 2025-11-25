# Recebe o código de acesso digitado pelo usuário
codigo = int(input("Informe o código de acesso: "))

# Verifica a área correspondente com base no código usando match/case
match codigo:
    case 1:
        print("Acesso à Academia")
    case 2:
        print("Acesso à Piscina")
    case 3:
        print("Acesso à Cobertura VIP")
    case 4 | 5:  # Usando o Pipe no sentido de 6 ou 7
        print("Acesso ao Estacionamento")
    case 6 | 7 | 8:  # Pipe como operador ou 'Or'
        print("Acesso às Áreas Comuns")
    case 11:
        print("Acesso Técnico")
    case _:
        print("Acesso negado. Código inválido.")



# Recebe o código de acesso digitado pelo usuário
codigo = int(input("Informe o código de acesso: "))

# Verifica a área correspondente com base no código usando match/case
match codigo:
    case 1:
        print("Acesso à Academia")
    case 2:
        print("Acesso à Piscina")
    case 3:
        print("Acesso à Cobertura VIP")
    case num if num == 4 or num == 5:  # Sem o uso do Pipe. Usamos o If com verificações lógicas. Observe bem a Sintaxe.
        print("Acesso ao Estacionamento")
    case num if num == 6 or num == 7 or num == 8:
        print("Acesso às Áreas Comuns")
    case 9:
        print("Acesso Técnico")
    case _:
        print("Acesso negado. Código inválido.")



# # Recebe o código de acesso digitado pelo usuário
# codigo = int(input("Informe o código de acesso: "))

# # Verifica a área correspondente com base no código usando match/case
# match codigo:
#     case 1:
#         print("Acesso à Academia")
#     case 2:
#         print("Acesso à Piscina")
#     case 3:
#         print("Acesso à Cobertura VIP")
#     case num if num == 4 or num == 5:
#         print("Acesso ao Estacionamento")
#     case num if 6 <= num <= 8:  # Maneira insentivada pela comunidade Python para realizar verificações em intervalos maiores. Neste caso, estamos verificando, se variável num está no intervalo entre 7 e 9.
#         print("Acesso às Áreas Comuns")
#     case 9:
#         print("Acesso Técnico")
#     case _:
#         print("Acesso negado. Código inválido.")

# --------------------------------------------------------
# Exemplo 2
# Classificando idade
idade = int(input("Digite a idade: "))

match idade:
    case i if i < 12:
        print("Criança")
    case i if 12 <= i < 18:
        print("Adolescente")
    case i if i >= 18:
        print("Adulto")
    case _:
        print("Idade inválida.")

# Atividade 2
valor = float(input("Digite um valor de venda: "))

match valor:
    case v if v < 100:
        print("Venda pequena")
    case v if 100 <= v < 500:
        print("Venda média")
    case v if v >= 500:
        print("Venda grande")
# --------------------------------------------------------

# --------------------------------------------------------
# Exemplo 3
# Menu de opções
opcao = input("""
MENU
1 - Cadastrar cliente
2 - Ver lista de clientes
3 - Gerar relatório
4 - Sair
Escolha: """)

match opcao:
    case "1":
        print("Cadastro iniciado...")
    case "2":
        print("Listando clientes...")
    case "3":
        print("Gerando relatório...")
    case "4":
        print("Saindo do sistema...")
    case _:
        print("Opção inválida.")

# Atividade 3
# Menu de opções
opcao = input("""
MENU
1 - Criar um usuário
2 - Editar usuário
3 - Visualizar usuário
4 - Deletar usuário
Escolha: """)

match opcao:
    case "1":
        print(f"Você digitou {opcao}")
        # escolha_valida = True
    case "2":
        print(f"Você digitou {opcao}")
        # escolha_valida = True
    case "3":
        print(f"Você digitou {opcao}")
        # escolha_valida = True
    case "4":
        print(f"Você digitou {opcao}")
        # escolha_valida = True
    case _:
        print("Opção inválida.")
        # escolha_valida = False

# Mostrar qual número foi escolhido (somente se for válido)
# if escolha_valida:
#     print(f"\nVocê escolheu a opção número: {opcao}")



# Atividade 3.1
# Entrada do valor da compra
valor = float(input("Informe o valor da compra: R$ "))

# Menu de formas de pagamento
opcao = input("""
FORMAS DE PAGAMENTO
1 - Pix  (12% de desconto)
2 - Débito  (8% de desconto)
3 - Crédito  (7% de juros)
4 - Dinheiro  (15% de desconto)
Escolha a opção: """)

match opcao:
    case "1":
        desconto = valor * 0.12
        valor_final = valor - desconto
        print("\n--- Pagamento via PIX ---")
        print(f"Preço normal: R$ {valor:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Preço final: R$ {valor_final:.2f}")

    case "2":
        desconto = valor * 0.08
        valor_final = valor - desconto
        print("\n--- Pagamento no Débito ---")
        print(f"Preço normal: R$ {valor:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Preço final: R$ {valor_final:.2f}")

    case "3":
        juros = valor * 0.07
        valor_final = valor + juros
        print("\n--- Pagamento no Crédito ---")
        print(f"Preço normal: R$ {valor:.2f}")
        print(f"Juros: R$ {juros:.2f}")
        print(f"Preço final: R$ {valor_final:.2f}")

    case "4":
        desconto = valor * 0.15
        valor_final = valor - desconto
        print("\n--- Pagamento em Dinheiro ---")
        print(f"Preço normal: R$ {valor:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Preço final: R$ {valor_final:.2f}")

    case _:
        print("\nOpção inválida.")
# ---------------------------------------------------------------------
