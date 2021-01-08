"""""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2
executada
"""""
def func2():
    print("Estou na 2")

def func1(f2=func2):
    return f2()

func1()

"""""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2
executada. Faça a função1 executar duas funções que recebam um número 
diferente de arugmentos
"""""

def func4(**kwargs):
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')

    if idade is not None:
        print(f'{nome} {sobrenome} tem {idade} anos')
    else:
        print(f'{nome} {sobrenome}')

def func3(f4=func4):
    func4(nome='Diogo', sobrenome='Araujo', idade='20')


# Resolução
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Diogo')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom-Dia')
print(executando)
print(executando2)
