##############################################
# Cadastro de Candidatos - Processo Seletivo
##############################################
print(50 * "=")
print("Cadastro de Candidatos - Processo Seletivo")
print(50 * "=")

ANO_ATUAL = 2025

candidatos_cadastrados = 0

for i in range(10):
    print(f"--- Candidato {i + 1} ---")

    nome = input("Nome: ")
    ano_nasc_cand = int(input("Ano de nascimento (ex: 2002): "))
    idade_cand = ANO_ATUAL - ano_nasc_cand

    # Verifica se o candidato é menor de idade
    if idade_cand < 18:
        print(f"\n{nome} tem {idade_cand} anos. Menores de 18 anos não podem ser cadastrados.")
        print("Continuando com o próximo...\n")
        continue  # Pula para a próxima iteração

    # Se for maior de idade, continua com o cadastro
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    formacao = input("Formação acadêmica: ")
    experiencia = input("Experiência profissional: ")

    print("\nCadastro concluído!")
    print(f"Nome: {nome}")
    print(f"Nascimento: {ano_nasc_cand} (idade: {idade_cand} anos)")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")
    print(f"Formação: {formacao}")
    print(f"Experiência: {experiencia}\n")

    candidatos_cadastrados += 1

print(f"\nProcesso finalizado. Total cadastrado: {candidatos_cadastrados}")


##############################################
# Cadastro de Candidatos - Processo Seletivo (continue ou break)
##############################################
print(40 * "=")
print("Cadastro de Candidatos - Processos Seletivos")
print(40 * "=")

ANO_ATUAL = 2025

for i in range(10):
    print(f"\n--- Candidato {i + 1} ---")

    ano_nasc = int(input("Ano de nascimento (ex: 2006): "))
    idade = ANO_ATUAL - ano_nasc

    # Verificação da idade
    if idade < 18:
        print("Cadastro encerrado! Candidato menor de 18 anos encontrado.")
        continue  # Pula para a próxima iteração do loop

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    formacao = input("Formação acadêmica: ")
    experiencia = input("Experiência profissional: ")

    print("\nCadastro concluído!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")
    print(f"Formação: {formacao}")
    print(f"Experiência: {experiencia}")

print("\nFim do processo de cadastro.")



##############################################
# Cadastro de Candidatos - Processo Seletivo (Não sabemos o número de candidatos)
##############################################
print(40 * "=")
print("Cadastro de Candidatos - Processos Seletivos")
print(40 * "=")

ANO_ATUAL = 2025

cadastro = 0   # conta somente cadastros aceitos
contador = 0   # conta todas as tentativas
continuar = "S"

while continuar == "S":
    contador += 1  # toda tentativa conta

    print(f"\nTentativa nº {contador}")

    ano_nasc = int(input("Ano de nascimento: "))
    idade = ANO_ATUAL - ano_nasc

    # Verificação da idade: se menor, encerra TUDO
    if idade < 18:
        print("Cadastro encerrado! Candidato menor de 18 anos encontrado.")
        # continuar = "N"   # encerra o loop
        continue  # se menor, não conta como cadastro
    else:
        cadastro += 1  # só conta se realmente cadastrou

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        formacao = input("Formação acadêmica: ")
        experiencia = input("Experiência profissional: ")

        print("\nCadastro concluído!")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Telefone: {telefone}")
        print(f"E-mail: {email}")
        print(f"Formação: {formacao}")
        print(f"Experiência: {experiencia}")

        print()
        continuar = input("Deseja cadastrar outro candidato? (S/N): ").upper()

print("\n=== Resumo do processo ===")
print(f"Total de tentativas: {contador}")
print(f"Total de cadastros aceitos: {cadastro}")
print("Fim do processo.")
