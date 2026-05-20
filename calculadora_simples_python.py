historico = []

num1 =float(input('digite um numero: '))
num2 =float(input('digite outro numero: '))

operador = str(input('Escolha a opereção que dejesa(+ - * / ): '))

if operador == '+':
    resultado = num1 + num2
    print(f'o resultado da sooma dos numero é: {resultado}')
elif operador == '-':
    resultado = num1 - num2
    print(f'o resultado da subitração é: {resultado}')
elif operador == '*':
    resultado = num1 * num2
    print(f'o resuldado da mulriplicação é: {resultado}')
elif operador == '/':
    resultado = num1 / num2
    print(f'o resultado da divisão é: {resultado}')

historico.append(f'{num1} {operador} {num2} = {resultado}')

while True:
    cont = input('\ndeseja continuar ("s") deseja sair ("n"): ')
    if cont == 's':
        num1 =float(input('digite um numero: '))
        num2 =float(input('digite outro numero: '))
        operador = str(input('Escolha a opereção que dejesa(+ - * / ): '))

        if operador == '+':
            resultado = num1 + num2
            print(f'o resultado da sooma dos numero é: {resultado}')
        elif operador == '-':
            resultado = num1 - num2
            print(f'o resultado da subitração é: {resultado}')
        elif operador == '*':
            resultado = num1 * num2
            print(f'o resuldado da mulriplicação é: {resultado}')
        elif operador == '/':
            resultado = num1 / num2
            print(f'o resultado da divisão é: {resultado}')
        historico.append(f'{num1} {operador} {num2} = {resultado}')

    elif cont == 'n':
        print('você saiu da area de calculos!')
        break

visu_hist = input('deseja ver historico da calculadora? (s / n): ')
if visu_hist == 's':
    for item in historico:
        print(f' -{item}')
elif visu_hist == 'n':
    print('voce escolheu nao ver o historico')
