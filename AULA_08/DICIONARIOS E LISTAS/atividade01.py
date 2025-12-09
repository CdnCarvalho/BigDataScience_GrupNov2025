vendedores = []

for i in range(3):
    print(f"\n--- Vendedor {i+1} ---")
    nome = input("Nome do vendedor: ")

    vendas = []
    for v in range(5):
        valor = float(input(f"Valor da venda {v+1}: R$ "))
        vendas.append(valor)

    total = sum(vendas)
    media = total / 5

    vendedor = {
        "nome": nome,
        "vendas": vendas,
        "total": total,
        "media": media
    }

    vendedores.append(vendedor)

print("\n--- Resultado Final ---")
for v in vendedores:
    print(f"Nome: {v['nome']}")
    print(f"Vendas: {v['vendas']}")
    print(f"Total: R$ {v['total']:.2f}")
    print(f"Média: R$ {v['media']:.2f}")
    print("-" * 20)
