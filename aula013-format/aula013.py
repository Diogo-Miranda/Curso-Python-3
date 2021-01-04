""""
Formatando valores com modificadores 
:s - Text (Strings)
:d - Inteiros (int)
:f - números com ponto flutuante
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""""

# Casas decimais
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))  # Formatar com 2 casas após a vírgula
print(f'{divisao:.2f}')  # Formatar com f strings

# Formatar uma String
nome = 'Diogo Araujo'
print(f'{nome:s}')  # Diz que isso é uma String

# Adicionar algum caractere na impressão
num_1 = 1
# 0000000001
print(f'{num_1:0>10}')  # :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

# 6 zeros mais as 4 casas
num_2 = 1150
# 1150000000
print(f'{num_2:0<10}')

# Coloca no centro
# 0001150000
print(f'{num_2:0^10}')

# Formatar como float
print(f'{num_2:.2f}')

# Formatar com 10 casas decimais
print(f'{num_2:0>10.2f}')

# Formatar String
print(f'{nome:#^50}')  # Coloca String com 50 caracteres (50 - len(nome)) + len(nome)

# Com .format
nome_formatado = '{n:@^50}'.format(n=nome)
print(nome_formatado)

sobrenome = 'Miranda'
nome_formatado = '{0:#^20} {1:@^20}'.format(nome, sobrenome)
print(nome_formatado)
