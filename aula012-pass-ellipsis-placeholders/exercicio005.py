""""
    Faça um programa que peça o primeiro nome do usuário. 
    Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
    Se tiver ente 5 e 6 letras, escreva "Seu nome é normal";
    Maior que 6 escreva "Seu nome é muito grande".
"""""

nome = input('Digite seu nome: ')
tamNome = len(nome)

if tamNome <= 4:
    print('Seu nome é curto')
elif 5 <= tamNome <= 6:
    print('Seu nome é normal')
elif tamNome > 6:
    print('Seu nome é longo')
