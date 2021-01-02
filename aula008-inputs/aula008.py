# Entrada de dados é feito por "input"

# Cria variável a atribui o input a ela
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
anoNascimento = 2021 - int(idade)

print(f'O usuário {nome} tem {idade} anos, nasceu em {anoNascimento} e o tipo das variáveis é '
      f'{type(nome)}')  # sempre irá retornar uma String

