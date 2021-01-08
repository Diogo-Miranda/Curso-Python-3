"""""
Funções (def) em Python - *args **kwargs - 
Aula 16 (Parte 3)
"""""

def fuc(a1, a2, a3, nome=None, a6=None):
    print("Função com argumento default")

def func(*args):  # retorna uma tupla
    print(args)
    print(f'Tamanho = {len(args)}')
    args = list(args)  # transforma de tupla -> lista
    args[0] = 20
    print(args)

# Desempacotando uma lista
lista = [1,2,3,4,5,6]
print(*lista, sep='-')

# Mesma coisa com *args
func(1,2,3,4,5)  # Retornam como uma tupla
func(lista)  # Lista no primeiro índice da tupla
func(*lista)  # Envia a lista desempacotada
lista2 = [1,2,3,4,5,6,7,8,7,8,9,2]
func(*lista, *lista2)  # Mescla as listas

# key words arguments (com palavras chaves)
def func2(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print(nome, sobrenome)

func2(*lista, *lista2, nome="Diogo", sobrenome="Miranda")

