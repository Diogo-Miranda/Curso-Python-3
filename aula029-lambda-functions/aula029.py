"""""
São funções anônimas
"""""

a = lambda x, y: x * y

print(a(2, 2))

# Exemplo
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 20],
    ['P5', 8]
]

lista.sort(key=lambda item: item[1])  # Do maior pro menor
print(lista)

# Ordena sem alterar a lista
print(sorted(lista, key=lambda item: item[1]))
