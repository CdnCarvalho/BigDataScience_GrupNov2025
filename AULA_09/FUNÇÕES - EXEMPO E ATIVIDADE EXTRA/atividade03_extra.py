# Em uma loja, o salário dos vendedores é composto por um valor fixo de R$1600
# mais uma comissão de 5%, baseada no valor das vendas realizadas no mês.
# O gerente precisa de um programa, que calcule o valor total do salário a ser
# pago para os vendedores, com base nas vendas e no percentual de comissão.
# Requisito:
# Crie uma função, que receba o valor das vendas, comissão, calcule e retorne
# o salário total do vendedor. Considere no exemplo Vendas como R$ 5000.00

def calcula_salario(ven, com, sal_fixo):
    valor_comissao = ven * (com / 100)
    sl_final = sal_fixo + valor_comissao
    return sl_final


vendas = 5000.00
comissao = 5
SALARIO_FIXO = 1600.00

salario_vendedor = calcula_salario(vendas, comissao, SALARIO_FIXO)

print(f'O salário total do vendor é: {salario_vendedor}')