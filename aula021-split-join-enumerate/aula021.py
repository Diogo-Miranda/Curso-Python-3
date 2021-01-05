""""
Split, Join, Enumarate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumarate - Enumerar elementos da lista # interáveis
* strip() - remove espaço do fim e no inicio
* capitalize() - coloca primeira letra maiuscula
"""""

# Split
string = "O brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)} vezes na frase') # Conta quantas vezes apareceu na frase

# Join
string = "o Brasil é penta."
lista = string.split(' ')
string2 = ','.join(lista).capitalize().strip()  # Junta todos os elementos da lista em uma string a partir de vírgula

print(string2)

# Enumerate (retorna tuplas)
for indice, valor in enumerate(lista):  # Enumera a lista de acordo com o indice
    print(indice, valor)

# O que a função Enumerate faz (desempacota)
lista = [[0, "Diogo"], [1, "João"], [2, "Maria"]]  # Lista com listas
for indice, nome in lista:
    print(indice, nome)
