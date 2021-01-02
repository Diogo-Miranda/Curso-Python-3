################
# Tipos de dados
# str - string - textos
# int - inteiro - 123456 (positivo ou negativo)
# float - real/ponto flutuante - 58.5
# bool - booleano/lógico - true/false
# Tipagem dinâmica
################

print("Diogo", type('Diogo'))  # retorna o tipo do valor
print(1, type(1))
print(2.5, type(2.5))
print(10 == 10, type(10 == 10))
print("bool('')", bool(''))  # '' é false, tudo vazio avalia em falso

# Type casting
print('Diogo', type('diogo'), bool('diogo'))
print('"10"', type('10'), "int('10')", type(int('10')))
