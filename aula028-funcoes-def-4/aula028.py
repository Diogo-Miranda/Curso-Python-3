# Escopo de variáveis em função

variavel = 'valor'

def func():
    print(variavel)

def func2():
    global variavel  # altera a global
    variavel = 'Outro valor'
    print(variavel)

func()
func2()

print(variavel)

