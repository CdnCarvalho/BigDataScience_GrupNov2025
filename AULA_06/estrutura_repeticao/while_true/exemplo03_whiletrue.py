# -----------------------------------------------------------------
# Exemplo 03 - Estrutura de repetição com While True "Loop Infinito"
c = 0
while True:
    print(f"\n{c+1}º While True - Laço infinito")
    num = int(input("Digite um número: "))
    dobro = num * 2
    triplo = num * 3
    quadruplo = num * 4

    print(f'O número é {num}, o dobro é {dobro}, o triplo é {triplo} e o quádruplo é {quadruplo}')
    c += 1

    if c == 5:
        break


# -------------------------------------------------------------------
# Exemplo com while True
# Esse código executa ao menos uma vez
# E continua até a condição ser satisfeita, como faria um do while
while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if 0 <= nota <= 10:
        break  # Sai do loop se a nota for válida
    else:
        print("Nota inválida. Tente novamente.")

print(f"Nota registrada: {nota}")


# -------------------------------------------------------------------
# SITUAÇÃO ANÁLISE DE IDADE: 
# Você está simulando a coleta de dados para análise de perfil de clientes.
# O programa pede a idade de uma pessoa e pergunta, se deseja registrar mais dados.
# Ao final, exibe quantas pessoas foram registradas e a média das idades dos clientes.
total_idades = 0
quantidade_pessoas = 0

while True:
    idade = int(input("Informe a idade do cliente: "))
    total_idades += idade
    quantidade_pessoas += 1

    continuar = input("Deseja registrar outro cliente? (s/n): ").lower()
    if continuar == 'n':
        break

media = total_idades / quantidade_pessoas
print(f"\nTotal de clientes: {quantidade_pessoas}")
print(f"Média de idade: {media:.2f}")
