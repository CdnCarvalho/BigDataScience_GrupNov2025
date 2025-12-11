
# import os
# os.system('cls')

# ------------------------------------------------- random.randint para gerar números aleatórios
import random
n = random.randint(1, 10)
m = random.randint(1, 10)
print(n, m)


# ------------------------------------------------- Gerar números aleatórios, dentro de uma lista
lst_numeros = [random.randint(1, 10) for num in range(5)]
print(lst_numeros)


# ------------------------------------------------- Gerar números decimais aleatórios
n_decimal = random.uniform(1, 10)
print(n_decimal)


# ------------------------------------------------- Gerar entre 0 e 1
n = random.random()
print(n)

