# len = retorna o tamanho de algum tipo

print("Diogo".__len__())  # <--- Isso que acontece
# len(str)

# tamanho de uma String
usuario = input('Digite seu usuário: ')
qntCaracteres = len(usuario)
print(usuario, qntCaracteres, type(qntCaracteres))

if qntCaracteres < 6:
    print('Usuário inválido, digite pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitado foi: {len(string1) + len(string2)}')
