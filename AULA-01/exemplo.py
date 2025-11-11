# EXEMPLO 1 - Perguntar e mostrar uma informação simples
nome = input("Qual é o seu nome? ")
print("Olá,", nome, "! Seja bem-vindo(a) ao curso de Python!")

# ATIVIDADE 1
cor = input("Qual é a sua cor favorita? ")
print("Sua cor favorita é:", cor)

# -----------------------------------------------------------
# EXEMPLO 2 - Usando duas variáveis e exibindo na mesma frase
cidade = input("Em qual cidade você mora? ")
estado = input("E em qual estado fica essa cidade? ")
print("Você mora na cidade de", cidade, "que fica no estado de", estado + ".")

# ATIVIDADE 2
animal = input("Qual é o seu animal favorito? ")
raca = input("Qual é a raça desse animal? ")
print("Você gosta de", animal, "da raça", raca + ".")
# -----------------------------------------------------------


# EXEMPLO 3 - Criando variáveis numéricas e exibindo resultados
idade = int(input("Quantos anos você tem? "))
ano_atual = 2025
ano_nascimento = ano_atual - idade
print("Você nasceu em", ano_nascimento, ".")

# ATIVIDADE 3
ano_atual = 2025
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
idade = ano_atual - ano_nascimento
print("Você tem", idade, "anos.")
# -----------------------------------------------------------


# EXEMPLO 4 - Cálculo simples entre duas variáveis
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos dois números é:", soma)

# ATIVIDADE 4 - Mesmo raciocínio, outro contexto (com multiplicação)
preco_unitario = float(input("Digite o preço de um ingresso de cinema: "))
quantidade = int(input("Quantos ingressos você comprou? "))
total = preco_unitario * quantidade
print("O valor total a pagar é de R$", total)
# ------------------------------------------------------------

# EXEMPLO 5 - Cálculos com mais de uma operação
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco * quantidade
desconto = total * 0.1
valor_final = total - desconto
print("O valor total da compra com desconto é:", valor_final)

# ATIVIDADE 5 - Aumento de salário
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)

# ATIVIDADE 5 - Consumo do Carro
km = float(input("Digite a distância percorrida (em km): "))
litros = float(input("Digite a quantidade de combustível gasto (em litros): "))
consumo = km / litros
print("O consumo médio do veículo foi de", consumo, "km por litro.")

####################################################################
# ATIVIDADES AVALIATIVAS



