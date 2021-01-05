"""""
For / Else em Python
"""""

lista = ['Diogo Araujo', 'Edna', 'Erika']

for valor in lista:
    if valor.startswith('D'):  # Verifica se inicia com algo
        break
else:  # Se o laço chega ao fim, ele executa o else
    print('Não existe uma palavra que começa com D')
