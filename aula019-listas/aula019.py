""""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""""

# Podem ser de vários tipos diferentes uma lista
lista = ['Diogo Araujo', 'A', 'B', 'C', 'D', 'E', 1.5]

# Operações
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

# Comando extend
l1.extend(l2)
print(l1)
l1.extend('a')
print(l1)

# Comando append = insere no final
l2.append('b')
print(l2)

# Comando insert = insere em qualquer lugar da lista
l2.insert(0, 'banana')
print(l2)

# Comando del = deletar
del(l1[1:3])
print(l1)

l1 = [1, 2, 3, 4, 5, 6, 7]

# Maior e menor (max and min)
print(max(l1))
print(min(l1))

# Usando range
l2 = list(range(0, 100, 8))  # Retorna uma Lista (objeto iterável) múltiplos de 8
print(l2)

# Iterando listas
for valor in l2:
    print(valor)

# Checar tipos
l4 = ['String', True, 10, -20.5]
for elem in l4:
    print(f'O tipo de elem é {type(elem)} e o seu valor é {elem}')

# Joguinho de advinhar
secreto = 'perfume'
digitadas = []

ganhou = False
while not ganhou:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra')
    else:
        digitadas.append(letra)
        print(digitadas)
        if letra in secreto:
            print(f'A letra "{letra}" existe na palavra secreta')
        else:
            print(f'A letra "{letra} não existe na palavra secreta')

        secretoTemporario = ''
        for letraSecreta in secreto:
            if letraSecreta in digitadas:
                secretoTemporario += letraSecreta
            else:
                secretoTemporario += '*'

        if secretoTemporario == secreto:
            print(f'Que legal, você ganhou! A palavra era: {secreto}')
            ganhou = True
        else:
            print(f'A palavra secreta está assim: {secretoTemporario}')