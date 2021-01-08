# Tupla e listas são semelhantes, mas tuplas não podem ser alteradas
# tupla = ()

t1 = (1, 2, 3, 'a', 'Diogo Araujo')

print(type(t1))
print(t1)
print(t1[4])

for value in t1:
    print(value)

print(t1[2:])  # "fatiar"

t2 = 1, 2, 'a', 'b'  # também é uma tupla
print(t2)

# Tupla com 1 elemento
t1 = 1

# Concatenar tuplas
t1 = 1, 2, 3, 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2
print(t3)

# Desempacotar tuplas
n1, n2, n3, *_, n10 = t3
print(n10)

# Tupla com 1 valor
t1 = 1,  # coloca-se a vírgula

# Multiplicador de tuplas
t1 = ('Diogo',) * 20
print(t1)

# Modificar tuplas
t1 = 1, 2, 3, 4, 5
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)
print(t1)

