# https://docs.python.org/3/library/stdtypes.html

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
else:
    print('Não pude converter os número para realizar contas')

# com try
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')
