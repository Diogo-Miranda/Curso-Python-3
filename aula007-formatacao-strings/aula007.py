nome = 'Diogo'  # String
idade = 20  # int
altura = 1.80  # float
ehMaior = idade > 18  # boolean
peso = 80  # integer
imc = peso/altura**2

# f strings #
print(f'{nome} tem {idade} anods de idade e seu imc é {imc:.2f}')  # exibe valores formatados
# exibe dois valores de ponto flutuante

# function format #
print('{2} {0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))  # existe uma ordem (0,1,2)
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))  # existe uma ordem (0,1,2)

