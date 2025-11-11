# EXEMPLO 1 - Perguntar e mostrar uma informação simples
# Enunciado: Peça ao usuário para digitar o nome e depois cumprimente-o.
nome = input("Qual é o seu nome? ")
print("Olá,", nome, "! Seja bem-vindo(a) ao curso de Python!")

# ATIVIDADE 1
# Enunciado: Peça ao usuário sua cor favorita e mostre uma mensagem com essa cor.
cor = input("Qual é a sua cor favorita? ")
print("Sua cor favorita é:", cor)

# -----------------------------------------------------------
# EXEMPLO 2 - Usando duas variáveis e exibindo na mesma frase
# Enunciado: Peça o nome da cidade e o estado onde o usuário mora, depois exiba ambos.
cidade = input("Em qual cidade você mora? ")
estado = input("E em qual estado fica essa cidade? ")
print("Você mora na cidade de", cidade, "que fica no estado de", estado + ".")

# ATIVIDADE 2
# Enunciado: Peça o nome do animal favorito do usuário e sua raça, depois exiba os dois.
animal = input("Qual é o seu animal favorito? ")
raca = input("Qual é a raça desse animal? ")
print("Você gosta de", animal, "da raça", raca + ".")
# -----------------------------------------------------------

# EXEMPLO 3 - Criando variáveis numéricas e exibindo resultados
# Enunciado: Peça a idade do usuário e calcule o ano de nascimento.
idade = int(input("Quantos anos você tem? "))
ano_atual = 2025
ano_nascimento = ano_atual - idade
print("Você nasceu em", ano_nascimento, ".")

# ATIVIDADE 3
# Enunciado: Peça o ano de nascimento do usuário e calcule a idade que ele terá em 2025.
ano_atual = 2025
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
idade = ano_atual - ano_nascimento
print("Você tem", idade, "anos.")
# -----------------------------------------------------------

# EXEMPLO 4 - Cálculo simples entre duas variáveis
# Enunciado: Solicite dois números e mostre a soma deles.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos dois números é:", soma)

# ATIVIDADE 4 - Mesmo raciocínio, outro contexto (com multiplicação)
# Enunciado: Calcule o valor total a pagar pela compra de ingressos de cinema.
preco_unitario = float(input("Digite o preço de um ingresso de cinema: "))
quantidade = int(input("Quantos ingressos você comprou? "))
total = preco_unitario * quantidade
print("O valor total a pagar é de R$", total)

# ATIVIDADE 4 (VARIAÇÃO) - Mesmo raciocínio, outro contexto (divisão)
# Enunciado: Descubra quantos ingressos de cinema podem ser comprados com o valor disponível.
preco_unitario = float(input("Digite o preço de um ingresso de cinema: "))
valor_disponivel = float(input("Digite quanto dinheiro você tem para a compra: "))
quantidade = int(valor_disponivel // preco_unitario)
print("Com R$", valor_disponivel, "você pode comprar", quantidade, "ingresso(s).")
# ------------------------------------------------------------

# EXEMPLO 5 - Cálculos com mais de uma operação
# Enunciado: Calcule o valor total de uma compra com desconto de 10%.
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco * quantidade
desconto = total * 0.1
valor_final = total - desconto
print("O valor total da compra com desconto é:", valor_final)

# ATIVIDADE 5 - Aumento de salário
# Enunciado: Calcule o novo salário de um funcionário com aumento de 15%.
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)

# ATIVIDADE 5 - Consumo do Carro
# Enunciado: Calcule o consumo médio de combustível de um carro em km por litro.
km = float(input("Digite a distância percorrida (em km): "))
litros = float(input("Digite a quantidade de combustível gasto (em litros): "))
consumo = km / litros
print("O consumo médio do veículo foi de", consumo, "km por litro.")
# ------------------------------------------------------------
