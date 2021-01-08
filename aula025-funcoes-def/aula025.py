"""""
Funções - def em python
"""""


def funcao():
    print('Hello World!')


def funcao2(msg='Olá'):
    print(msg)
    msg = msg.replace('O', '0')
    return f'{msg} replace'


variavel = funcao2()
print(variavel)
funcao()
funcao2()
funcao2("oi")
