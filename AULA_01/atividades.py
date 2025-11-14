# ATIVIDADE AVALIATIVA 1
# Pensando em um boletim escolar.
# O programa deve calcular a média de duas notas informadas pelo usuário.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print("A média do aluno é:", media)

# -------------------------------------------------------------------
# ATIVIDADE AVALIATIVA 2
# O usuário digitará 2 números e o programa exibirá o resultado
# das quatro operações básicas e o módulo.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
modulo = num1 % num2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Módulo:", modulo)
