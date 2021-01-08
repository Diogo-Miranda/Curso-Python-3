"""""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome
"""""
def saudacao(saudacao="Seja bem-vindo", nome="Diogo"):
    print(f'{saudacao} {nome}')
saudacao("Olá", "Erika")


"""""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""""
def sum(n1=0, n2=0, n3=0):
    return n1+n2+n3
print(sum(2,3,4))


"""""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual
Retorne o valor do primeiro número somado do aumento do percentual do mesmo
"""""
def sumPercent(n1, percent):
    return n1*(1+(percent/100))
result = sumPercent(100, 30)
print(result)

"""""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorn fizz,
se o parâmetro da função for divisível por 5, retorne buzz.
Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, 
caso contrário, retorne o númetro enviado
"""""
def fizzBuzz(n):
    result = n
    if n % 2 == 0 and n % 5 == 0:
        result = 'FizzBuzz'
    elif n % 2 == 0:
        result = 'Fizz'
    elif n % 5 == 0:
        result = 'Buzz'
    return result

print(fizzBuzz(11))