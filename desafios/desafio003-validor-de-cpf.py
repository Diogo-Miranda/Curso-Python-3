cpf = ''.join((''.join(input("Informe o CPF (XXX.XXX.XXX-XX): ").split('.'))).split('-'))

# Validar primeiro dígito
firstSum = 0
for index, counter in enumerate(range(10, 1, -1)):
    firstSum += (int(cpf[index]) * counter)
    # print(f'{cpf[index]} * counter = {firstSum}')

# Verificar primeiro dígito
firstDigit = 11 - (firstSum % 11)
if firstDigit > 9:
    firstDigit = 0
print(f'Digito 1 = {firstDigit}')

# Validar segundo digito
secondSum = 0
for index, counter in enumerate(range(11, 1, -1)):
    secondSum += (int(cpf[index]) * counter)

# Verificar segundo digito
secondDigit = 11 - (secondSum % 11)
print(f'Digito 2 = {secondDigit}')
