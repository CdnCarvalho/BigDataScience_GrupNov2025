
############### ESTRUTURAS DE REPETIÇÃO ###############

# ----------------------------------------------------------- While True sem Exception
lst_vendas = []
venda = 1
tentativa = 0

while True:
    tentativa += 1
    print(f'Tentativa {tentativa}')
    valor = input(f'Informe o valor da {venda}ª venda: ')

    # Se não for um número, entra no if 
    if not valor.isdigit():
        print('Informe apenas números.\n')
        continue  # Volta para o início do loop

    valor = int(valor)
    lst_vendas.append(valor)
    venda += 1

    resposta = input('Quer continuar? [s/n]: ')[0].lower()

    if resposta == 'n':
        break  # Comando break, interrompe o loop e sai do while

print(f'Vendas registradas: {lst_vendas}')



# ----------------------------------------------------------- While True com try Except Else finally -  Letras ao invés de números)
lst_vendas = []
venda = 1
tentativa = 1

while True:
    try:
        valor = int(input(f'Informe o valor da {venda}ª venda: '))
    except ValueError:
        print('Informe apenas números.')
    except KeyboardInterrupt:
        print('\nFinalizado pelo usuário.')
        break
    else:
        lst_vendas.append(valor)
        venda += 1

        resposta = input('Quer continuar? [s/n]: ').lower()
        if resposta == 'n':
            break
    finally:
        print(f'Tentativa {tentativa} finalizada.\n')
        tentativa += 1

print(f'Vendas registradas: {lst_vendas}')


