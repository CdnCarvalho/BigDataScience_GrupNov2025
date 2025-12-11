# Função que calcula e mostra o total de uma venda
def calcular_venda(preco, quantidade):
    total = preco * quantidade
    print(f"Total da venda: R$ {total:.2f}")


# Programa principal
print("=== Cálculo de 3 vendas ===")
for i in range(1, 4):
    print(f"\n--- Venda {i} ---")
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade vendida: "))

    calcular_venda(preco, quantidade)