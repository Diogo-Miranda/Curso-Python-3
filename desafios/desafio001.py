"""
* Criar variáveis para nome (str), idade (int),
* Altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o imc da pessoa com 2 casas decimas (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com chaves)
"""

nome = "Diogo"
idade = 20
peso = 74.0
altura = 1.77
anoAtual = 2021
anoNascimento = anoAtual - idade
IMC = peso/altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {IMC:.2f}')
print(f'{nome} nasceu em {anoNascimento}')
