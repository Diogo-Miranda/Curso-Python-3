"""""
Criar uma estrutura de repetição.
Criar dois contadores:
- Um conta de maneira progressiva
- Um conta de maneira regressiva
0 10
1 9
2 8
3 7
4 6 
...
"""""

# Minha solução
counter = list(range(1, 11))
for index, value in enumerate(counter):
    print(index, counter[len(counter)-index-1])

print('===')

# Outra solução
for index, r in enumerate(range(10, 1, -1)):
    print(index, r)
