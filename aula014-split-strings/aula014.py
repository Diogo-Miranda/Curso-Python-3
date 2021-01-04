""""
* String indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""""

# positivos  [01234]
texto     =  'Diogo'
# negativos -[43210]

url = 'www.google.com.br/'

print(url[:-1])  # remove o último caractere

string = 'Python_s2'
nova_string = string[2:6]  # fatia do índice 2 ao 6
print(nova_string)
nova_string = string[:6]  # pega até o índice 6 (5)
print(nova_string)
nova_string = string[7:]  # pega do 7 até o final
print(nova_string)

# pular caracteres
nova_string = string[0::2]  # começa do 0 passo 2
print(nova_string)
# inverter string
nova_string = string[::-1]
print(nova_string)
