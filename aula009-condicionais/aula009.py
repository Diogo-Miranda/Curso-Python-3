""""
Condições IF, ELIF e ELSE 
"""""

# O bloco if é a partir da indentação
# ELIF = else if
# Operadores relacionados
# == > >= < <= !=

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))

# Limite para pegar empréstimo
limiteMenor = 20
limiteMaior = 30

if limiteMenor <= idade <= limiteMaior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÃO pode pegar o empréstimo')


# in e not in

frase = "diogo"

if 'di' in frase:
    print("Existe.")
else:
    print("Não existe.")

if 'di' not in frase:
    print("Existe.")
else:
    print("Não existe.")
   