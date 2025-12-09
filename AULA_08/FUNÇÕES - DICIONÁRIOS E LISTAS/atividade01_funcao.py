# Função para cadastrar vendedores
def cadastrar_vendedores(qtd_vendedores):
    print("\n--- Cadastro dos vendedores ---")
    for i in range(qtd_vendedores):
        print(30 * '=')
        nome = input("Nome do vendedor: ")
        vendas = []
        
        for v in range(1, 6):
            valor = float(input(f"Valor da venda {v}: R$ "))
            vendas.append(valor)

        total = sum(vendas)
        media = total / len(vendas)

        vendedor = {
            "nome": nome,
            "vendas": vendas,
            "total": round(total, 2),
            "media": round(media, 2)
        }

        print(vendedor)
        vendedores.append(vendedor)


# Função para mostrar resultados
def mostrar_vendedores(lista_vendedores):
    print("\n--- Resultado Final ---")
    for v in lista_vendedores:
        print(f"Nome: {v['nome']}")
        print(f"Vendas: {v['vendas']}")
        print(f"Total: R$ {v['total']:.2f}")
        print(f"Média: R$ {v['media']:.2f}")
        print("-" * 20)


# Programa principal
vendedores = []
qtd = int(input("Quantos vendedores deseja cadastrar? "))

cadastrar_vendedores(qtd)
mostrar_vendedores(vendedores)
