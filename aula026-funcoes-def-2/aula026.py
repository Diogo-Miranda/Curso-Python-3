def funcao(var):
    print(var)


def funcao2(var):
    return var


def div(n1, n2):
    if n2 > 0:
        result = n1 / n2
    else:
        result = None

    return result


variavel = funcao('Valor que eu quero')  # returna None
result = div(5, 6)
print(result)


# Recebendo funções
def f(var):
    print(var)


def dump():
    return f


var = dump()
print(id(var), id(f))  # var é o mesmo objeto que f
var('Pode imprimir algo')


# Funções também retorna tuplas
def tupla():
    return 'Diogo', 'Araujo'


var = tupla()
print(var, type(var))
