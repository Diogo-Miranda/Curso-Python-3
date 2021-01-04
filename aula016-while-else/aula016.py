""""
While / Else - Aula 8
contadores
acumuladores
"""""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador)
    acumulador += contador
    contador += 1
else:  # Usado para quando a expressão for em algum momento falsa
    print(f'Fim... Valor acumulado: {acumulador}')