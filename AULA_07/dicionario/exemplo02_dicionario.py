# Lista para armazenar os vendedores que bateram a meta
vendedores_com_meta = []

# Meta de vendas
meta = 5000

# Coleta de dados dos 5 vendedores
for i in range(2):
    print(f"\nCadastro do {i+1}º vendedor:")
    nome = input("Nome: ")
    valor_vendas = float(input("Valor vendido: "))
    regiao = input("Região: ")

    # Verifica se bateu a meta
    if valor_vendas >= meta:
        vendedor = {
            'nome': nome,
            'vendas': valor_vendas,
            'regiao': regiao
        }
        vendedores_com_meta.append(vendedor)
        print("Meta alcançada!")
    else:
        print("Meta não alcançada.")

# Exibindo quem bateu a meta
print("\nVendedores que bateram a meta:")
for v in vendedores_com_meta:
    # print(v)
    print(f"{v['nome']} - R${v['vendas']} - Região: {v['regiao']}")