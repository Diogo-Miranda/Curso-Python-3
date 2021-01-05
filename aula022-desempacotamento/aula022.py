"""""
Desempacotamento de listas em Python
"""""

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista  # Desempacotamento em python
print(n2)

# O que sobra, cria-se uma outra lista com o restante dos valores
n1, n2, *outra_lista = lista  # Evita error too my values
print(n1, n2)

lista2 = ['Diogo', 'Araujo',1,2,3,4,5,6,100]
n1, n2, *outra_lista, ultimo_lista = lista2
print(n1, n2, outra_lista, ultimo_lista)
