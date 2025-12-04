# LISTA PARA ARMAZENAR 5 NÚMEROS
numeros_lista = []

# Leitura dos números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros_lista.append(numero)

# Mostrando os dados
print("\nNúmeros na lista:", numeros_lista)

# Acessando o primeiro número
print("Primeiro número da lista:", numeros_lista[0])

# Alterando o primeiro número da lista
numeros_lista[0] = 99
print("Lista após alteração:", numeros_lista)

# Adicionando um novo número
numeros_lista.append(100)
print("Lista com novo número:", numeros_lista)

# Removendo um número
numeros_lista.remove(99)  # só remove se o número existir
print("Lista após remoção:", numeros_lista)

# Removendo o último número
numeros_lista.pop()

# Removendo pelo índice
del numeros_lista[0]

# Limpando a lista
# numeros_lista.clear()
print(numeros_lista)


# Segunda parte
pares = []
impares = []
for i in numeros_lista:
    if i % 2 == 0:
        pares.append(i)
        # print(f'O número {i} é par!')
    else:
        impares.append(i)
        # print(f'O número {i} é impar')

print(f'Números pares {pares}')
print(f'Números pares {impares}')
