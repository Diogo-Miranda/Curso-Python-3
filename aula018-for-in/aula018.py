""""
For in em Python
Iterando string com for
Função range(start=0, stop, step=1)
"""""
texto = 'Python'

# enumerate
for n, letra in enumerate(texto):
    print(n, letra)

# for in
for letra in texto:
    print(letra)

# usando função range
for numero in range(10):
    print(numero)

for n in range(5, 10, 1):  # init=5 end=10 step=1
    print(n)

for n in range(20, 10, -1):  # init=20 end=10 step=-1
    print(n)
