""""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe ue não é um número inteiro
"""""

num = input('Digite um número: ')

# Verificar se é um número inteiro

if num.isdigit():
    num = int(num)
    # Calcular se é par ou ímpar
    if num % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
else:
    print('Não é um número inteiro')
